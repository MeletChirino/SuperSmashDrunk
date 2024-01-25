# This file holds map generation library
import random

class Tile:
    # TODO: Make this a kind of enumeration class
    # so that you have list and stuff automatically
    BLANK=0
    SLIDER=1
    LADDER=2
    BLUE=3
    RED=4
    SPICY=5
    LIST=[0, 1, 2, 3, 4, 5]

class Map:
    def __init__(self, columns, rows):
        self.rows = rows
        self.columns = columns
        # Generate map
        self.generate()

    def generate(self):
        self.map = []
        row = []
        # List with tile types
        # TODO: next should be an enumration list from above
        tile_type = [
                Tile.BLANK,
                Tile.SLIDER,
                Tile.LADDER
                ]
        for i in range(self.rows):
            row = []
            for j in range(self.columns):
                row.append(random.choice(tile_type))
            self.map.append(row)
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
            raise("Wrong index")
        i = index // self.rows
        j = (index % self.columns)
        # TODO: Remove following print
        print(F"tile[{i}][{j}]")
        return self.map[i][j]
    
    def __str__(self):
        return self.show()
        


if __name__ == "__main__":
    new_map = Map(5, 5)
    print(F"new map = \n{new_map}")
    print(F"{new_map.get_tile_type(0)}")
    print(F"{new_map.get_tile_type(7)}")
    print(F"{new_map.get_tile_type(24)}")
    try:
        print(F"{new_map.get_tile_type(25)}")
    except Exception as e:
        print(F"Error: {e}")
