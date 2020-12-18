import numpy, scipy.ndimage

active = "#"

def parseInput(fileName):
    lines = []
    with open(fileName) as f:
        for line in f:
            l = line.strip()
            lines.append(l)

    return numpy.array([[c == active for c in line] for line in lines])


#This is heavily refactored after seeing https://www.reddit.com/r/adventofcode/comments/keqsfa/2020_day_17_solutions/gg4kafh?utm_source=share&utm_medium=web2x&context=3 from u/thomasahle
def part1(fileName, dimensions, iterations):

    D = dimensions
    
    flatcube = parseInput(fileName)
    cube = numpy.expand_dims(flatcube, axis=tuple(range(D - 2)))

    #intialize sliding window with 1s except for us
    slidingWindow = numpy.ones(shape=(3,) * D) 
    slidingWindow[(1,) * D] = 0

    for _ in range(iterations):
        #Have to deal with more neighbors each iteration
        cube = numpy.pad(cube, 1).astype(int)
        neighborCount = scipy.ndimage.convolve(cube, slidingWindow, mode="constant", cval=0)
        cube = (cube == 1) & ((neighborCount == 2) | (neighborCount == 3)) | (cube == 0) & (neighborCount == 3)

    return(numpy.sum(cube))




print(part1("input", 3, 6), part1("input", 4, 6))