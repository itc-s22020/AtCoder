#[AC] 448Byte 25ms 8892KB Python3
def check_sequence(nums):
    # 条件1: 広義単調増加
    if not all(nums[i] <= nums[i+1] for i in range(len(nums)-1)):
        return "No"
    # 条件2: 100以上675以下
    if not all(100 <= num <= 675 for num in nums):
        return "No"
    # 条件3: 25の倍数
    if not all(num % 25 == 0 for num in nums):
        return "No"
    return "Yes"
 
nums = list(map(int, input().split()))
print(check_sequence(nums))
