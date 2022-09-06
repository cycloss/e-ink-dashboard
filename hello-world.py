#!/usr/bin/python3
# -*- coding:utf-8 -*-
import logging
import os
import time

from PIL import Image, ImageDraw, ImageFont

# requires the e-Paper repo to be in the directory and called ePaper (should be a submodule)
import ePaper.RaspberryPi_JetsonNano.python.lib.waveshare_epd.epd3in7 as epd3in7

FONT_DIR = "assets/fonts"


def main():

    logging.basicConfig(ormat='%(asctime)s [%(levelname)s] -  %(message)s',
                        level=logging.DEBUG,
                        datefmt='%H:%M:%S %d-%m-%Y')
    logging.info("Hello World Demo")

    try:
        # initialise
        screen = epd3in7.EPD()
        logging.info("init and Clear")
        screen.init(0)

        # clear with white
        screen.Clear(epd3in7.GRAY1, 0)

        font36 = ImageFont.truetype(f'{FONT_DIR}/Font.tcc', 36)

        logging.info("Drawing hello world")
        # create a new image with PIL, using L mode for 8-bit pixels (black and white)
        # https://pillow.readthedocs.io/en/stable/handbook/concepts.html#modes
        # background color is white
        canvas = Image.new('L', (screen.height, screen.width), epd3in7.GRAY1)

        # create a draw object to draw on the image
        draw = ImageDraw.Draw(canvas)

        # draw hello world
        draw.text((10, 0), 'hello world', font=font36, fill=0)

        # display it on the screen
        screen.display_4Gray(screen.getbuffer_4Gray(canvas))

        # wait 5 seconds
        time.sleep(5)

        # clear with white
        logging.info("Clear...")
        screen.init(0)
        screen.Clear(epd3in7.GRAY1, 0)

        # sleep display
        logging.info("Goto Sleep...")
        screen.sleep()

    except IOError as e:
        logging.info(e)

    except KeyboardInterrupt:
        logging.info("ctrl + c:")

        # clean up power on exit so uses 0 consumption
        epd3in7.epdconfig.module_exit()
        exit()


# only execute if this file is run directly
if __name__ == "__main__":
    main()
