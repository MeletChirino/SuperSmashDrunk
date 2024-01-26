from map_generation import *

if __name__ == "__main__":
    new_map = Map(10,10)
    print(F"Map generated = {new_map}")
    current_tile = Tile(start=True)
    pos = 0
    while(not (current_tile.type == TileType.END)):
        print(F"----\nPOSITION = {pos}")
        print(F"PLEASE INPUT DICE NUMBER")
        dice_number = int(input())
        pos += dice_number
        current_tile = new_map.get_tile(pos)
        print(F"MOVE = {current_tile.action()}")
        print(F"ACTION = {current_tile.type}")
        if (current_tile.type == TileType.SLIDER) or (current_tile.type == TileType.LADDER):
            print(F"Moving thru slider ({current_tile.move}), press enter")
            input()
        pos += current_tile.action()
    print(F"THANKS FOR PLAYING")

