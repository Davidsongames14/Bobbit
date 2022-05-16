map_test = [[["blank","wall"], ["blank","wall"], ["blank", "wall"], ["blank", "wall"]],             
    [["blank", "wall"], ["player", "blank"], ["blank", "blank"], ["blank", "wall"]], 
    [["blank", "wall"], ["blank", "blank"], ["blank", "blank"], ["blank", "wall"]],
    [["blank", "wall"], ["blank", "blank"], ["blank", "blank"], ["blank", "wall"]],
    [["blank", "wall"], ["blank", "wall"], ["blank", "wall"], ["blank", "wall"]]]

map_test = {
    "size": (4, 5);
    (0, 0): "wall"; (0, 1): "wall"; (0, 2): "wall"; (0, 3): "wall"; 
    (1, 0): "wall";                                 (1, 3): "wall";
    (2, 0): "wall"; (2, 1): "player";               (2, 3): "wall";
    (3, 0): "wall";                                 (3, 3): "wall";
    (4, 0): "wall"; (4, 1): "wall"; (4, 2): "wall"; (4, 3): "wall"; 
}
