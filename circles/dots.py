from math import pi as PI
import cairo
import random

WIDTH, HEIGHT = 1600, 1600
RGB_MAX = 255

COLORS = {
    'darkbrown': {'r': 120/RGB_MAX, 'g': 90/RGB_MAX, 'b': 126/RGB_MAX},
    'darkblue': {'r': 55/RGB_MAX, 'g': 72/RGB_MAX, 'b': 102/RGB_MAX}
}

def on_draw(ctx):
    draw_background(ctx, WIDTH, HEIGHT)
    draw_circle(ctx, 30, COLORS['darkblue'])

def draw_background(ctx, width, height):
    ctx.save()
    ctx.scale(WIDTH, HEIGHT)
    ctx.rectangle(0, 0, 1, 1)
    ctx.set_source_rgb( COLORS['darkbrown']['r'], COLORS['darkbrown']['g'], COLORS['darkbrown']['b'] )
    ctx.fill()
    ctx.restore()

def draw_circle(ctx, radius, color):
    shadow_offset_x, shadow_offset_y = random.randint(-30, 30), random.randint(-30, 30) 

    ctx.save()
    draw_shadow(ctx, WIDTH/2, HEIGHT/2, radius, shadow_offset_x, shadow_offset_y)
    ctx.set_source_rgb( color['r'], color['g'], color['b'] )
    ctx.arc(WIDTH/2, HEIGHT/2, radius, 0, 2 * PI)
    ctx.fill_preserve()
    ctx.restore()

def draw_shadow(ctx, width, height, radius, offset_x, offset_y):
    ctx.set_source_rgba(0, 0, 0, 0.3)
    ctx.arc(width + offset_x, height + offset_y, radius, 0, 2 * PI)
    ctx.fill()

if __name__ == "__main__":
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
    ctx = cairo.Context(surface)
    on_draw(ctx)
    surface.write_to_png("./outputs/dots.png")
