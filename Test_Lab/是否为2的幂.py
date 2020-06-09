def is_power_of_2(num):
    return (num & num - 1) == 0


print(is_power_of_2(128))
print(is_power_of_2(8))
print(is_power_of_2(0))
print(is_power_of_2(1))
print(is_power_of_2(12))