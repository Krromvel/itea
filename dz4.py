def bin(x):
    a=""
    while x>0:
        a = str(x%2) + a
        x//=2
    return a

while True:
    x = int(input("Введіть число: "))
    if x != 0:
        print (bin(x))
    else:
        break