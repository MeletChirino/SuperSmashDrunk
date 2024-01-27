from SuperSmashDrunk import *
import cowsay

def main():
    """! Main program entry.

    TODO: Update this to be a pytest instance
    """
    # Generate map
    new_map = Map(10,10)
    print(F"Map generated = \n{new_map}")
    # Initialize variables
    current_tile = Tile(start=True)
    pos = 0
    # Load decks
    blue_deck = load_deck("blue_cards.xml")
    red_deck = load_deck("red_cards.xml")
    spicy_deck = load_deck("spicy_cards.xml")
    while(not (current_tile.type == TileType.END)):
        card = Card('','Nothing too bad happened')
        print(F"----\nPOSITION = {pos}")
        print(F"PLEASE INPUT DICE NUMBER")
        # Get position
        pos = int(input())
        current_tile = new_map.get_tile(pos)
        # Update position depending on tile
        pos += current_tile.action()["move"]
        # Show actions when tile is type SLIDER or LADDER
        if (current_tile.type == TileType.SLIDER) or (current_tile.type == TileType.LADDER):
            print(F"PRESS ENTER")
            card.description = F"Move {current_tile.action()['move']}"
            input()
        # Pick card when is BLUE tile
        if (current_tile.type == TileType.BLUE):
            card = random.choice(blue_deck)
        if (current_tile.type == TileType.RED):
            card = random.choice(red_deck)
        if (current_tile.type == TileType.SPICY):
            card = random.choice(spicy_deck)
        cowsay.stimpy(card.description)
    print(F"THANKS FOR PLAYING")


if __name__ == "__main__":
    main()
