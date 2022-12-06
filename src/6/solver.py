import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

file1 = open(os.path.join(__location__, 'input.txt'))
lines = file1.readlines()

dict = {}

startofpacket = False

for line in lines:
    lastfour = []
    lastfourten = []
    for pos, char in enumerate(line):
        if not startofpacket:
            if len(set(lastfour)) == 4:
                startofpacket = True
                print(f"found startofpacket {pos}")
            if len(lastfour) < 4:
                lastfour.append(char)
            else:
                lastfour = lastfour[1:4] + [char]

        if startofpacket:
            if len(set(lastfourten)) == 14:
                print(f"found startofmessage {pos}")
                print(pos)
            if len(lastfourten) < 14:
                lastfourten.append(char)
            else:
                lastfourten = lastfourten[1:14] + [char]
