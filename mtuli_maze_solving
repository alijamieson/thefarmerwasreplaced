# ---------------------------------------------------------
#  start
# ---------------------------------------------------------

from __builtins__ import *
import targets

clear()

while get_pos_x() != 0:
    move(West)
while get_pos_y() != 0:
    move(South)

# ---------------------------------------------------------
#  coordinates (make dynamic somehow)
# ---------------------------------------------------------
    
drone_start_positions = [
    (0, 0),    (12, 0),    (20, 0),    (28, 0),
    (0, 12),   (12, 12),   (20, 12),   (28, 12),
    (0, 20),   (12, 20),   (20, 20),   (28, 20),
    (0, 28),   (12, 28),   (20, 28),   (28, 28), (28, 28)
]

drones = []

drone_no = max_drones()

# ---------------------------------------------------------
#  macro code
# ---------------------------------------------------------

for drone_id in range(drone_no):
    def maze(d_id=drone_id):
        for i in range(8):
            if get_ground_type() != Grounds.Soil:
                till()
            else:
                continue
            plant(Entities.Bush)
            for j in range(3):
                do_a_flip()
            use_item(Items.Weird_Substance, 8)

            ALL_DIRECTIONS = [North, South, East, West]

            def opposite_direction(direction):
                if direction == North:
                    return South
                elif direction == East:
                    return West
                elif direction == South:
                    return North
                elif direction == West:
                    return East

            def explore_option(direction):
                if get_entity_type() == Entities.Treasure:
                    harvest()
                    return True
                pass

                if not move(direction):
                    return False
                
                for explore_direction in ALL_DIRECTIONS:
                    if opposite_direction(explore_direction) != direction:
                        if explore_option(explore_direction):
                            return True
                
                move(opposite_direction(direction))

            while True:
                for direction in ALL_DIRECTIONS:
                    if explore_option(direction):
                        continue
            # move(North)
        # move(East)

# ---------------------------------------------------------
#  spawn drones
# ---------------------------------------------------------

drones = []
for k in range(drone_no + 1):
    drone = spawn_drone(maze)
    
    posx, posy = drone_start_positions[k]
    
    while get_pos_x() != posx:
        move(East)
    
    while get_pos_y() != posy:
        move(North)

    drones.append(drone)
