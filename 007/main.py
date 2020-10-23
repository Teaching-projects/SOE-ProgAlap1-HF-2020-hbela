egyenleg = 0
nincs_szamla = 0
honap = 0

while honap != 3:
    penzmozgas = int(int(input()))
    nincs_szamla += penzmozgas
    egyenleg += penzmozgas
    if honap != 0:
        egyenleg -= 2000
    if egyenleg > 0:
        egyenleg += int(egyenleg * 0.05)
    else:
        egyenleg += int(egyenleg * 0.1)
    honap += 1
    
print(int(egyenleg))
print(nincs_szamla)
    