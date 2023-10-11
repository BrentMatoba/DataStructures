unsorted=[0, 8, 5, 3, 20, 2, 9]
#recursive algorithm
#keyword: pivot
#Time Complexity: Worst case: O(n^2), average case:O(nlogn)


#The pivot is the point around which the rest of the array is sorted.
#pivot MUST meet three conditions after being sorted
#this is the win condition

#pivot rules:
#1)Pivot in the correct position in the final, sorted array
    #all items on the left are smaller, and all numbers on the right are larger
#2)Items to the left are smaller
#3)Items to the right are larger



#Pseudocode
#check length        
    #solo items are already sorted
#find pivot
    #median of three
#move pivot to final spot in array
    #this isn't strictly necessary but probably better for humans
#find itemFromLeft, the first item from the left larger than the pivot
#find itemFromRight, the first item from the right smaller than the pivot
#swap
#repeat until itemFromLeft has a greater index than itemFromRight
#swap itemFromLeft with pivot.
#recursively call the function




    



def checkLength():
    if array.length <= 2:
        return array
    else:
        #sort
        print("beep")


def medianOfThree(array):
    #returns pivot point of array using medianOfThree technique
    
    firstIndex = 0
    midIndex = len(array)//2
    lastIndex = len(array)-1
    
    first = array[0]
    mid = array[int(len(array)/2)]
    last = array[len(array) - 1]
    
    #sorts first, mid, and last numbers of array into ascending order
    #yes I am aware there is a sort() function in Python but for the purposes of this exercise I'm going to avoid using it.
    if first > mid:
        if first < last:
            midIndex = firstIndex
        elif mid > last:
            midIndex = midIndex
        else:
            midIndex = lastIndex
    elif first < mid:
        if mid < last:
            midIndex = midIndex
        elif first > last:
            midIndex = firstIndex
        else:
            midIndex = lastIndex
    else:
        midIndex = firstIndex

    return midIndex
    

def pivotToEnd(pivot, array):
    #move pivot to final index of array
    array[pivot], array[len(array)-1] = array[len(array)-1], array[pivot]


#find itemFromLeft, the first item from the left larger than the pivot
def getItemFromLeft(pivot, array):
    i = 0
    seeker = array[i]
    while i <= len(array)-1:
        if seeker >= pivot:
            return i
        i+=1
        seeker = array[i]

    return i
def getItemFromRight(pivot, array):
    
    #gets last item of array that is not the pivot
    i = len(array)-2
    seeker = array[i]

    while i >= 0:
        if array[i] < pivot:
            return i
        i -=1
        seeker = array[i]

    return i
        

def swapIndex(array, left, right):
    #swaps two indexes within a given array
    array[left], array[right] = array[right], array[left]

def splitList(array):
    midpoint = len(array)//2
    halfOne = array[:midpoint]
    halfTwo = array[midpoint:]
    return halfOne, halfTwo
#find itemFromRight, the first item from the right smaller than the pivot
    #repeat until itemFromLeft has a greater index than itemFromRight
    #swap itemFromLeft with pivot.
    #recursively call the function






def quickSort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = medianOfThree(unsorted)
        pivotToEnd(pivot, unsorted)
        itemFromLeft = getItemFromLeft(pivot, unsorted)
        itemFromRight = getItemFromRight(pivot, unsorted)
        swapIndex(unsorted, itemFromLeft, itemFromRight)
        halfOne, halfTwo = splitList(unsorted)
        print(halfOne, halfTwo)
        #divide array into two halves, each gets a recursion
quickSort(unsorted)
print(unsorted)



#to'dos
#remember to move pivot back
#research recursion
#finish quickSort recursion


    