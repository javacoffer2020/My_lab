def level_24() -> None:
    print(f"\033[31mLevel 24\033[0m")
    import numpy as np
    from PIL import Image
    im0 = Image.open("source/maze.png")
    rgba_array = np.asarray(im0, dtype=np.uint8).copy()
    im0 = im0.convert(mode="1")
    maze_array = np.asarray(im0, dtype=np.uint8).copy()
    maze_array = 1 - maze_array

    n, m = maze_array.shape
    queue_list = [(0, m - 2)]
    path_array = np.zeros((n, m, 2), dtype=np.int)
    dx_tuple, dy_tuple = (0, 0, 1, -1), (1, -1, 0, 0)
    while queue_list:
        x, y = queue_list.pop(0)
        maze_array[x, y] = 0
        if x == n - 1:
            break
        for dx, dy in zip(dx_tuple, dy_tuple):
            xx, yy = x + dx, y + dy
            if 0 <= xx < n and 0 <= yy < m and maze_array[xx, yy]:
                maze_array[xx, yy] = False
                path_array[xx, yy] = [x, y]
                queue_list.append((xx, yy))

    im1 = Image.new(mode="1", size=(n, m), color=1)
    r_list = []
    x, y = n - 1, 1
    while x != 0 or y != 0:
        im1.putpixel((x, y), 0)
        r_list.append(rgba_array[x, y, 0])
        x, y = path_array[x, y]
    # im1.save("level_24/path.png")
    im1.show()

    r_list = r_list[-2::-2]
    r_bytes = bytes(r_list)
    with open("source/red.rar", "wb") as file:
        file.write(r_bytes)


if __name__ == "__main__":
    level_24()

