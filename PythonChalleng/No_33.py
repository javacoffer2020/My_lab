def level_33() -> None:
    print(f"\033[31mLevel 33\033[0m")
    from PIL import Image
    import numpy as np

    im = Image.open("source/beer2.png")
    data_list = list(im.getdata())
    data_set = set(data_list)
    while data_set:
        c0 = max(data_set)
        data_set.remove(c0)
        c1 = max(data_set)
        data_set.remove(c1)
        c0, c1 = max(c0, c1), min(c0, c1)

        n = int(len(data_list) ** 0.5)
        data_np = np.array(data_list, dtype=np.uint8).reshape(n, n)
        data_np[data_np >= c1] = 255
        data_np[data_np < c1] = 0
        data_list = [c for c in data_list if c < c1]

        im = Image.fromarray(data_np, "L")
        im.save(f"source/No_33/{n}.png")


if __name__ == "__main__":
    level_33()