#!/usr/bin/python3
"""
Expanding Square 2 - Pibow Candy

Creates a square that increases in size. It does this with each of the
colors.

....................

Author: Paul Ryan

This program was written on a Raspberry Pi using the Geany IDE.
"""
########################################################################
#                          Import modules                              #
########################################################################

from time import sleep
import unicornhat
from bfp_unicornhat import print_header
from bfp_unicornhat import stop

########################################################################
#                           Variables                                  #
########################################################################

from bfp_unicornhat import R
from bfp_unicornhat import O
from bfp_unicornhat import Y
from bfp_unicornhat import G
from bfp_unicornhat import B
from bfp_unicornhat import I
from bfp_unicornhat import V
from bfp_unicornhat import W
OFF = (0, 0, 0)

########################################################################
#                            Functions                                 #
########################################################################


def expanding_square_2():
    """
    Creates a square that increases in size. It does this with each of
    the colors.
    """

    sleep_speed = 0.1
    colors = [R, O, Y, G, B, I, V, W]

    for color in colors:
        for _ in range(0, 5):

            unicornhat.set_pixel(3, 3, color)
            unicornhat.set_pixel(3, 4, color)
            unicornhat.set_pixel(4, 3, color)
            unicornhat.set_pixel(4, 4, color)

            unicornhat.show()
            sleep(sleep_speed)

            unicornhat.set_pixel(2, 2, color)
            unicornhat.set_pixel(3, 2, color)
            unicornhat.set_pixel(4, 2, color)
            unicornhat.set_pixel(5, 2, color)

            unicornhat.set_pixel(2, 3, color)
            unicornhat.set_pixel(2, 4, color)
            unicornhat.set_pixel(2, 5, color)

            unicornhat.set_pixel(3, 5, color)
            unicornhat.set_pixel(4, 5, color)
            unicornhat.set_pixel(5, 5, color)

            unicornhat.set_pixel(5, 3, color)
            unicornhat.set_pixel(5, 4, color)
            unicornhat.set_pixel(5, 5, color)

            unicornhat.show()
            sleep(sleep_speed)

            unicornhat.set_pixel(1, 1, color)
            unicornhat.set_pixel(2, 1, color)
            unicornhat.set_pixel(3, 1, color)
            unicornhat.set_pixel(4, 1, color)
            unicornhat.set_pixel(5, 1, color)
            unicornhat.set_pixel(6, 1, color)

            unicornhat.set_pixel(1, 2, color)
            unicornhat.set_pixel(1, 3, color)
            unicornhat.set_pixel(1, 4, color)
            unicornhat.set_pixel(1, 5, color)
            unicornhat.set_pixel(1, 6, color)

            unicornhat.set_pixel(2, 6, color)
            unicornhat.set_pixel(3, 6, color)
            unicornhat.set_pixel(4, 6, color)
            unicornhat.set_pixel(5, 6, color)
            unicornhat.set_pixel(6, 6, color)

            unicornhat.set_pixel(6, 2, color)
            unicornhat.set_pixel(6, 3, color)
            unicornhat.set_pixel(6, 4, color)
            unicornhat.set_pixel(6, 5, color)

            unicornhat.show()
            sleep(sleep_speed)

            unicornhat.set_pixel(0, 0, color)
            unicornhat.set_pixel(1, 0, color)
            unicornhat.set_pixel(2, 0, color)
            unicornhat.set_pixel(3, 0, color)
            unicornhat.set_pixel(4, 0, color)
            unicornhat.set_pixel(5, 0, color)
            unicornhat.set_pixel(6, 0, color)
            unicornhat.set_pixel(7, 0, color)

            unicornhat.set_pixel(0, 1, color)
            unicornhat.set_pixel(0, 2, color)
            unicornhat.set_pixel(0, 3, color)
            unicornhat.set_pixel(0, 4, color)
            unicornhat.set_pixel(0, 5, color)
            unicornhat.set_pixel(0, 6, color)
            unicornhat.set_pixel(0, 7, color)

            unicornhat.set_pixel(1, 7, color)
            unicornhat.set_pixel(2, 7, color)
            unicornhat.set_pixel(3, 7, color)
            unicornhat.set_pixel(4, 7, color)
            unicornhat.set_pixel(5, 7, color)
            unicornhat.set_pixel(6, 7, color)
            unicornhat.set_pixel(7, 7, color)

            unicornhat.set_pixel(7, 1, color)
            unicornhat.set_pixel(7, 2, color)
            unicornhat.set_pixel(7, 3, color)
            unicornhat.set_pixel(7, 4, color)
            unicornhat.set_pixel(7, 5, color)
            unicornhat.set_pixel(7, 6, color)

            unicornhat.show()
            sleep(sleep_speed)

            square_off()


def square_off():
    """
    Creates a vortex pattern with each of the colors.
    """

    sleep_speed = 0.1

    unicornhat.set_pixel(3, 3, OFF)
    unicornhat.set_pixel(3, 4, OFF)
    unicornhat.set_pixel(4, 3, OFF)
    unicornhat.set_pixel(4, 4, OFF)

    unicornhat.show()
    sleep(sleep_speed)

    unicornhat.set_pixel(2, 2, OFF)
    unicornhat.set_pixel(3, 2, OFF)
    unicornhat.set_pixel(4, 2, OFF)
    unicornhat.set_pixel(5, 2, OFF)

    unicornhat.set_pixel(2, 3, OFF)
    unicornhat.set_pixel(2, 4, OFF)
    unicornhat.set_pixel(2, 5, OFF)

    unicornhat.set_pixel(3, 5, OFF)
    unicornhat.set_pixel(4, 5, OFF)
    unicornhat.set_pixel(5, 5, OFF)

    unicornhat.set_pixel(5, 3, OFF)
    unicornhat.set_pixel(5, 4, OFF)
    unicornhat.set_pixel(5, 5, OFF)

    unicornhat.show()
    sleep(sleep_speed)

    unicornhat.set_pixel(1, 1, OFF)
    unicornhat.set_pixel(2, 1, OFF)
    unicornhat.set_pixel(3, 1, OFF)
    unicornhat.set_pixel(4, 1, OFF)
    unicornhat.set_pixel(5, 1, OFF)
    unicornhat.set_pixel(6, 1, OFF)

    unicornhat.set_pixel(1, 2, OFF)
    unicornhat.set_pixel(1, 3, OFF)
    unicornhat.set_pixel(1, 4, OFF)
    unicornhat.set_pixel(1, 5, OFF)
    unicornhat.set_pixel(1, 6, OFF)

    unicornhat.set_pixel(2, 6, OFF)
    unicornhat.set_pixel(3, 6, OFF)
    unicornhat.set_pixel(4, 6, OFF)
    unicornhat.set_pixel(5, 6, OFF)
    unicornhat.set_pixel(6, 6, OFF)

    unicornhat.set_pixel(6, 2, OFF)
    unicornhat.set_pixel(6, 3, OFF)
    unicornhat.set_pixel(6, 4, OFF)
    unicornhat.set_pixel(6, 5, OFF)

    unicornhat.show()
    sleep(sleep_speed)

    unicornhat.set_pixel(0, 0, OFF)
    unicornhat.set_pixel(1, 0, OFF)
    unicornhat.set_pixel(2, 0, OFF)
    unicornhat.set_pixel(3, 0, OFF)
    unicornhat.set_pixel(4, 0, OFF)
    unicornhat.set_pixel(5, 0, OFF)
    unicornhat.set_pixel(6, 0, OFF)
    unicornhat.set_pixel(7, 0, OFF)

    unicornhat.set_pixel(0, 1, OFF)
    unicornhat.set_pixel(0, 2, OFF)
    unicornhat.set_pixel(0, 3, OFF)
    unicornhat.set_pixel(0, 4, OFF)
    unicornhat.set_pixel(0, 5, OFF)
    unicornhat.set_pixel(0, 6, OFF)
    unicornhat.set_pixel(0, 7, OFF)

    unicornhat.set_pixel(1, 7, OFF)
    unicornhat.set_pixel(2, 7, OFF)
    unicornhat.set_pixel(3, 7, OFF)
    unicornhat.set_pixel(4, 7, OFF)
    unicornhat.set_pixel(5, 7, OFF)
    unicornhat.set_pixel(6, 7, OFF)
    unicornhat.set_pixel(7, 7, OFF)

    unicornhat.set_pixel(7, 1, OFF)
    unicornhat.set_pixel(7, 2, OFF)
    unicornhat.set_pixel(7, 3, OFF)
    unicornhat.set_pixel(7, 4, OFF)
    unicornhat.set_pixel(7, 5, OFF)
    unicornhat.set_pixel(7, 6, OFF)

    unicornhat.show()
    sleep(sleep_speed)


if __name__ == '__main__':
    try:
        # STEP01: Print header
        print_header()
        # STEP02: Print instructions in white text
        print("\033[1;37;40mPress Ctrl-C to stop the program.")
        # STEP03:
        expanding_square_2()
        # STEP04: Exit the program.
        stop()
    except KeyboardInterrupt:
        stop()
