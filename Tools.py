def marker(tool, screen, canvas, mpos, mb, mx, my, ox, oy, color, thickness): # marker tool
    if tool == "Marker":
        screen.set_clip(canvas)
        if mx == ox and my == oy: #Checks if mouse was stable
            draw.circle(screen, color, (ox,oy), thickness) #draws a circle at the mouses position
        else:
            dx = mx-ox #distance between mx and ox
            dy = my-oy #distance between my andoy
            dist = hypot(dx, dy) # distance between old mouse pos and new mouse pos
            x = dx/dist
            y = dy/dist
            for i in range(int(dist)):
                draw.circle(screen, color, (int(ox+i*x), int(oy+i*y)), thickness) # drawing the circle at every pixel

def eraser(tool, screen, canvas, mpos, mb, mx, my, ox, oy, thickness): # Eraser tool
    if tool == "Eraser":
        screen.set_clip(canvas)
        if mx == ox and my == oy: #Checks if mouse was stable
            draw.circle(screen, (255, 255, 255), (ox,oy),thickness) #draws a circle at the mouses position
        else:
            dx = mx-ox #distance of mx and ox
            dy = my-oy #distance of my, oy
            dist = hypot(dx, dy) # distance between old mouse pos and new mouse pos
            x = dx/dist
            y = dy/dist
            for i in range(int(dist)):
                draw.circle(screen, (255, 255, 255), (int(ox+i*x), int(oy+i*y)), thickness) # drawing the circle at every pixel

def spray(tool, screen, canvas, mpos, mb, mx, my, color, thickness): #spray tool
    if tool == "Spray":
        screen.set_clip(canvas)
        for i in range(thickness*3): #increases speed
            x=randint(-thickness,thickness) # Finds a random x coordinates
            y=randint(-thickness,thickness) # Finds a random y coordinates
            if hypot(x,y) < thickness-1:
                screen.set_at((x+mx,y+my),(color))

def flood(tool, screen, canvas, color, mb, mpos, mx, my): # Flood tool
    if tool == "Flood Fill" and canvas.collidepoint(mpos):
        spot = [mpos]
        screen.set_clip(canvas)
        selected_color = tuple(screen.get_at((mx, my)))
        if selected_color != color:
            while len(spot) > 0:
                cx, cy = spot.pop()
                if screen.get_at((cx, cy)) == selected_color and canvas.collidepoint((cx,cy)):
                    screen.set_at((cx, cy), color)
                    spot.append((cx+1, cy))
                    spot.append((cx-1, cy))
                    spot.append((cx, cy+1))
                    spot.append((cx, cy-1))
