def sumOfList(nums):
    if len(nums) == 0:
        return 0
    else:
        head = nums[0]
        tail = nums[1:]
        return head + sumOfList(tail)


nums = [5,2,4,8]
print('the sum of ', nums, 'is: ', sumOfList(nums))