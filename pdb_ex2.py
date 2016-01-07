#pdb_ex2.py
import pdb


def add_one(num):
    result = num + 1
    print(result)
    return result

#exercise used xrange on line13 which was replaced with range in python 3
def main():
    pdb.set_trace()
    for num in range(0,10):
        add_one(num)


if __name__ == '__main__':
    main()
