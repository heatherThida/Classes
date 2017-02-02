for i in range(0, 5):
    x = 10
    print(i)
print()
print("final: ", i, " ", x)
print()

for i in ["kitten", 7, "hello", 193]:
    print(i)

for i in "hello":
    print(i)

x=0
while x<5:
    print("spam")
    x=x+1
    if(x==3):
        break
else:
    print("else")

ls = ["Hello", "kitty", "cat"]
for i in ls:
    for j in i:
        print(j)
