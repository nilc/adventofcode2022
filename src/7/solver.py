import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

import re

file1 = open(os.path.join(__location__, 'input.txt'))
lines = file1.readlines()

startofpacket = False

dirs: dict = {}


class file():
    name: str
    size: int

    def __init__(self, name, size):
        self.name = name
        self.size = size

    def getsize(self):
        return self.size


allpaths = []


class Path():
    rootpath = False

    def __init__(self, name, parent_path):
        self.name = name
        self.parent_path = parent_path
        self.sub_paths = {}
        self.files: [file] = []

    def getsize(self):
        size = 0
        for f in self.files:
            size = size + f.size
        for p in list(self.sub_paths.values()):
            if (p != self):
                print(p.get_path())
                size = size + p.getsize()
        return size

    def get_path(self):

        parent_path = self.parent_path
        parents = [self, parent_path]
        while parent_path.rootpath is not True:
            parent_path = parent_path.parent_path
            parents.append(parent_path)

        parents.reverse()
        return "/".join(map(lambda t: t.name, parents))


rootpath = Path("/", None)
rootpath.rootpath = True
rootpath.parent_path = rootpath

currentpath = rootpath
for line in lines:
    line = line.strip()
    print(f"[{currentpath.get_path()}] line is {line}")
    if line.startswith("$ "):
        if line.startswith("$ cd "):
            cdcommand = re.search(r"cd (.*)", line)
            cd_dir = cdcommand.group(1)
            if cd_dir == "/":
                currentpath = rootpath
            elif cd_dir == "..":
                currentpath = currentpath.parent_path
            else:
                # if cd_dir not in currentpath.sub_paths.keys():
                #    currentpath.sub_paths[cd_dir] = Path(cd_dir, currentpath)
                currentpath = currentpath.sub_paths[cd_dir]
    else:
        if line.startswith("dir "):
            name = line.replace("dir ", "")
            if name not in currentpath.sub_paths.keys():
                newdir = Path(name, currentpath)
                currentpath.sub_paths[name] = newdir
                print(f"added dir {newdir.get_path()} ")
                allpaths.append(newdir)

        else:
            name_size = line.split(" ")
            currentpath.files.append(file(name_size[1], int(name_size[0])))

size = 0
sizeused = rootpath.getsize()
freespace=70000000-sizeused

wantedspace=30000000
space_to_free_up=wantedspace-freespace
mindiff=None
for path in allpaths:
    dir_size = path.getsize()
    if dir_size > space_to_free_up:
        extra_space = dir_size-space_to_free_up
        if mindiff is None or mindiff>extra_space:
            print(f"{path.get_path()} {extra_space} {path.getsize()}")
            mindiff=extra_space
            bestpath=path

print(bestpath.getsize())
