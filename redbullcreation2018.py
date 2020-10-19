'''Testing printer formatting'''

from escpos.printer import Dummy
from escpos import config
c = config.Config()
printer = c.printer()

# title
title_size = [1, 4]
printer.line_spacing(spacing=64)
printer.set(align="center", width=title_size[0], height=title_size[1], font='a' )
printer.image("/home/pi/redbull/img/CPS_logo.png", impl='bitImageColumn')
printer.text("Collated Paper\nServices\n")

# normal text
text_size = [2, 1]

printer.line_spacing(spacing = 0)
printer.set(align='left', width=text_size[0], height=text_size[1], font='b')
printer.text("Here is a copy of your document.*"
printer.set(align="center")
printer.image("/home/pi/redbull/img/landscape_IMG_20180630_214502_974.jpg, impl='bitImageColumn')

printer.text("* (Document may not be actually yours. The interdimensional government of Haap is beta testing the concept of time and is not liable for any documents that may have been misplaced within the temporal vortex.")

#barcode
barcode_size = [3, 2]
printer.line_spacing(spacing = 0)
printer.set(align="center", width=barcode_size[0], height=barcode_size[1], font='b')
printer.barcode("the_giant", "CODE128", function_type="B")

#too tall
tall_size = [2, 3]
printer.line_spacing(spacing = 16)
printer.set(align="center", width=tall_size[0], height=tall_size[1], font='b')
