def level_32() -> None:
    print(f"\033[31mLevel 32\033[0m")
    import numpy as np
    from PIL import Image

    is_solved = False
    ans_points = np.zeros(1)

    n = 9
    horizontal = [[2, 1, 2], [1, 3, 1], [5], [7], [9], [3], [2, 3, 2], [2, 3, 2], [2, 3, 2]]
    vertical = [[2, 1, 3], [1, 2, 3], [3], [8], [9], [8], [3], [1, 2, 3], [2, 1, 3]]

    n = 32
    horizontal = [[3, 2], [8], [10], [3, 1, 1],
                  [5, 2, 1], [5, 2, 1], [4, 1, 1], [15],
                  [19], [6, 14], [6, 1, 12], [6, 1, 10],
                  [7, 2, 1, 8], [6, 1, 1, 2, 1, 1, 1, 1], [5, 1, 4, 1], [5, 4, 1, 4, 1, 1, 1],
                  [5, 1, 1, 8], [5, 2, 1, 8], [6, 1, 2, 1, 3], [6, 3, 2, 1],
                  [6, 1, 5], [1, 6, 3], [2, 7, 2], [3, 3, 10, 4],
                  [9, 12, 1], [22, 1], [21, 4], [1, 17, 1],
                  [2, 8, 5, 1], [2, 2, 4], [5, 2, 1, 1], [5]]
    vertical = [[5], [5], [5], [3, 1],
                [3, 1], [5], [5], [6],
                [5, 6], [9, 5], [11, 5, 1], [13, 6, 1],
                [14, 6, 1], [7, 12, 1], [6, 1, 11, 1], [3, 1, 1, 1, 9, 1],
                [3, 4, 10], [8, 1, 1, 2, 8, 1], [10, 1, 1, 1, 7, 1], [10, 4, 1, 1, 7, 1],
                [3, 2, 5, 2, 1, 2, 6, 2], [3, 2, 4, 2, 1, 1, 4, 1], [2, 6, 3, 1, 1, 1, 1, 1], [12, 3, 1, 2, 1, 1, 1],
                [3, 2, 7, 3, 1, 2, 1, 2], [2, 6, 3, 1, 1, 1, 1], [12, 3, 1, 5], [6, 3, 1],
                [6, 4, 1], [5, 4], [4, 1, 1], [5]]

    def print_points(points: np.array) -> None:
        # print array in console
        if points[0, 0] == -2:
            print("ERROR\n")
            return
        for i in range(n):
            for j in range(n):
                if points[i, j] >= 1:
                    print('█', end='')
                elif points[i, j] == 1:
                    print('■', end='')
                elif points[i, j] == 0:
                    print('.', end='')
                elif points[i, j] == -1:
                    print('×', end='')
            print()
        print()

    def horizontal_put(points: np.array, x: int, y0: int, y1: int) -> np.array:
        # the next position of current array is already occupied
        if y1 + 1 < n and np.min(points[x, y0:y1 + 1]) >= 1:
            points[0, 0] = -3
            return points
        # some positions of current array are inaccessible
        if np.min(points[x, y0:y1]) == -1 or (y1 < n and points[x, y1] > 0):
            points[0, 0] = -2
            return points
        # set all positions of current array occupied
        points[x, y0:y1] = 1
        # set the next position of current array inaccessible
        if y1 < n:
            points[x, y1] = -1
        return points

    def vertical_put(points: np.array) -> np.array:
        for y in range(n):
            x = 0
            # this column is already finished
            if points[n - 1, y] != 0:
                continue
            for i, nums in enumerate(vertical[y]):
                # find next begin position of this column
                while x < n and points[x, y] <= 0:
                    x += 1
                # at the end of this column
                if x == n:
                    break
                # goto the end position of current array
                if points[x, y] == 2:
                    x += nums
                # not enough positions to put current array
                elif points[x, y] == 1 and x + nums - 1 >= n:
                    points[0, 0] = -2
                    return points
                # set positions of current array occupied
                elif points[x, y] == 1:
                    points[x, y] = 2
                    points[x + 1:x + nums, y] = 1
                    # set the next position of current array inaccessible
                    if x + nums < n:
                        points[x + nums, y] = -1
                    # this is the last array and set all rest positions inaccessible
                    if i + 1 == len(vertical[y]) and x + nums < n:
                        points[x + nums:, y] = -1
                    break
        return points

    def search(points: np.array, x: int, y: int, k: int) -> None:
        nonlocal is_solved, ans_points
        # solution is found
        if x == n:
            print_points(points)
            ans_points = points.copy()
            is_solved = True
            return

        # the last position of this row can start this array
        j_end = n - sum(horizontal[x][k:]) - (len(horizontal[x]) - k - 1)

        for j in range(y, j_end + 1):
            # the previous position of current array is occupied
            if j >= 1 and points[x, j - 1] > 0:
                break

            # create a copy
            j1 = j + horizontal[x][k]
            new_points = points.copy()

            # try to put current array into positions row[x] column[j-j1]
            new_points = horizontal_put(new_points, x, j, j1)
            # error code -2
            if new_points[0, 0] == -2:
                continue
            # error code -3
            elif new_points[0, 0] == -3:
                break

            # check and put arrays in columns
            new_points = vertical_put(new_points)
            if new_points[0, 0] == -2:
                continue

            # this is the last array of this row, but some rest positions of this row are still occupied
            if k + 1 == len(horizontal[x]) and j1 < n and np.max(new_points[x, j1:]) > 0:
                continue

            # recur to next
            if k + 1 == len(horizontal[x]):
                search(new_points, x + 1, 0, 0)
            else:
                search(new_points, x, j1 + 1, k + 1)

            # solution is already found
            if is_solved:
                return

    search(np.zeros((n, n), dtype=np.int), 0, 0, 0)

    ans_points[ans_points > 0] = 255
    ans_points[ans_points <= 0] = 0
    im = Image.fromarray(ans_points.astype(np.uint8), "L")
    im.show()


if __name__ == "__main__":
    level_32()