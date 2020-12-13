h = int(input('Введіть висоту: '))
for i in range(h):
    a=h-i
    b=h+i
    for j in range(b+1):
        if j>=a:
            print("^", end="")
        else:
            print("", end=" ")
    else:
        print()