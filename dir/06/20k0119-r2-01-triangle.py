count = 0
min_z = 1000
max_x = 0

min_z_list = []
max_x_list = []

for z in range(100):
    for y in range(100):
        for x in range(100):
            if 0 < x < y < z < 100:
                if (x ** 2 + y ** 2) == z ** 2:
                    if z < min_z:
                        min_z = z
                        min_z_list = [x, y, z]
                    if x > max_x:
                        max_x = x
                        max_x_list = [x, y, z]
                    # print(f"{x},{y},{z}")
                    count += 1


print(f"0 < x < y < z < 100 の時 x^2 + y^2 = z^2 を満たす(x, y, z)の数は{count}個\nzが最小となる組(x, y, z):{min_z_list}\nxが最大となるような組(x, y, z):{max_x_list}")