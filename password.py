import random
lower="abcdefghijklmnopqrstuvwxyz"
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number="0123456789"
symbols="!@#$%^&*()+{}[]?/.,<>"
all_char=lower+upper+number+symbols
leng=int(input("enter length:"))
password=''.join(random.sample(all_char,leng))
print("GENERATE PASSWORD:", password)
