from map_generation import *

if __name__ == "__main__":
    new_map = Map(10,10)
    print(F"Map generated = {new_map}")
    current_tile = Tile(start=True)
    pos = 0
    while(not (current_tile.type == TileType.END)):
        print(F"----\nPOSITION = {pos}")
        print(F"PLEASE INPUT DICE NUMBER")
        pos = int(input())
        current_tile = new_map.get_tile(pos)
        pos += current_tile.action()
        if (current_tile.type == TileType.SLIDER) or (current_tile.type == TileType.LADDER):
            print(F"PRESS ENTER")
            input()
    print(F"THANKS FOR PLAYING")

