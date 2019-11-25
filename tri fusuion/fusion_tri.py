import random as rd
import time

def tri(data):

    # recursive case
    if len(data) >= 2:
        # recursive call
        return_1 = tri(data[:len(data) // 2])
        return_2 = tri(data[len(data) // 2:])
        cursor1 = 0
        cursor2 = 0
        new = []

        # fusion
        while cursor1 < len(return_1) or cursor2 < len(return_2):
            if cursor1 < len(return_1) and cursor2 < len(return_2):
                # the comparasion between the 2
                if return_1[cursor1] <= return_2[cursor2]:
                    new.append(return_1[cursor1])
                    cursor1 += 1

                else: 
                    new.append(return_2[cursor2])
                    cursor2 += 1

            # only one not empty
            elif cursor1 < len(return_1):
                new.append(return_1[cursor1])
                cursor1 += 1

            elif cursor2 < len(return_2):
                new.append(return_2[cursor2])
                cursor2 += 1

        return new

    # other case    
    return data

def classic(data):
    new = []
    mini = None

    while len(data) > 0:
        for el in data:
            if not mini or el <= mini:
                mini = el

        data.remove(mini)
        new.append(mini)
        mini = None

    return new




if __name__ == "__main__":
    t = time.time()
    tri(list((rd.random()) for _ in range(20_000)))
    print("Fusoin execute in %.4f s" % (time.time() - t))

    t = time.time()
    classic(list((rd.random()) for _ in range(20_000)))
    print("Classic execute in %.4f s" % (time.time() - t))