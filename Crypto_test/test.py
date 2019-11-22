data = [12, 23, 250, 100]
key = [125, 230, 3, 65]
out = [0, 0, 0, 0]

mix_matrix = [[2, 1, 6, 3], [9, 6, 6, 3], [2, 5, 6, 8], [8, 7, 2, 3]]

def shift_one(numb):
    if numb > 128:
        numb -= 128
        numb //= 2
        numb += 1

    else:
        numb //= 2

    return numb

# first cycle
for i in range(len(data)):
    out[i] = data[i] ^ key[i % len(key)]

# the 13 turn
for _ in range(13):
    # substitution
    for i in range(len(out)):
       out[i] = 256 - out[i]

    # shift rows
    out[1] = shift_one(out[1])

    for _ in range(2):
        out[2] = shift_one(out[2])

    for _ in range(3):
        out[3] = shift_one(out[3])
    

    # mix matrix
    new = [0, 0, 0, 0]

    new[0] = ((2 * out[0]) % 256) ^ ((3 * out[1]) % 256) ^ out[2] ^ out[3]
    new[1] = ((2 * out[1]) % 256) ^ ((3 * out[2]) % 256) ^ out[3] ^ out[0]
    new[2] = ((2 * out[2]) % 256) ^ ((3 * out[3]) % 256) ^ out[0] ^ out[1]
    new[3] = ((2 * out[3]) % 256) ^ ((3 * out[0]) % 256) ^ out[1] ^ out[2]

    print(out[0], ((14 * new[0]) % 256) ^ ((11 * new[1]) % 256) ^ ((13 * new[2]) % 256) ^ ((9 * new[3]) % 256))   
    out = new

    # add
    for i in range(len(data)):
        out[i] = out[i] ^ key[i % len(key)]

    print(out)
