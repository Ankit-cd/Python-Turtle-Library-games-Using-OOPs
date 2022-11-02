y=int(input())
x=input()
c=""
for i in x:
    for j in range(y):
        c=c+i
    if c in x:
        x=x.replace(c,"")
    c=""
print(type(x))
print(type(y))

# a=int(input())
# x=input()
# print(a)
# print(x)
# print(type(a))
# print(type(x))