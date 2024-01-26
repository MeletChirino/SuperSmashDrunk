#!/usr/bin/env python3
"""! @brief SuperSmashDrunk main library"""
##
# @mainpage SuperSmashDrunk project
#
# @section description_main Description
# This is a game to drink with friends. Goal is to pass
# an unkown labirynth using one or two dices. On every
# Tile could be consequences good for you or four your
# friends. Happy drink.
# @section notes_main Notes
# - First version of the game is meant to be played from
# terminal. Future versions will support django or pygame
# integration.
# Copyright (c) 2024 Melet Chirino. All rights reserved.

##
# @file SuperSmashDrunk.py
#
# @brief This file holds main library for playing the game.
#
# @section description_SuperSmashDrunk_main Description
# This file holds Tile and Map class.
#
# @section libraries_main Libraries/Modules
# - random: used for getting random choices
# - enum: used for enumerate TileType class
# - cowsay: This shows messages on cow voice
#
# @section notes_SuperSmashDrunk_notes Notes
# - Prealfa version holds very basic things
# @section todo_SuperSmashDrunk_main TODO
# - Implement CowSay library
# - Add Cards on xml format
#
# @section author_SuperSmashDrunk_main Author(s)
# - Created by Melet Chirino on 25/01/2024
# - Cards added by (nobody yet)
# Copyright (c) 2024 Melet Chirino. All rights reserved.

# Imports
import random
from enum import Enum
import xml.etree.ElementTree as ET

# Type of tiles used on game
class TileType(Enum):
    """! TileType enumerated class

    Enumeration of all kind of possible tile type.
    """
    BLANK=0
    SLIDER=1
    LADDER=2
    BLUE=3
    RED=4
    SPICY=5
    START=6
    END=7

# Class that defines a Tile and its actions
class Tile:
    """! Tile base class

    Defines tile class where players will step on. 
    """
    def __init__(self, **kwargs):
        """! Tile base class initializer.

        @param start  If you add 'start' keyword argument this tile will be set as START type.

        @param end  If you add 'end' keyword argument this tile will be set as END type.

        @return An instance of Tile class initialized with random type unless 'start' or 'end' keywords are used.
        """

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
        """! This holds action of tile depending on its type.

        @return  A dictionary with 'message' and 'move' keywords.
        'message' should be printed on game and 'move' will be used to update
        player's position.
        """
        # This method returns a message and movement of an actions
        message = ''
        if self.type == TileType.LADDER:
            message = F"THIS IS A LADDER, MOVE FORWARD {self.move}"
        if self.type == TileType.SLIDER:
            message = F"THIS IS A SLIDER, MOVE BACKWARDS {-self.move}"
        if self.type == TileType.BLUE:
            message = "BLUE TILE, SOMETHING GOOD THING HAPPENS"
        if self.type == TileType.RED:
            message = "RED TILE, SOMETHING BAD THING HAPPENS"
        if self.type == TileType.BLANK:
            message = "BLANK TILE NOTHING HAPPENS"
        if self.type == TileType.SPICY:
            message = "SPICY TILE, SOMETHING WILL HAPPEN"
        action_dict = {
                "move": self.move,
                "message": message
                }
        return action_dict

    def __str__(self):
        """! Retrieves the Tile's description.

        @return  The tile type name
        """
        return F"{self.type.name}"

class Map:
    """! The Map class.

    An squared array of Tiles, game program will interact with
    map directly.
    """
    def __init__(self, columns, rows):
        """! Map class initalizer.

        @param columns  Number of columns of the map.
        @param rows  Number of rows of the map.

        @return  An instance of the Map class.
        """
        self.rows = rows
        self.columns = columns
        # Generate map
        self.generate()
        # Full number of tiles
        self.full_tiles = rows * columns

    def generate(self):
        """! Generates and array of Tiles.

        @return  An array of tiles called map, this is also a member.
        """
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

    def get_tile(self, index):
        """! Gets an specific Tile depending on index and not on coordinates.

        @return  Specific Tile
        """
        if index >= (self.rows * self.columns):
            # TODO: When index is higher than full number go backwards
            left = index - self.full_tiles
            index = self.full_tiles - left
        i = index // self.rows
        j = (index % self.columns)
        return self.map[i][j]

    def __str__(self):
        """! Retrieves Map's description."""
        string = ""
        for i in range(self.rows):
            string += "["
            for j in range(self.columns):
                string += str(self.map[i][j]) + ", "
            string += "]\n"
        return string

# Global constants
ID = 0
NAME = 1
DESCRIPTION = 2

class Card:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    def __str__(self):
        return self.name

def load_deck(file):
    deck = []
    root = ET.parse(file)
    root_node = root.getroot()
    for card in root_node:
        new_card = Card(
                card[NAME].text,
                card[DESCRIPTION].text
                )
        deck.append(new_card)
    return deck

def main():
    """! Main program entry.

    Used only for testing purposed and it is not supposed to be used
    else where.
    """
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


if __name__ == "__main__":
    main()
