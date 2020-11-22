s = 0
text=input()
for i in text:
  if i.isdigit():
    s += int(i)
print(s)
