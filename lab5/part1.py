import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
# print(x)

#1
txt = "The rain in abbbb"
x1 = re.search("ab*", txt)
# print(x1)


#2
txt = "aaa abbb abb"
x2 = re.search("ab{2,3}", txt)
# print(x2)

#3
txt = "abc_b a_dc"
x3 = re.search("._.", txt)
# print(x3)

#4
txt = "abcb Adc"
x4 = re.search("[A-Z][a-z]", txt)
# print(x4)

#5
txt = "fbfdbdbadfdfdfb"
x5 = re.search("a.*b", txt)
# print(x5)

#6
txt = "a,fd.,df    ,d,ff,,,,,"
x6 = re.sub("[,. ]", ":", txt)
# print(x6)


#7
txt = "my_Function"
x7 = re.sub("_", "", txt)
# print(x7)

#8
txt = "thisIsAString"
x8 = re.split("(?=[A-Z])", txt)
# print(x8)

#9
txt = "thisIsAString"
x9 = re.sub("(?<=[a-zA-Z])(?=[A-Z])", ' ', txt)
print(x9)

#10
txt = "camelCaseString"
x10 = re.sub("([a-z])([A-Z])", "\\1_\\2", txt).lower()
# print(x10)
