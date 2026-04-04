clear()
while True:
    for i in range(get_world_size()):
        for i in range(get_world_size()):
            if get_ground_type() != Grounds.Soil:
                till()
                if can_harvest(): 
                    harvest()
            plant(Entities.Pumpkin)
            move(North)
        move(East)

    while get_pos_x() != 0 :
        move(East)

    while get_pos_y() != 0:
        move(South)

    pump_bot_l = measure()
    print(pump_bot_l)

    while get_pos_x() != get_world_size() -1:
        move(West)

    while get_pos_y() != get_world_size() -1:
        move(North)

    pump_top_r = measure()
    print(pump_top_r)

    if pump_bot_l == pump_top_r:
        harvest()
    else:
        continue
        
