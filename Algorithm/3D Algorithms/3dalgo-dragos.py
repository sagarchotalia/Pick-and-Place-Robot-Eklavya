import copy
from math import ceil

class Bin(object):
    def __init__(self, name, width, height, depth):
        self.name = name

        # dimensions
        self.width = int(width)
        self.height = int(height)
        self.depth = int(depth)

        

        # bin's items
        self.items = []
        self.remaining_space = self.width * self.height * self.depth

        # 3D representation for the bin
        self.vector_3D = []
        self.build_vector()

    def build_vector(self):
        # 3D - Vector
        for i in range(0, self.width):
            new_list1 = []

            for j in range(0, self.height):
                new_list2 = []

                for k in range(0, self.depth):
                    new_list2.append(0)

                new_list1.append(new_list2)

            self.vector_3D.append(new_list1)

    def print_data(self):
        print(self.name, "|", "Dimensions:", self.width, "x", self.height, "x", self.depth, "|", len(self.items), "items |", self.remaining_space, "remaining space")

    # pack the item in the current bin and edit item's properties(position and rotation type)
    def pack(self, item, position, type):
        # add item to packed items
        self.items.append(item)

        # edit 3D vector, put 1 where the item is located
        for i in range(position[0], position[0] + item.rotate(type)[0]):
            for j in range(position[1], position[1] + item.rotate(type)[1]):
                for k in range(position[2], position[2] + item.rotate(type)[2]):
                    self.vector_3D[i][j][k] = 1

        # edit remaining space
        volume = item.width * item.height * item.depth
        self.remaining_space -= volume

        # change item's position
        item.pos = copy.deepcopy(list(position))
        # change item's rotation type
        item.RT = type

    # check if the item can be packed with this properties(position and rotation type)
    def can_be_packed(self, item, position, type):
        for i in range(position[0], position[0] + item.rotate(type)[0]):
            for j in range(position[1], position[1] + item.rotate(type)[1]):
                for k in range(position[2], position[2] + item.rotate(type)[2]):
                    # check for bin's limits
                    if i >= self.width or j >= self.height or k >= self.depth:
                        return False

                    # check if the space is already used
                    if self.vector_3D[i][j][k] == 1:
                        return False

        # check if the item above another item has at least half of its dimension on the "underitem"
        if position[1] >= 1:
            for i in range(position[0], ceil((position[0] + item.rotate(type)[0]) / 2)):
                    for k in range(position[2], ceil((position[2] + item.rotate(type)[2]) / 2)):
                        if self.vector_3D[i][position[1] - 1][k] == 0:
                            return False

        return True

class Item(object):
    def __init__(self, name, width, height, depth):
        self.name = name

        # dimensions w x h x d
        self.width = int(width)
        self.height = int(height)
        self.depth = int(depth)

        if self.width <= 0 or self.height <= 0 or self.depth <= 0:
            print("Wrong item dimensions")
            exit(1)

        # position in the bin, if it'll be packed
        self.pos = [-1, -1, -1]

        # rotation type - [0; 5], see Item.rotate to know how the item is rotated
        # check readMe too
        self.RT = 0

    def print_data(self):
        print(self.name, "|", "Dimensions:", self.width, "x", self.height, "x", self.depth, "|", "Position [x, y, z]:", self.pos, "| rotation type:", self.RT)

    # rotations
    def rotate(self, type):
        if type == 0: # normal position
            return (self.width, self.height, self.depth)
        elif type == 1: # rotate Z
            return (self.height, self.width, self.depth)
        elif type == 2: # rotate Y
            return (self.width, self.depth, self.height)
        elif type == 3: # rotate X, rotate Y
            return (self.depth, self.width, self.height)
        elif type == 4: # rotate X
            return (self.depth, self.height, self.width)
        else: # rotate X, rotate Z
            return (self.height, self.depth, self.width)

class Items_List(object):
    def __init__(self):
        self.items = []

    def add_item(self, new_item):
        self.items.append(new_item)

    def delete_item(self, index):
        if len(self.items) != 0:
            if 0 <= index < len(self.items):
                del self.items[index]

    def print_data(self):
        if len(self.items) != 0:
            for index in range(len(self.items)):
                print(str(index) + ")")
                self.items[index].print_data()

def get_items_total_volume(item_list):
    volume_T = 0
    for item in item_list:
        volume = item.width * item.height * item.depth
        volume_T += volume

    return volume_T

def sort_by_volume(item_list):
    for i in range(len(item_list)):
        for j in range(len(item_list)):
            if item_list[i].width * item_list[i].height * item_list[i].depth > item_list[j].width * item_list[j].height * item_list[j].depth:
                item_list[i], item_list[j] = item_list[j], item_list[i]

    return item_list

def bp3D(current_bin, Items): # (Bin object, list of Item objects)
    # conditions, wrong arguments
    if type(current_bin) != Bin:
        print("Incorrect current_bin parameter!")
        exit(30)

    if type(Items) != list or len(Items) == 0 or type(Items[0]) != Item:
        print("Incorrect Items parameter!")
        exit(31)

    # Credits to:
       # https://www.researchgate.net/publication/228974015_Optimizing_Three-Dimensional_current_bin_Packing_Through_Simulation
    # Consider that the strategy and the algorithm from this code have been heavily changed for my needs.
    notPacked = copy.deepcopy(Items)

    # sort items by volume
    notPacked = sort_by_volume(notPacked)

    # put the first item (which is the biggest after sorting) in the current_bin
    # the item need to be small enough to fit in container
    for index in range(len(notPacked)):
        # try item's every rotation
        for rotation_type in range(6):
            # if it don't fit try the next one
            if notPacked[index].rotate(rotation_type)[0] > current_bin.width or \
                notPacked[index].rotate(rotation_type)[1] > current_bin.height or \
                notPacked[index].rotate(rotation_type)[2] > current_bin.depth:
                pass
            # if I find an item that fits, pack it and break
            else:
                current_bin.pack(notPacked[index], (0, 0, 0), rotation_type)
                del notPacked[index]
                break

        if len(current_bin.items) != 0:
            break

    # if there's no item in bin that means no item fits in the container, so.. skip
    if len(current_bin.items) != 0:
        while True:
            # if no change is detected the loop will stop
            not_changes = True

            # for every existing item in notPacked try to find a position in bin in which the item can fit
            for i in range(len(notPacked)):
                # get current item
                current_item = notPacked[i]

                # select an item from container; try to put current item in one of following 3 positions:
                    # back lower right corner of selected_bin_item
                    # front lower left corner of selected bin item
                    # back upper left corner of selected bin item
                for j in range(len(current_bin.items)):
                    # get current bin item
                    current_bin_item = current_bin.items[j]

                    # choose the available position
                    for p in range(3):
                        # final position
                        pivot = [-1, -1, -1]

                        if p == 0: # back lower right corner of current_bin_item
                            # just increase the position point from x axis with the current item width
                            pivot = [
                                current_bin_item.pos[0] + current_bin_item.rotate(current_bin_item.RT)[0],
                                current_bin_item.pos[1],
                                current_bin_item.pos[2]
                            ]
                        elif p == 1: # front lower left corner of current_bin_item
                            # just increase the position point from z axis with the current item depth
                            pivot = [
                                current_bin_item.pos[0],
                                current_bin_item.pos[1],
                                current_bin_item.pos[2] + current_bin_item.rotate(current_bin_item.RT)[2]
                            ]
                        else: # back upper left corner of current_bin_item
                            # just increase the position point from y axis with current item height
                            pivot = [
                                current_bin_item.pos[0],
                                current_bin_item.pos[1] + current_bin_item.rotate(current_bin_item.RT)[1],
                                current_bin_item.pos[2]
                            ]

                        # try to find a rotation type for packing, try all of them, see rotation function from Item class or readMe
                        for k in range(6):
                            if current_bin.can_be_packed(current_item, pivot, k):
                                # if I find a rotation which make the item fitting, choose it
                                current_bin.pack(current_item, pivot, k)
                                del notPacked[i]
                                not_changes = False
                                break

                        # Already found an item which fits, so break to reload the process
                        if not_changes == False:
                            break

                    # Already found an item which fits, so break to reload the process
                    if not_changes == False:
                        break

                # Already found an item which fits, so break to reload the proccess
                if not_changes == False:
                    break

            # If there's no changes that means there's no item that fits in the container, so break the packing process
            if not_changes:
                break