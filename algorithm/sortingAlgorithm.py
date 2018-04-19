# -*- coding: utf-8 -*-

# 冒泡排序
def sortingAl(nums):
    # print(nums);
    for i in range(len(nums)-1,0,-1):
        for j in range(0,i):
            if nums[j]>nums[j+1]:
                tmp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = tmp
    return nums

def sortingAl2(nums):
    for i in range(0,len(nums)-1):
        size = len(nums)-i;
        for j in range(0,size):
            if nums[i]>nums[i+j]:
                tmp = nums[i]
                nums[i] = nums[i+j]
                nums[i+j] = tmp
    return nums
def sortingAl3(nums):
    for i in range(0,len(nums)-1):
        size = len(nums)-i;
        for j in range(0,size):
            if nums[i]>nums[i+j]:
                tmp = nums[i]
                nums[i] = nums[i+j]
                nums[i+j] = tmp
    return nums



if __name__ == '__main__':
    nums = [5, 3, 7, 9, 2, 7]
    print(sortingAl(nums))
    print(sortingAl2(nums))