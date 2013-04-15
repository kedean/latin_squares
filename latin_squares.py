from random import shuffle
from itertools import permutations

def verifySquares(squares, dim):
    seen = []
    for rows in squares:
        if len(rows) < dim:
            return False
        for row in rows:
            if len(row) < dim or row in seen:
                return False
            else:
                seen.append(row)
    return True

def createSquares(dim, auto_verify=True):
    #construct the rows to extract from
    rows = [r for r in permutations(range(0, dim))]
    shuffle(rows)

    #construct the squares of the cube
    squares = [rows[dim*index:dim*(index+1)] for index in range(0, dim)]

    #verify that the squares are valid
    if auto_verify and verifySquares(squares, dim) == False:
        raise ValueError("The latin squares produced were not valid. This may be due to using a dimension less than 4.")

    return squares

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-pprint", dest="pprint", action="store_true", help="Uses pythons pprint library to output instead of manual printing.")
    parser.add_argument("dim", type=int, help="Dimension of the cube that is produced.")
    args = parser.parse_args()

    try:
        squares = createSquares(args.dim)
    except:
        print("An error occured, make sure you did not use a dimension less than 4.")
        exit()

    if args.pprint:
        import pprint
        pprint.pprint(squares)
    else:
        rowsep = "".join("---" * len(squares[0][0]))
        for rows in squares:
            print(rowsep)
            for row in rows:
                print(" " + ", ".join(map(str, row)))
        print(rowsep)