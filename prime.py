b=input()
a=int(b)
if(a<=1000):
    if(((a%2)==0) or ((a%3)==0) or ((a%5)==0)):
     print("no")
    else:
     print("yes")
else:
    print("no")
