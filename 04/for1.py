# for i in range(5, 20, 2):
#     print(i)

# names = ["Ada", "Ruby", "Julia"]

# for i in range(len(names)):
#     print(i, " : ", names[i])

# for index, value in enumerate(names):
#     print(index, " : ", value)

pa = ""
magic = "hokuspokus"
for num in range(2, 10, 2):
    pa = pa + str(num) + magic[num]
    print(pa)