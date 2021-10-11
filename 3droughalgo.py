# we have the height, breadth and length values from the python script
# which we need to use in this algorithm
# this script also needs to take into account the remaining space left in the target bin. for this, it needs to work with openCV
# in order to get the coordinates and the contours which will give the space left in the bin.


if(binWidth < binHeight and binWidth < binDepth):
    packByWidth = True
    packByHeight = False
elif(binDepth<binHeight and binDepth<binWidth):
    packByWidth = False
    packByHeight = False
    #this implies that packing by depth is true
elif(binHeight<binDepth and binHeight<binWidth):
    packByHeight = True
    packByWidth = False

def toPack():
    toPack = notPacked
    notPacked = {}
    # Create a new bin called currentBin and check whether the item toPack[0]
    # is able to fit in this bin at position (x,y,z)=(0,0,0).
    # if toPack[0] does not fit then rotate it (over the six rotation types) until it fits and pack it
    # into this bin at postion (0,0,0).
    i = 1
    for i in range (sys.getsizeof(toPack) - 1):
        currentItem = toPack[i]
        fitted = False
    p = 0
    for p in range(2):
        k = 0
        while (k < numberOfItems in currentBin) and (not fitted):
            binItem = currentBin[k]
            if(packByWidth):
                pivot = p
            elif(packByHeight):
                # compute pivot point p for height
                else
                    #compute pivot point p for depth
            
            # switch (pivot)
            # {
            # case 0 : Choose (pivotX, pivotY, pivotZ ) as the back lower right corner of binItem
            # break
            # case 1 : Choose (pivotX, pivotY, pivotZ ) as the front lower left corner of binItem
            # break
            # case 2 : Choose (pivotX, pivovY, pivotZ ) as the back Upper left corner of binItem
            # break
            # }
            
            
if(currentItem can be packed in currentBin at position(pivotX,pivotY,pivotZ)):
    pack currentItem in currentBin at (pivotX,pivotY,pivotZ)
else:
    #try rotating the item
    while notPacked has at least one Item in it:
    rotate(currentItem)
           
    while (currentItem cannot be packed in currentBin at position(pivotX,pivotY)) and (not all rotations for currentItem checked)
            
    if (currentItem can be packed in currentBin at position(pivotX,pivotY,pivotZ)):
        Pack currentItem into currentBin at position(pivotX, pivotY ,pivotZ)
        fitted=true
    else:
        restore currentItem to original rotation type
        
    if(notFitted):
        Add currentItem to the list notPacked 