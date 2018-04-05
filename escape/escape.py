"""Cheers! A simple text-based, escape-the-room-type, game. Have fun!"""

import items as it
import player as p

player = p.Player()


def word_wrap(target, numb=1):
    """Wrap text headings"""
    wrap = "=" * (len(target) * numb)

    print(wrap)
    print(target)
    print(wrap)


def title():
    """Introduce storyline"""
    intro = "\t**ThE CrAvInG**"
    grumble = "\n\t**grrRRrRrrRUmmMmMMble**\n"

    word_wrap(intro, 2)
    print("\t  ==Thus Far==\n\n")
    print("\t**A bell sounds**")
    print("You awaken unto an empty white room..")
    print("..with no idea where you are or how you arrived.")
    print("You look around, searching for any clue of what's going on..")
    print("..but to no avail.")
    print("You look down and check yourself,")
    print("thankful that you're still, at least, in posession of your pants.")
    print(grumble)
    print("Startled by the sudden noise, you scramble guardedly to your feet.")
    print(grumble)
    print("""That sound...that feeling...you recognize it..
    ..A cold realization sets in.""")
    print("\n\t.. ... ... ... ... ... ... ..\n")
    print("You've developed a serious craving for twizzlers.\n")
    word_wrap("Search your surroundings for a way to escape!")


def main():
    """Run game"""
    while True:
        player.stats()
        player.action()
        if it.WHITE_ORB in it.PACK.pocket:
            p.ROOMS[1]["orb"] = it.BLACK_ORB
        if it.TWIZZLERS in it.PACK.pocket:
            print("You sigh, blissfully, as you unwrap the pack of twizzlers.")
            print("Game Over!")
            break


# Start!!
title()
player.menu()
main()
