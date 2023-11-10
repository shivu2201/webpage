string=input("enter the string")
count=0
for i in string:
    if(i=='a' or i=='e' or i=='o' or i=='i'or i=='u' or i=='A' or i=='E' or i=='O' or i=='I'or i=='U'):
        count+=1
print(count)