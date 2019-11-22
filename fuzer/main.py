import os

# get paths
path = "./data/"
paths = list((a if not os.path.isdir(path + a) else None) for a in os.listdir(path))

# clear the paths
while None in paths:
    paths.remove(None)

# fuze a file
for file in paths:

    # open file and read data
    with open(path + file, "rb") as fp:
        data = fp.read()

    # random data
    for _ in range(256):
        data = data.replace(os.urandom(1), os.urandom(1), len(data.hex()))
    
    # modify files
    with open(path + file, "wb") as fp:
        fp.write(data)