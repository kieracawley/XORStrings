import sys
mode = sys.argv[1]
keyfile = sys.argv[2]
inpfile = sys.argv[3]
key = open(keyfile).read()[:-1] #removes the mandatory \n at the end of the file to support one line messages.
inp = open(inpfile).read()[:-1] #removes the mandatory \n at the end of the file to support one line messages.

new = key
index = 0
while len(new) < len(inp):
    new += key[index % len(key)]
    index += 1

final = ""
for i in range(len(inp)):
    if (mode == "numOut"):
        final = final + (hex(ord(new[i]) ^ ord(inp[i])))[2:] + " "
    else:
        final = final + chr(ord(new[i]) ^ ord(inp[i]))

print(final)
