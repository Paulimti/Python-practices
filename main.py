mile=5280
feet= mile *13
print("13 Miles is equal to:", feet, "feet")

hours=7
minutes=21
sec=37
total_sec=(hours*3600)+(minutes*60)+sec
print(total_sec, "seconds")

l=4
w=7
perimeter=(2*w)+(2*l)
area= w*l
print("perimeter: ", perimeter, "Inches")
print("Area: ", area, "sq.inch")

r=8
circum= 2*3.14*r
area = 3.14*(r**2)
print("Circumference",circum, "inches")
print("Area",area, "sq.inch")

#concatination

name1='firstname'
name2='lastname'
print(name1+' '+name2)


str1,str2='Hello!', 'Welcome to python'
print(str1+" "+str2)

# repetition

str1="firstname "
print(str1*10)

#slicing

str1="Programiz"
x=len(str1)
print(x)
print(str1[-8:-6]) #end will go like (end-1)


str= 'Hello'
print(str)