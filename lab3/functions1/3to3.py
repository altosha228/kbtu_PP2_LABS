def check(nums):
  prev = None
  for i in nums:
    if(i == prev and i == 3):
      return True
    prev = i
    continue
  return False

nums = [3, 3, 1, 4]
nums2 = [3, 1, 3, 1]
print(check(nums))
print(check(nums2))