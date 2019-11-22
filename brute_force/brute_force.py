import hashlib as hl
import string
import time

# get the password
c = input("Char set (1) all chars (2) letters + digits (1/2) > ")
h = input("Hash (1) sha_256 (2) sha3_256 (1/2) > ")
has = hl.sha256 if h == "1" else hl.sha3_256


password = input("Password > ")
p_hash = has(password.encode()).hexdigest()
print("Hash > %s" % p_hash)

# data use
size = 1
test = []

dic = string.printable if c == "1" else string.ascii_letters + string.digits



max_size = len(dic) - 1
started = time.time()

def end(data, size):
    # end of brutforce for a nb of chars
    for nb in data:
        if nb != size:
            return False

    return True

# loop
while True:
    test = list(0 for _ in range(size))

    # loop for a size
    while not end(test, max_size):
        test_hash = has(("".join((dic[a]) for a in test )).encode()).hexdigest()

        # finish
        if test_hash == p_hash:
            break

        # next word
        prev = True
        for i in range(len(test_hash)):
            i = size - 1 - i
            if prev:
                if test[i] != max_size:
                    prev = False
                test[i] = (test[i] + 1) % (max_size + 1)
                

    if test_hash == p_hash:
        break

    size += 1


print("find after %d s > %s" % (int(time.time() - started) ,"".join((dic[a]) for a in test)))