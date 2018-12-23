from math import pi as PI
import subprocess as s
import random
import cairo

WIDTH, HEIGHT = 1024, 512
RGB_MAX = 255

def draw():
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
    ctx = cairo.Context(surface)

    radius = 30
    
    for frame_count in range(200):
        paint_board(ctx, WIDTH, HEIGHT)
        draw_line(ctx, HEIGHT / 2, radius)
        surface.write_to_png('./tmp/frame_%06d.png' % frame_count)
    
    s.Popen('mencoder mf://./tmp/frame*.png -mf w=600:h=400:fps=10:type=png -ovc lavc -lavcopts vcodec=mpeg4:mbd=2:trell -oac copy -o ./tmp/output.avi && mplayer ./tmp/output.avi', shell=True)

def draw_line(ctx, y, radius):
    GREEN, COLOR_STEP = random.uniform(0, 1), random.uniform(0.01, 0.1)

    for x in range(radius, WIDTH - radius, radius):
        draw_circle(
            ctx, 
            x, 
            y,
            radius, 
            {'r': 1, 'g': GREEN, 'b': 0})
        GREEN += COLOR_STEP

def paint_board(ctx, width, height):
    ctx.save()
    ctx.scale(width, height)
    ctx.rectangle(0, 0, 1, 1) 
    ctx.set_source_rgb(253/RGB_MAX, 227/RGB_MAX, 167/RGB_MAX)
    ctx.fill()
    ctx.restore()

def draw_circle(ctx, x, y, radius, color):
    ctx.save()
    ctx.arc(x, y, radius, 0, 2 * PI)
    ctx.set_line_width(2)

    if color != None:
        ctx.set_source_rgb(color['r'], color['g'], color['b'])
        ctx.fill_preserve()

    ctx.set_source_rgb(0, 0, 0)
    ctx.stroke()
    ctx.restore()

draw()