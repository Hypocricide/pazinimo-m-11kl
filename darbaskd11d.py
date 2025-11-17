from random import *

n = int(input("Kiek zaideju komandoje? n = "))

a = [randint(170, 220) for i in range(n)]
print("ugiuduom:\n", a)

for i in range(n - 1):
    for j in range(n - 2, i - 1, -1):
        if a[j + 1] < a[j]:
            a[j], a[j + 1] = a[j + 1], a[j]

print("surikiuotas ug:\n", a)

maziausias = a[0]
didziausias = a[-1]
skirtumas = didziausias - maziausias

print(f"zem zaidejas: {maziausias} cm")
print(f"Auksciausias zaid: {didziausias} cm")
print(f"skirtumas tarp ugio: {skirtumas} cm")
