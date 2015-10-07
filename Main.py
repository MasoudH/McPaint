from pygame import *
from math import *

screen = display.set_mode((1200, 675))
background = image.load("Pictures/Background.jpg")
background = transform.scale(background, (1200, 675))
screen.blit(background, (0, 0))

display.set_caption("McPaint Pro by Atilla Saadat and Masoud Harati for McHacks 2015")

canvas = draw.rect(screen, (255, 255, 255), (25, 25, 800, 625))

draw.rect(screen, (129, 9, 9), (845, 25, 340, 269)) # Rect around Color Pallete
draw.rect(screen, (129, 9, 9), (845, 314, 340, 336)) # Rect around tools

color_rect = Rect(865, 45, 300, 194)
color_pallete = image.load("Pictures/Color.jpg")
color_pallete = transform.scale(color_pallete, (300, 194))
screen.blit(color_pallete, (865, 45))


icon = image.load("Pictures/Icon.png")
display.set_icon(icon)


tool = "Marker"
#-----Tools------
marker_rect = draw.rect(screen, (50, 50, 50), (865, 334, 140, 140))
marker = image.load("Pictures/Tools/Marker.png")
markerSelected = image.load("Pictures/Tools/Marker Selected.png")

eraser_rect = draw.rect(screen, (50, 50, 50), (865, 489, 140, 140))
eraser = image.load("Pictures/Tools/Eraser.png")
eraserSelected = image.load("Pictures/Tools/Eraser Selected.png")

spray_rect = draw.rect(screen, (50, 50, 50), (1025, 334, 140, 140))
spray = image.load("Pictures/Tools/Spray.png")
spraySelected = image.load("Pictures/Tools/Spray Selected.png")

flood_rect = draw.rect(screen, (50, 50, 50), (1025, 489, 140, 140))
flood = image.load("Pictures/Tools/Flood.png")
floodSelected = image.load("Pictures/Tools/Flood Selected.png")
#----------------

color = (0, 0, 0, 255)
draw.rect(screen, color, (865, 249, 300, 25))

mx, my = 0, 0

running = True
while running:
    for e in event.get():
    	if e.type == QUIT:
            running = False

    if tool == "Marker":
    	draw.rect(screen, (50, 50, 50), marker_rect)
    	screen.blit(markerSelected, (880, 350))
    else:
    	draw.rect(screen, (50, 50, 50), marker_rect)
    	screen.blit(marker, (880, 350))

    if tool == "Eraser":
    	draw.rect(screen, (50, 50, 50), eraser_rect)
    	screen.blit(eraserSelected, (880, 505))
    else:
    	draw.rect(screen, (50, 50, 50), eraser_rect)
    	screen.blit(eraser, (880, 505))

    if tool == "Spray":
    	draw.rect(screen, (50, 50, 50), spray_rect)
    	screen.blit(spraySelected, (1040, 350))
    else:
    	draw.rect(screen, (50, 50, 50), spray_rect)
    	screen.blit(spray, (1040, 350))

    if tool == "Bucket":
    	draw.rect(screen, (50, 50, 50), flood_rect)
    	screen.blit(floodSelected, (1040, 505))
    else:
    	draw.rect(screen, (50, 50, 50), flood_rect)
    	screen.blit(flood, (1040, 505))


    display.flip()
quit()