x=input()
a=""
for i in x:
    if i.isdigit():
        if int(i)==0 or int(i)==1:
            a+=i
print(len(a)==len(x))

