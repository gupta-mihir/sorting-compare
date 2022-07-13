from typing import List
from urllib.parse import _NetlocResultMixinBytes


msg = "This is a sorting program. We will compare all the popular sorting algorithms to see which is the best."
print(msg)
print("This is when the sorting program start")


def bin_sort(self, nums: List[int]) -> List[int] :
    #do stuff BINARY SORT

    print("Binary Sort")

def bubble(nums) :
    print("Bubble Sort")
    n = len(nums)

    for i in range(n):
        for j in range(0, n - i - 1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]


def bucket(self, nums: List[int]) -> List[int] :
        #do stuff bubble sort 
    print("Bucket Sort")

def counting(self, nums: List[int]) -> List[int] :
    #do stuff bubble sort 
    print("Counting Sort")
        
def heap(nums) :
    #do stuff bubble sort 
    print("Heap Sort")

def insertion(nums):
    #do stuff bubble sort 
    print("Insertion Sort")
    for i in range(1, len(nums)):
        print ("% d" % nums[i])
    for i in range(1, len(nums)):
 
        key = nums[i]
 
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >= 0 and key < nums[j] :
                nums[j + 1] = nums[j]
                j -= 1
        nums[j + 1] = key
    print("Sorted Array")
    for i in range(1, len(nums)):
        print ("% d" % nums[i])

def merge(nums)  :
    #do stuff bubble sort 
    print("Merge Sort")




def quick(self, nums: List[int]) -> List[int] :
    #do stuff bubble sort 
    print("Quick Sort")

def radix(self, nums: List[int]) -> List[int] :
    #do stuff bubble sort 
    print("Radix Sort")

def selection(self, nums: List[int]) -> List[int] :
    #do stuff bubble sort 
    print("Selection Sort")

arr = [64, 34, 25, 12, 22, 11, 90]
  
bubble(arr)
  
print("Sorted array is:")
for i in range(len(arr)):
    print("%d" % arr[i], end=" ")
print(" \n")
merge(arr)
insertion(arr)
