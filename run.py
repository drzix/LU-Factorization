from lib.matrix import *

try:
    # sm = SquareMatrix([[2, 3],  # 2x2
    #                   [6, 10]])
    # sm = SquareMatrix([[1, 3, 5],  # 3x3
    #                   [2, 4, 7],
    #                   [1, 1, 0]])
    # sm = SquareMatrix([[11, 9, 24, 2],  # 4x4
    #                   [1, 5, 2, 6],
    #                   [3, 17, 18, 1],
    #                   [2, 5, 7, 1]])
    sm = SquareMatrix([[1, 2, -1, 1, 3],  # 5x5
                      [6, 2, 23, 4, 12],
                      [7, 6, 2, 8, 12],
                      [8, 5, -9, 7, 66],
                      [15, 2, -34, 1, 4]])

    l, u = sm.lu_factorize()
    print("A")
    print(sm)
    print("L")
    print(l)
    print("U")
    print(u)
    print("A = LU")
    print(l * u)

except Exception as e:
    print('Error: ' + e.args[0])
