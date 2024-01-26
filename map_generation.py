# This file holds map generation library
import random
from enum import Enum

class TileType(Enum):
    BLANK=0
    SLIDER=1
    LADDER=2
    BLUE=3
    RED=4
    SPICY=5
    START=6
    END=7

class Tile:
    def __init__(self, **kwargs):
        self.move = 0
        if kwargs.get("start"):
            self.type = TileType.START
            return
        elif kwargs.get("end"):
            self.type = TileType.END
            return
        
        # Pop START and END from tiletype
        tile_list = [e for e in TileType]
        idx = tile_list.index(TileType.START)
        tile_list.pop(idx)
        idx = tile_list.index(TileType.END)
        tile_list.pop(idx)
        self.type = random.choice(tile_list)
        # Setting move preset to fixed value
        if self.type == TileType.SLIDER:
            self.move -= random.randint(0, 10)
        elif self.type == TileType.LADDER:
            self.move += random.randint(0, 10)
        

    def action(self):
        # When tile is type SLIDER or LADDER return move member
        if self.type == TileType.LADDER:
            print(F"THIS IS A LADDER, MOVE FORWARD {self.move}")
            return self.move
        if self.type == TileType.SLIDER:
            print(F"THIS IS A SLIDER, MOVE BACKWARDS {-self.move}")
            return self.move
        if self.type == TileType.BLUE:
           print("BLUE TILE, SOMETHING GOOD THING HAPPENS") 
        if self.type == TileType.RED:
           print("RED TILE, SOMETHING BAD THING HAPPENS")
        if self.type == TileType.BLANK:
           print("BLANK TILE,NOTHING HAPPENS")
        if self.type == TileType.SPICY:
           print("SPICY TILE, SOMTHING WILL HAPPEN")
        # TODO: get card
        # When there is no moving action return 0
        return 0

    def __str__(self):
        return F"{self.type.name}"

class Map:
    def __init__(self, columns, rows):
        self.rows = rows
        self.columns = columns
        # Generate map
        self.generate()
        # Full number of tiles
        self.full_tiles = rows * columns

    def generate(self):
        self.map = []
        self.action = []
        for i in range(self.rows):
            row = []
            for j in range(self.columns):
                row.append(Tile())
            self.map.append(row)
        self.map[0][0] = Tile(start=True)
        self.map[self.rows-1][self.columns-1] = Tile(end=True)
        return self.map

    def show(self):
        string = ""
        for i in range(self.rows):
            string += "["
            for j in range(self.columns):
                string += str(self.map[i][j]) + ", "
            string += "]\n"
        return string

    def get_tile(self, index):
        if index >= (self.rows * self.columns):
            # TODO: When index is higher than full number go backwards
            #raise(Exception("Wrong index"))
            left = index - self.full_tiles
            index = self.full_tiles - left
        i = index // self.rows
        j = (index % self.columns)
        # TODO: Remove following print
        #print(F"tile[{i}][{j}]")
        return self.map[i][j]
    
    def __str__(self):
        return self.show()
        


if __name__ == "__main__":
    COLUMNS = 9
    ROWS = 10
    new_map = Map(ROWS, COLUMNS)
    print(F"new map = \n{new_map}")
    print(F"{new_map.get_tile_type(0)}")
    print(F"{new_map.get_tile_type(7)}")
    print(F"{new_map.get_tile_type(24)}")
    try:
        print(F"{new_map.get_tile_type(78)}")
    except Exception as e:
        print(F"Error: {e}")
