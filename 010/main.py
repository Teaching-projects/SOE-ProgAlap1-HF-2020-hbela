honap = 0
total = 0
perc = []
sms = []
szamla=[]

while honap != 12:
    perc.append(int(input()))
    sms.append(int(input()))
    honap += 1
cshavi = int(input())
csperc = int(input())
csSMS = int(input())

for i in range(len(perc)):
    if perc[i]*csperc + sms[i]*csSMS < cshavi: szamla.append(cshavi)
    else: szamla.append(perc[i]*csperc + sms[i]*csSMS)
for i in range(len(szamla)):
    total += szamla[i]

print(szamla)
print(total)


