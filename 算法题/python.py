"""

1、只出现一次的数字
    作者: VAME

"""

def str2List(nums):
    numsList = list(int(i) for i in nums if i.isdigit())
    return numsList

def singleNumber(nums):
    result = 0
    for num in nums:
        result ^= num
    return result

nums = input('输入：')
numsList = str2List(nums)
res = singleNumber(numsList)
print(f'输出：{res}')