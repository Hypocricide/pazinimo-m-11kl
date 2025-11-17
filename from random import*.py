# from random import*
# n=int(input("Kiek elementu turi masyvas a? n="))
# a=[randint(0,5) for i in range(n)]
# print('pradinis masyvas\n', a)
# rik_pozym=1
# for i in range(n -1):
#     if rik_pozym == 0
#     break
# rik_pozym=0
# for j in range(n-2, -1, -1):
# if a[j+1]<a[j]:
#     a[j], a[j=1] =a[j+1],a[j]
#     rik_pozym +=1
# print('surikiuotas masyvas\n',a)


# from random import *

# n = int(input("Kiek elementų turi masyvas a? n = "))
# a = [randint(-10, 10) for i in range(n)]
# print("Pradinis masyvas\n", a)

# for i in range(n - 1, -1, -1):
#     for j in range(0, i):
#         if a[j] > a[j + 1]:
#             a[j], a[j + 1] = a[j + 1], a[j]

# print("Surikiuotas masyvas\n", a)


# # Masyvo elementų rikiavimas. „Burbulo“ metodas
# from random import *

# n = int(input("Kiek elementų turi masyvas a? n = "))
# a = [randint(-10, 10) for i in range(n)]
# print("Pradinis masyvas\n", a)

# for i in range(n - 1):
#     for j in range(n - 2, i - 1, -1):
#         if a[j + 1] < a[j]:
#             a[j], a[j + 1] = a[j + 1], a[j]

# print("Surikiuotas masyvas\n", a)


# from random import *

# n = int(input("Kiek zaideju komandoje? n = "))

# a = [randint(170, 220) for i in range(n)]
# print("ugiuduom:\n", a)

# for i in range(n - 1):
#     for j in range(n - 2, i - 1, -1):
#         if a[j + 1] < a[j]:
#             a[j], a[j + 1] = a[j + 1], a[j]

# print("surikiuotas ug:\n", a)

# maziausias = a[0]
# didziausias = a[-1]
# skirtumas = didziausias - maziausias

# print(f"zem zaidejas: {maziausias} cm")
# print(f"Auksciausias zaid: {didziausias} cm")
# print(f"skirtumas tarp ugio: {skirtumas} cm")
