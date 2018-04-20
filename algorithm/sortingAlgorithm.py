# -*- coding: utf-8 -*-

# 冒泡排序 ：临近位置反复比较更换位置，符合条件即更换位置。这样比较的复杂度梯度下降。
def sortingAl(nums):
    # print(nums);
    for i in range(len(nums)-1,0,-1):
        for j in range(0,i):
            if nums[j]>nums[j+1]:
                tmp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = tmp
    return nums
# 选择排序 ：固定坐标位置，逐一比较，符合条件即更换位置继续比较。这样比较的复杂度梯度下降。
def sortingAl2(nums):
    for i in range(0,len(nums)-1):
        size = len(nums)-i;
        for j in range(0,size):
            if nums[i]>nums[i+j]:
                tmp = nums[i]
                nums[i] = nums[i+j]
                nums[i+j] = tmp
    return nums
# 插入排序
def sortingAl3(nums):
    step = 0
    for i in range(1,len(nums)):
        for j in range(i, 0, -1):
            step += 1
            # print(step)
            flag = False
            if nums[i] < nums[j-1]:
                tmp = nums[i]
                nums[i] = nums[i-1]
                nums[i-1] = tmp
                print("step %s")
            #     flag = True
            # if flag:
            #     break
    return nums
if __name__ == '__main__':
    nums = [5, 3, 7, 9, 2, 7]
    print(sortingAl(nums))
    print(sortingAl2(nums))
    print(sortingAl2(nums))