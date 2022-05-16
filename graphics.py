graphics_strings = {
    "blank": "\033[0m  ",                   #no color
    "wall": "\033[100m  ",                  #gray
    "player": "\033[44m  ",                 #blue
    "friend": "\033[42m  ",                 #green
    "enemy": "\033[41m  ",                  #red
    "collectable": "\033[103m  ",           #yellow
    "door": "\033[107m  ",                  #white (placeholder, but might stay if no better color is chosen)
    "teleport": "\033[0m  "                 #no color
}

def render_map(map):           #renders the map
    for i in map:
        for j in i:
            if j[0] == "blank":
                print(graphics_strings[j[1]], end="")
            else:
                print(graphics_strings[j[0]], end="")
        print("\033[0m")