from math import pi as PI
import random
import sys
import cairo

RGB_MAX = 255

BACKGROUND_COLORS = [
    {'r': 42/RGB_MAX, 'g': 177/RGB_MAX, 'b': 3/RGB_MAX}, #GREEN
    {'r': 154/RGB_MAX, 'g': 2/RGB_MAX, 'b': 2/RGB_MAX} #RED
]
COLOR_PALLETE = [
    {'r': 55/RGB_MAX, 'g': 72/RGB_MAX, 'b': 102/RGB_MAX},  #DARK_BLUE
    {'r': 33/RGB_MAX, 'g': 150/RGB_MAX, 'b': 243/RGB_MAX}, #LIGHT_BLUE
    {'r': 255/RGB_MAX, 'g': 235/RGB_MAX, 'b': 59/RGB_MAX}, #YELLOW
    {'r': 255/RGB_MAX, 'g': 152/RGB_MAX, 'b': 0/RGB_MAX} , #ORANGE 
    {'r': 255/RGB_MAX, 'g': 0/RGB_MAX, 'b': 0/RGB_MAX},    #RED
    {'r': 139/RGB_MAX, 'g': 95/RGB_MAX, 'b': 74/RGB_MAX}   #GREEN
]

def on_draw(ctx, width, height, dimension, radius):
    draw_background(ctx, width, height)
    x_offset, y_offset = int(width / dimension), int(height / dimension)

    for row in range(0, dimension):
        for col in range(0, dimension):
            dot_color = COLOR_PALLETE[ random.randint(0, len(COLOR_PALLETE) - 1) ]
            x = (col * x_offset) + (x_offset / 2) + random.randint(-10, 10)
            y = (row * y_offset) + (y_offset / 2) + random.randint(-10, 10)
            draw_circle(ctx, x, y, radius, dot_color)

def draw_background(ctx, width, height):
    ctx.save()
    ctx.scale(width, height)
    ctx.rectangle(0, 0, 1, 1)
    bg = BACKGROUND_COLORS[ random.randint(0, len(BACKGROUND_COLORS)-1) ]
    ctx.set_source_rgb( bg['r'], bg['g'], bg['b'] )
    ctx.fill()
    ctx.restore()

def draw_circle(ctx, x, y, radius, color):
    BASE_OFFSET = 10
    shadow_offset_x, shadow_offset_y = random.randint(-BASE_OFFSET, BASE_OFFSET), random.randint(-BASE_OFFSET, BASE_OFFSET) 

    ctx.save()
    draw_shadow(ctx, x, y, radius, shadow_offset_x, shadow_offset_y)
    ctx.set_source_rgb( color['r'], color['g'], color['b'] )
    ctx.arc(x, y, radius, 0, 2 * PI)
    ctx.fill_preserve()
    ctx.restore()

def draw_shadow(ctx, width, height, radius, offset_x, offset_y):
    ctx.set_source_rgba(0, 0, 0, 0.3)
    ctx.arc(width + offset_x, height + offset_y, radius, 0, 2 * PI)
    ctx.fill()

if __name__ == "__main__":
    width = int(sys.argv[1]) if len(sys.argv) > 1 else 1600
    height = int(sys.argv[2]) if len(sys.argv) > 2 else 1600
    dimension = int(sys.argv[3]) if len(sys.argv) > 3 else 10
    radius = int(sys.argv[4]) if len(sys.argv) > 4 else 30

    print('USING width: ', width)
    print('USING height: ', height)
    print('USING DIMENSION: ', dimension)
    print('USING RADIUS: ', radius)

    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
    ctx = cairo.Context(surface)
    on_draw(ctx, width, height, dimension, radius)
    surface.write_to_png("./outputs/dots.png")
