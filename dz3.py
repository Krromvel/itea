#Задача 1
a=input('Введіть рядок: ').split()
print(max(a,key=len))


# Задача 2
a=input("Введіть ненормований рядок: ").strip()
if a.count('  ')>0:
    while a.count('  ')>0:
        b=a.replace('  ', ' ')
        a=b
    print(a)
