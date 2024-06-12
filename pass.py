from time import sleep
print("you should give me the password that:\n 1. has at least 6 characters \n 2. has an appercase letter\n 3.has a symbol from the list below:\n '.' , '_' , '/', '?'")
sleep(1)
n = input("type the password")
# 6 characters
# at least 1 capital letter
# at least 1 symbol
x = 0
up = 0
symb_num = 0
symbols_list = [".", "_", "/", "?"]
while x<len(n):
  for j in n:
    x += 1 
    if j.isupper() is True:
      print(j)
      up += 1 
      print(up)
    if j in symbols_list:
      print(j)
      symb_num += 1
      print(symb_num)
    print(x)
else:     
  if up >= 1 and symb_num >= 1 and x >= 6:
    print("correct")
  else:
    print("incorrect")
