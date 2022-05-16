graphics_strings = {
    "wall": "\033[100m  ",                  #gray
    "player": "\033[44m  ",                 #blue
    "friend": "\033[42m  ",                 #green
    "enemy": "\033[41m  ",                  #red
    "collectable": "\033[103m  ",           #yellow
    "door": "\033[107m  ",                  #white (placeholder, but might stay if no better color is chosen)
    "teleport": "\033[0m  "                 #no color
}

def render_map(map):           #renders the map
    map_size = map["size"]
    for y in range(map_size[1]):
        for x in range(map_size[0]):
            coords = (x, y)
            if coords in map.keys():
                print(graphics_strings[map[coords]], end="")
            else:
                if 0 in coords or coords[0] == map_size[0]-1 or coords[1] == map_size[1]-1:
                    print(graphics_strings["wall"], end="")
                else:
                    print("\033[0m  ", end="")
        print("\033[0m")
