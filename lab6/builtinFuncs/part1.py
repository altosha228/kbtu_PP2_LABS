import math

def multiply_list(list) :
  return math.prod(list)

list = [1, 2, 3, 4, 5]
# print(multiply_list(list))


def countCaseLetters(str):
  uppers = 0
  lowers = 0
  for char in str:
    if(char.isupper()):
      uppers += 1
    else:
      lowers += 1
  return uppers, lowers


string = "AAAaaBb"
ups, lows = countCaseLetters(string)
# print(ups, lows)


def isPalindrome(str):
  return str[::-1] == str

string = "аргентинаманитнегра"
print(isPalindrome(string))