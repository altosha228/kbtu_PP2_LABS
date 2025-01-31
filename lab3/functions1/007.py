def spyGame(nums):
  prevprev = None
  prev = None
  for i in nums:
    if(i == 7 and prev == 0 and prevprev == 0):
      return True
    prev = i
    prevprev = prev
      
  return False

nums = [0, 0, 7, 1, 2, 3]
nums2 = [1, 2, 3, 4, 0, 0, 7]
nums3 = [0, 1, 2, 3]
print(spyGame(nums))
print(spyGame(nums2))
print(spyGame(nums3))