from api import API
### TODO: Enter your API key
API_KEY = '4631e00c-c926-40a1-aea2-dabe47e3693e'
_api = API(API_KEY)
#!/usr/bin/env
#-*- coding: utf-8 -*-

import math


def solve(game):
	
	# --- Available commands ---
	# TRAVEL [NORTH|SOUTH|WEST|EAST]
	# [BUS|TRAIN|FLIGHT] {CityName}
	# SET_PRIMARY_TRANSPORTATION [CAR|BIKE]
	 
	
	# TODO: Implement your solution
	
	# Example solution
	solution = list();
	x = game.start.x;
	y = game.start.y;
	x_malm = 296;
	y_malm = 423;
	x_upp = 349;
	y_upp = 333;

	citylist = [];
	for city in game.cities:
		x_city = city.x;
		y_city = city.y;
		distance = math.sqrt(math.pow(x_city-game.start.x,2) + math.pow(y_city-game.start.y,2));
		citylist.append((city.x,city.y,distance));

	citylist.sort(key=lambda tup: tup[2])  # sorts in place

	print citylist
	
	solution.append('SET_PRIMARY_TRANSPORTATION BIKE');
	
	for city in citylist[:39]:
		if city[1] > game.start.y and city[1]<game.end.y:
			if x > city[0]:
				while(x>city[0]):
					x-=1;
					solution.append("TRAVEL WEST");
			else:
				while(x<city[0]):
					x+=1;
					solution.append("TRAVEL EAST");
			if y > city[1]:
				while(y>city[1]):
					y-=1;
					solution.append("TRAVEL NORTH");
			else:
				while(y<city[1]):
					y+=1;
					solution.append("TRAVEL SOUTH");
			
	
##	while (x>x_malm):
##		x-=1;
##		solution.append("TRAVEL WEST");
##	while (y<y_malm):
##		y+=1;
##		solution.append("TRAVEL SOUTH");
	while (x < game.end.x):
	      x+=1;
	      solution.append("TRAVEL EAST");
	while (y < game.end.y):
	      y+=1;
	      solution.append("TRAVEL SOUTH");
	
	return solution;


def main():
	_api.initGame()
	game = _api.getMyLastGame()
    #Or get by gameId:
	#game = _api.getGame();
	solution = solve(game)
	_api.submitSolution(solution, game.id)

main()
