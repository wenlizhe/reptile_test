# 有个楼梯，每次只能走1或者2阶，一共几种走法

def count_way(current_floor):
    basic_num = {1: 1, 2: 2}
    if current_floor in basic_num.keys():
        return basic_num[current_floor]
    else:
        return count_way(current_floor-1) + count_way(current_floor-2)


if __name__ == '__main__':
    print(count_way(1))
