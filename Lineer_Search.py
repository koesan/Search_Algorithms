def lineer_search(liste, value):

    for index, item in enumerate(liste):
        if item == value:
            return index 
    return -1


liste = [94, 13, 14, 45, 4, 34, 11, 36, 87, 35, 47, 82, 75, 99, 54, 50, 43, 22, 10, 52, 15, 23, 42, 80, 74, 58, 16, 1, 59, 48, 42, 63, 53, 17, 23, 6, 4, 80, 50, 63, 15, 97, 4, 70, 9, 93, 33, 61, 44, 54, 28, 99, 26, 30, 95, 32, 27, 12, 28, 47, 8, 7, 80, 82, 93, 94, 36, 41, 58, 18, 64, 37, 74, 49, 80, 96, 21, 65, 53, 17, 74, 34, 28, 46, 45, 58, 59, 91, 29, 30, 38, 63, 54, 13, 89, 26, 81, 75, 21, 79]

value = 1

index= lineer_search(liste, value)

print(index)
