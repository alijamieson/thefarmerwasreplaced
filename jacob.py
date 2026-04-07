b1 =Grounds.Soil
b2 =Grounds.Grassland
half = get_world_size()/2
def for_all(f):
    if get_pos_x()>=half and get_pos_y()>=half:
        if Grounds !=b1:
            till()
        a=Entities.Carrot
    elif get_pos_x()<=half and get_pos_y()>=half:
        if Grounds !=b1:
            till()
        a=Entities.Pumpkin
    elif get_pos_x()>=half and get_pos_y()<=half:
        if Grounds !=b2:
            till()
    elif get_pos_x()=<half and get_pos_y()=<half:
        if get_pos_x()%2=0 or get_pos_y()%2=0:
            a=Entities.Tree
        if get_pos_x()%2=1 or get_pos_y()%2=1:
            a=Entities.Bush
    def row():
        for _ in range(get_world_size()-1):
            plant(a)
            if can_harvest():
                f()
            move(East)
        f()
    for _ in range(get_world_size()):
        if not spawn_drone(row):
            row()
        move(North)

while True:
    for_all(harvest)
