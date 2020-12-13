'''
Hello world!
Привет мир!
One, two, three
Один, два, три
'''
with open ("file.txt", encoding="utf-8") as file:
    lines = 0
    letters = 0
    for line in file:
        line=line.strip()
        lines += 1
        letters=len(line)
        words = 0
        line = line.split()
        words=len(line)
        print(line, letters, "симв.", words, "сл.")
print(lines, "рядки")



# with open ("file.txt", encoding="utf-8") as file:
#     lines = 0
#     letters = 0
#     for line in file:
#         line=line.strip()
#         lines += 1
#         letters=len(line)
#         flag=0
#         words = 0
#         line = line.split()
#         words=len(line)
#         # for words in line:
#         #     if words != " " and flag==0:
#         #         words += 1
#         #         flag = 1
#         #     elif words == " ":
#         #         flag = 0
#         print(line, letters, "симв.", words, "сл.")
# print(lines, "рядки")