import sys
im =[list('..########################...........'),
list('..#......................#...#####...'),
list('..#..........########....#####...#...'),
list('..#..........#......#............#...'),
list('..#..........########.........####...'),
list('..######......................#......'),
list('.......#..#####.....###########......'),
list('.......####...#######................')]
HEIGHT = len(im)
WIDTH = len(im[0])

def printImage(image):
    for y in range(HEIGHT):
    # Print each row.
        for x in range(WIDTH):
        # Print each column.
            sys.stdout.write(image[y][x])
        sys.stdout.write('\n')
    sys.stdout.write('\n')


def floodFill(image, xi, yi, newChar, oldChar=None):
    if oldChar == None:
        oldChar = image[yi][xi]
    if oldChar == newChar or image[yi][xi] != oldChar:
        return
    image[yi][xi] = newChar
    printImage(im)
    if yi + 1 < HEIGHT and image[yi + 1][xi]== oldChar:
        floodFill(image, xi, yi + 1,newChar, oldChar)
    if yi - 1 >= 0 and image[yi - 1][xi] == oldChar:
        floodFill(image, xi, yi - 1,newChar, oldChar)
    if xi + 1 < WIDTH and image[yi][xi + 1]== oldChar:
        floodFill(image, xi + 1, yi,
                newChar, oldChar)
    if xi - 1 >= 0 and image[yi][xi - 1] ==oldChar:
            floodFill(image, xi - 1, yi,newChar, oldChar)
    return


printImage(im)
floodFill(im, 3, 3, 'o')
printImage(im)