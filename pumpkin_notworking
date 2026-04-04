clear()
for _ in range(get_world_size()):
    for _ in range(get_world_size()):
        till()
        plant(Entities.Pumpkin)
        move(North)
    move(East)
def harvest_column():
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
while True:
    if spawn_drone(harvest_column):
        move(East)
