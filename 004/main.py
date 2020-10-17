"""
Kerj be ket egesz szamot (feltetelezhetjuk, hogy pozitivak), es ird ki a legnagyobb kozos osztojukat, majd a legkisebb kozos tobbszorosuket.

pl:
Bemenet:
6
27
Kimenet:
3
54
"""

a = int(input())
b = int(input())
x = a
y = b
while a !=b:
    if a > b:
        a = a - b
    else:
        b = b - a

print(a)
print(int(x*y/a))

