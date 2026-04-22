# to show to BitSculpt, by Jacob

a=1
def ifharvest():
	global a
	while not can_harvest():
		move(North)
		if get_pos_y()==31:
			move(East)
		else:
			break
			a=0
	if a!=0:
		harvest()
		a=1
def harvest_plant(plant1):
	plant(plant1)
	ifharvest()
def forever_harvest_plant(plant1,plant2,goal,list_unlock0):
	while True:
		harvest_plant(plant1)
		if num_items(plant2)==goal:
			for i in range(32):
				unlock0=list_unlock0[i]
				unlock(unlock0)
			break
		move(North)
		if get_pos_y()==31:
			move(East)
def Cactus():
	forever_harvest_plant(Entities.Cactus,Items.Cactus,15600000,Unlocks.Mazes)
while True:
	if spawn_drone(Cactus):
		pass
	if get_pos_y()==31:
		move(East)
	ifharvest()
