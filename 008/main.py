import math

x=0.0
y=0.0

irany = str(input())
if irany == "stop":
    print(round(x,2))
    print(round(y,2))
    print(math.sqrt(pow((0-round(x,2)),2) + pow((0-round(y,2)),2)))
else:
    egyseg = float(input())
    while irany != 'stop':
        if irany == "forward":
            y += egyseg
        if irany == "backward":
            y -= egyseg
        if irany == "right":
            x += egyseg
        if irany == "left":
            x -= egyseg
        irany = str(input())
        if irany == "stop":
            break
        else:
            egyseg = float(input())
    print(round(x,2))
    print(round(y,2))
    print(round(math.sqrt(pow((0-round(x,2)),2) + pow((0-round(y,2)),2))),2)

    