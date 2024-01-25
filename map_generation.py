# This file holds map generation library
import random
from enum import Enum

class Tile(Enum):
    BLANK=0
    SLIDER=1
    LADDER=2
    BLUE=3
    RED=4
    SPICY=5
    START=6
    END=7

class Map:
    def __init__(self, columns, rows):
        self.rows = rows
        self.columns = columns
        # Generate map
        self.generate()

    def generate(self):
        self.map = []
        row = []
        for i in range(self.rows):
            row = []
            for j in range(self.columns):
                # Remove START and END elements
                tile_list = [e for e in Tile]
                idx = tile_list.index(Tile.START)
                tile_list.pop(idx)
                idx = tile_list.index(Tile.END)
                tile_list.pop(idx)
                row.append(random.choice(tile_list))
            self.map.append(row)
        self.map[0][0] = Tile.START
        self.map[self.rows-1][self.columns-1] = Tile.END
        return self.map

    def show(self):
        string = ""
        for i in range(self.rows):
            string += "["
            for j in range(self.columns):
                string += str(self.map[i][j]) + ", "
            string += "]\n"
        return string

    def get_tile_type(self, index):
        if index >= (self.rows * self.columns):
            # TODO: create custom exception class
            raise(Exception("Wrong index"))
        i = index // self.rows
        j = (index % self.columns)
        # TODO: Remove following print
        print(F"tile[{i}][{j}]")
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
