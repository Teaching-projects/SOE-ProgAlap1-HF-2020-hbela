egyenleg = 0
penz = [] #Számla nélküli pénz
osszeg = 0
honap = 0

while honap != 12:
    penzmozgas = int(int(input()))
    penz.append(penzmozgas)
    egyenleg += penzmozgas
    if honap != 0:
        egyenleg -= 2000
    if egyenleg > 0:
        egyenleg += int(egyenleg * 0.05)
    else:
        egyenleg += int(egyenleg * 0.1)
    honap += 1

for i in range(len(penz)):
    osszeg += penz[i]

print(int(egyenleg))
print(osszeg)
    