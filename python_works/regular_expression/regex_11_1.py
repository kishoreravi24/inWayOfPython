import re
txt = "4567-8910-1231-3333"
x = re.findall("^[456]{1}(?:([0-9])(?!.*\1)){3}-(?:([0-9])(?!.*\1)){4}-(?:([0-9])(?!.*\1)){4}-(?:([0-9])(?!.*\1)){4}$", txt)
print(x)
if x:
  print("Matches")
else:
  print("No match")