from SuperSmashDrunk import *
from card_pick import *

def main():
    """! Main program entry.

    TODO: Update this to be a pytest instance
    """
    new_map = Map(10,10)
    print(F"Map generated = {new_map}")
    current_tile = Tile(start=True)
    pos = 0
    blue_deck = load_deck("blue_cards.xml")
    while(not (current_tile.type == TileType.END)):
        print(F"----\nPOSITION = {pos}")
        print(F"PLEASE INPUT DICE NUMBER")
        pos = int(input())
        current_tile = new_map.get_tile(pos)
        pos += current_tile.action()["move"]
        if (current_tile.type == TileType.SLIDER) or (current_tile.type == TileType.LADDER):
            print(F"PRESS ENTER")
            input()
        if (current_tile.type == TileType.BLUE):
            card = random.choice(blue_deck)
            print(F"--> {card.description}")
    print(F"THANKS FOR PLAYING")


if __name__ == "__main__":
    main()
