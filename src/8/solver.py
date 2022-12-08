import math
import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

file1 = open(os.path.join(__location__, 'input.txt'))
lines = file1.readlines()

trees: [[]] = []

for line in lines:
    line = line.strip()
    row = []
    for char in line:
        row.append(int(char))
    trees.append(row)
visible = 0

columns = len(trees[0])
rows = len(trees)
visibletree = set()


def check_scenery(startcol, startrow, tree_house_height):
    print(f"check {startcol}:{startrow} treehouseheight:{tree_house_height}")
    scenery_all_dirs = []
    for dir in ["up", "down", "right", "left"]:
        print(dir)
        scenery = 0
        if dir == "up" or dir == "down":
            for col in [startcol]:
                r = list(range(startrow, -1,-1))
                if dir == "down":
                    r = range(startrow,rows)
                for row in r:
                    print(f"checking {col}:{row}")
                    height = trees[row][col]
                    if row == startrow and col == startcol:
                        pass
                    elif height < tree_house_height:
                        print(f"{row}:{col} {height} lower than {tree_house_height}")
                        scenery = scenery + 1
                    else:
                        print(f"{row}:{col} {height} higher than {tree_house_height}")
                        scenery = scenery + 1
                        break
        if dir == "left" or dir == "right":
            for row in [startrow]:
                r = list(range(startcol, columns))
                if dir == "left":
                    r = range(startcol,-1,-1)
                for col in r:

                    height = trees[row][col]
                    if row == startrow and col == startcol:
                        pass
                    elif height < tree_house_height:
                        print(f"{row}:{col} {height} lower than {tree_house_height}")
                        scenery = scenery + 1
                    else:
                        print(f"{row}:{col} {height} higher than {tree_house_height}")
                        scenery = scenery + 1
                        break
        scenery_all_dirs.append(scenery)
    print(scenery_all_dirs)
    return math.prod(scenery_all_dirs)


bestscenery = 0
for startrow in range(0, rows):
    for startcol in range(0, columns):
        scenerypoints = check_scenery(startcol=startcol, startrow=startrow, tree_house_height=trees[startrow][startcol])
        if scenerypoints > bestscenery:
            bestscenery = scenerypoints
print(bestscenery)
