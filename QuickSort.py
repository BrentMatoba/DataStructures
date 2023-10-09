unsorted=[0, 8, 5, 3, 20, 2, 9]
#recursive algorithm
#think pivot

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
    if array.length > 2:
        return array
    else:
        #sort
        print("beep")


def medianOfThree(array):
    #returns pivot point of array using medianOfThree technique
    first = array[0]
    mid = array[int(len(array)/2)]
    last = array[len(array) - 1]
    
    #sorts first, mid, and last numbers of array into ascending order
    #yes I am aware there is a sort() function in Python but for the purposes of this exercise I'm going to avoid using it.
    if first > last:
        first, last = last, first
    if first > mid:
        first, mid = mid, first
    if mid > last:
        mid, last = last, mid
    
    return mid

def pivotToEnd(pivot, array):
    array[pivot], array[len(array)-1] = array[len(array)-1], array[pivot]
    #move pivot to final spot in array
        #this isn't strictly necessary but probably better for humans
    #find itemFromLeft, the first item from the left larger than the pivot
    #find itemFromRight, the first item from the right smaller than the pivot
    #swap
    #repeat until itemFromLeft has a greater index than itemFromRight
    #swap itemFromLeft with pivot.
    #recursively call the function





print(unsorted)
pivot = medianOfThree(unsorted)
pivotToEnd(pivot, unsorted)
print(unsorted)

    