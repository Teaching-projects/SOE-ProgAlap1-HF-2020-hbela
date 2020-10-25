"""
Keregessunk be pozitiv egesz szamokat addig, amig 0-t nem kapunk.
Ezutan irjuk ki, hogy melyik szam hanyszor szerepelt, egeszen a legnagyobb kapott szamig.

Pleda bemenet:
--------------------------------------------
1
1
2
1
5
0
--------------------------------------------


Pelda kimenet:
--------------------------------------------
1: 3
2: 1
3: 0
4: 0
5: 1
--------------------------------------------

Feltetelezhetjuk, hogy legalabb egy nem 0 szamot fogunk kapni.

"""
def Max(list):
    max = 0
    for i in range(0, len(list)):
        if list[i] > max:
            max = list[i]
    return max

szamok = []
while True:
    szam = int(input())
    if szam == 0:
        break
    szamok.append(szam)
    
for i in range(1,Max(szamok)+1):
    print(str(i)+": "+str(szamok.count(i)))



