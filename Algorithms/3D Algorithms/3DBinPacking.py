# -*- coding: utf-8 -*-

# bin [0.42,0.225,0.31]
# box [0.18, 0.09, 0.06]

import copy
from math import ceil

class Bin(object):
    def __init__(self, name, length, width, depth):
        self.name = name

        # dimensions
        self.length = int(length)
        self.width = int(width)
        self.depth = int(depth)

        # bin's items
        self.bin_items = []

        # 3D representation for the bin
        self.vector_3D = []
        self.build_vector()

    def build_vector(self):
        # 3D - Vector
        for i in range(0, self.length):
            new_list1 = []

            for j in range(0, self.width):
                new_list2 = []

                for k in range(0, self.depth):
                    new_list2.append(0)

                new_list1.append(new_list2)

            self.vector_3D.append(new_list1)
            
    def can_be_packed(self, item, position):    
        for i in range(position[0], position[0] + item.length):
            for j in range(position[1], position[1] + item.width):
                for k in range(position[2], position[2] + item.depth):
                    # check for bin's limits
                    if i >= self.length or j >= self.width or k >= self.depth:
                        return False

                    # check if the space is already used
                    if self.vector_3D[i][j][k] == 1:
                        return False

        # check if the item above another item has at least half of its dimension on the "underitem"
        if position[1] >= 1:
            for i in range(position[0], ceil((position[0] + item.length) / 2)):
                    for k in range(position[2], ceil((position[2] + item.depth) / 2)):
                        if self.vector_3D[i][position[1] - 1][k] == 0:
                            return False

        return True
    
    def pack(self, item, position):
        # add item to packed items
        self.bin_items.append(item)

        # edit 3D vector, put 1 where the item is located
        for i in range(position[0], position[0] + item.length):
            for j in range(position[1], position[1] + item.width):
                for k in range(position[2], position[2] + item.depth):
                    self.vector_3D[i][j][k] = 1

        # change item's position
        item.pos = copy.deepcopy(list(position))
        
class Item(object):
    def __init__(self,name,length,width,depth):
        
        self.name = name
        # dimensions w x h x d
        self.length = int(length)
        self.width = int(width)
        self.depth = int(depth)

        # position in the bin, if it'll be packed
        self.pos = [-1, -1, -1]

               
def bp3D(current_bin, box): # (Bin object, box to be packed)
    not_changes = True
    if(len(current_bin.bin_items)==0&(current_bin.can_be_packed(box,(0,0,0)))): # first box to be packed
        current_bin.pack(box, (0, 0, 0)) 
        return [0,0,0]
    else:
        for i in range(len(current_bin.bin_items)):
            # get current bin item
            current_bin_item = current_bin.bin_items[i]
            for p in range(3):
                # final position
                pivot = [-1, -1, -1]
                if p == 0: 
                    #pt_rt_bottom_front=>update bottom right front_x
                    pivot = [
                        current_bin_item.pos[0] + current_bin_item.length,
                        current_bin_item.pos[1],
                        current_bin_item.pos[2]
                    ]
                elif p == 1:  # pt_left_front_top=>update top left front_z
                    pivot = [
                        current_bin_item.pos[0],
                        current_bin_item.pos[1],
                        current_bin_item.pos[2] + current_bin_item.depth,
                    ]
                else: # pt_left_bottom_back=>update bottom left back_y
                    pivot = [
                        current_bin_item.pos[0],
                        current_bin_item.pos[1] + current_bin_item.width,
                        current_bin_item.pos[2]
                    ]
                if current_bin.can_be_packed(box, pivot):
                    current_bin.pack(box, pivot)
                    return box.pos #returning the position where box is being placed

        return -1 # box cannot be fit 

