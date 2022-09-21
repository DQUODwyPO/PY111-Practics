def calculate_paths(shape: (int, int), point: (int, int)) -> int:
    """
    Given field with size rows*cols count available paths from (0, 0) to point

    :param shape: tuple of rows and cols (each from 1 to rows/cols)
    :param point: desired point for horse
    :return: count of paths from (1, 1) to (point[0], point[1]) (numerating from 0, so (0, 0) - left bottom tile)
    """
    rows = shape[0]
    cols = shape[1]
    desk = [[0] * (rows + 4) for _ in range((cols + 4))]
    p = [point[0] + 2, point[1] + 2]
    desk[3][3] = 1
    clt = 0
    while 1:
        cnt = 0
        for i in range(2, rows + 2):
            for j in range(2, cols + 2):
                if desk[i][j] > 0 and [i, j] != p:
                    cnt += 1
                    desk[i - 2][j - 1] += desk[i][j]
                    desk[i - 2][j + 1] += desk[i][j]
                    desk[i + 2][j - 1] += desk[i][j]
                    desk[i + 2][j + 1] += desk[i][j]
                    desk[i - 1][j - 2] += desk[i][j]
                    desk[i - 1][j + 2] += desk[i][j]
                    desk[i + 1][j - 2] += desk[i][j]
                    desk[i + 1][j + 2] += desk[i][j]
                    desk[i][j] -= desk[i][j] * 8
                    # не закончено
        for j in range(cols + 4):
            print(desk[j])
        print()
        clt += 1
        if cnt == 0 or clt == 10:
            break
    #for j in range(cols + 4):
    #    print(desk[j])
    return desk[point[0]][point[1]]
# (8, 8) (7, 7) - 220
#  (5, 5) (4, 4) - 2
calculate_paths((5, 5), (4, 4))
