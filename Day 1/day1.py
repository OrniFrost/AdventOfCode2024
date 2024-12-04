
def read_and_stock(list_1, list_2):
    file = open("input.txt", "r")
    while True:
        content=file.readline()
        if not content:
            break
        content_split = content.split()
        list_1.append(int(content_split[0]))
        list_2.append(int(content_split[1]))
    file.close()

def calcul_sum_of_difference(list_1, list_2):
    sum = 0
    for i in range(len(list_1)):
        if list_2[i] >= list_1[i]:
            sum += list_2[i] - list_1[i]
        else:
            sum += list_1[i] - list_2[i]
    return sum


list_1 = []
list_2 = []
read_and_stock(list_1, list_2)
list_1.sort()
list_2.sort()
print(calcul_sum_of_difference(list_1,list_2))
