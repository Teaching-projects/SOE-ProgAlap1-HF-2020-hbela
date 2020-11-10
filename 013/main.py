"""
Tovabbfejlesztjuk az elozo dolgot. 

Most atirjuk a kiirato fuggvenyt ugy, hogy kap egy dictionary-t is, amiben benne van a jatekos karakterunk a kovetkezo modon:

character = {
    "name" : "Dark Wanderer",
    "position" : {
        "x" : 4 ,
        "y" : 2 
    }
}


Az eredmenye a kiiratasnak a korabbi peldaterkepen igy nezne ki:

████████████████████████████
██░░░░░░░░░░░░██████████████
██░░░░░░🧙‍░░░░██████░░░░░░██
██░░░░██████████████░░██░░██
██░░░░██░░░░░░░░░░██░░██░░██
██░░░░░░░░░░░░██░░██░░██░░██
██████████░░░░██░░██░░██░░██
██░░░░░░░░░░░░██░░░░░░██░░░░
████████████████████████████

Ket dolog valtozott meg:
 - Az eddigi █ es ░ karaktereket mindig duplan rajzoljuk ki, hogy korulbelul negyzet alaku legyen egy mezo.
 - A karakterunk helyere 🧙‍-t irunk ki.



"""

def initialize_map (width, height):
    # ide masold be a helyes megoldasodat a multkorirol
    terkep = [["██",]*width]
    for i in range(height-2):
        sor = ["██"]
        for k in range(width-2):
            sor.append("░░")
        sor.append("██")
        terkep.append(sor)
    terkep.append(["██"] * width)

    return terkep

def pretty_map_print(map, character):
    # Ide masold be a multkorit, a fenti modositasokkal. 
    # Ha a karakter pozicioja a palyan kivul lenne, egyszeruen ne jelenjen meg
    x = character["position"]["x"]
    y = character["position"]["y"]
    
    if (x < len(map[1])-1 and x >= 0) and (y < len(map) - 1 and y >= 0):
        map[y][x] = "🧙"

    for i in range(len(map)):
        for k in range(len(map[i])):
            print(map[i][k],end="")
        print()

###############################################################
###############################################################
####### Ez alatt nem modosithatsz #############################
###############################################################
###############################################################


def initialize_character():
    x=int(input())
    y=int(input())
    return {"name": "Placeholder name", "position" : {"x":x,"y":y} }

width=int(input())
height=int(input())
map=initialize_map(width,height)

character=initialize_character()

pretty_map_print(map,character)
