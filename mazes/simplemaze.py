import sys
import random
import cairo
import numpy
import subprocess as s

CELL_SIZE, WALL_SIZE = 20, 10

def draw(width, height, generate_video = False):
    X_DIMENSION, Y_DIMENSION = int(width/CELL_SIZE), int(height/CELL_SIZE)
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
    ctx = cairo.Context(surface)

    paint_background(ctx, width, height)
    draw_grid(ctx, width, height)
    generate_maze(ctx, surface, width, height, X_DIMENSION, Y_DIMENSION, generate_video)
    surface.write_to_png('./maze.png')

    if generate_video:
        s.Popen('mencoder mf://./tmp/maze*.png -mf w=600:h=400:fps=10:type=png -ovc lavc -lavcopts vcodec=mpeg4:mbd=2:trell -oac copy -o ./tmp/output.avi && mplayer ./tmp/output.avi', shell=True)

def generate_maze(ctx, surface, width, height, X_DIMENSION, Y_DIMENSION, generate_video = False):
    frame_count = 0
    maze = numpy.zeros((X_DIMENSION, Y_DIMENSION), dtype=bool)
    stack = []

    remove_wall_between( ctx, (0, 0), (0, 0)) #open entrance
    remove_wall_between( ctx, (X_DIMENSION-1, Y_DIMENSION-1), (X_DIMENSION-1, Y_DIMENSION) )
    
    curr_cell = ( random.randint(0, X_DIMENSION-1), random.randint(0, Y_DIMENSION-1) )
    maze[curr_cell[0], curr_cell[1]] = True #mark as visited
    visited_count = 1

    while visited_count < X_DIMENSION * Y_DIMENSION:
        unvisited_neighbour = get_unvisited_neighbour(maze, curr_cell)

        if unvisited_neighbour != None:
            stack.append(curr_cell)            
            remove_wall_between( ctx, curr_cell, unvisited_neighbour )

            if generate_video:
                surface.write_to_png('./tmp/maze_%06d.png' % frame_count)
                frame_count += 1

            curr_cell = unvisited_neighbour
            maze[curr_cell[0], curr_cell[1]] = True #Visited
            visited_count += 1          
        elif len(stack):
            curr_cell = stack.pop()
            
def get_unvisited_neighbour(maze, cell):
    candidates = []
    X_DIMENSION, Y_DIMENSION = maze.shape[0], maze.shape[1] 
    
    x, y = cell[0], cell[1] + 1, 
    if y >= 0 and y < Y_DIMENSION and x >= 0 and x < X_DIMENSION and maze[x, y] == False: 
       candidates.append( (x, y) )

    x, y = cell[0], cell[1]-1
    if y >= 0 and y < Y_DIMENSION and x >= 0 and x < X_DIMENSION and maze[x, y] == False:
       candidates.append( (x, y) )

    x, y = cell[0]+1, cell[1]
    if y >= 0 and y < Y_DIMENSION and x >= 0 and x < X_DIMENSION and maze[x, y] == False:
       candidates.append( (x, y) )

    x, y = cell[0]-1, cell[1]
    if y >= 0 and y < Y_DIMENSION and x >= 0 and x < X_DIMENSION and maze[x, y] == False:
       candidates.append( (x, y) )

    if len(candidates):
        idx = random.randint(0, len(candidates)-1)
        return candidates[idx]
    else:
        return None
        
def remove_wall_between(ctx, cell1, cell2):
    ctx.save()
    ctx.set_source_rgb(1, 1, 1)
    ctx.set_line_width(WALL_SIZE)

    if cell1[0] == cell2[0]:
        y_brush_pos = max(cell1[1], cell2[1]) * CELL_SIZE
        offset = int(WALL_SIZE/2)
        x_start = cell1[0]*CELL_SIZE
        ctx.move_to(x_start + offset, y_brush_pos)
        ctx.line_to(x_start + CELL_SIZE - offset, y_brush_pos)    
    else:
        x_brush_pos = max(cell1[0], cell2[0]) * CELL_SIZE
        offset = int(WALL_SIZE/2)
        y_start = cell1[1]*CELL_SIZE
        ctx.move_to(x_brush_pos, y_start + offset)
        ctx.line_to(x_brush_pos, y_start + CELL_SIZE - offset)  

    ctx.stroke()
    ctx.restore()

def paint_background(ctx, WIDTH, HEIGHT):
    ctx.rectangle(0, 0, WIDTH, HEIGHT)
    ctx.set_source_rgb(1, 1, 1)
    ctx.fill()

def draw_grid(ctx, WIDTH, HEIGHT):
    ctx.save()
    ctx.set_source_rgb(0, 0, 0)
    ctx.set_line_width(WALL_SIZE)

    for y in range(0, HEIGHT + 1, CELL_SIZE):
        ctx.move_to(0, y)
        ctx.line_to(WIDTH, y)
        ctx.stroke()

    for x in range(0, WIDTH + 1, CELL_SIZE):
        ctx.move_to(x, 0)
        ctx.line_to(x, HEIGHT)
        ctx.stroke()  
          
    ctx.restore()

if __name__ == "__main__":
    if len(sys.argv) < 3: 
        print('Invalid arguments!')
        exit(1)
    elif len(sys.argv) == 4 and sys.argv[3] != '--video':
        print('Invalid argument! Only "--video" is expected as third argument')
        exit(2)

    width, height = sys.argv[1], sys.argv[2]
    draw( int(width), int(height), len(sys.argv) == 4 )