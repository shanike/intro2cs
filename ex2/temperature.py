#################################################################
# FILE : larges_and_smallest.py
# WRITER : Shani Kehati, shani , 322866823
# EXERCISE : intro2cs2 ex2
# DESCRIPTION: check if it is summer according to provided threshold_temp(int) and first, second and third days temperatures
#################################################################


def is_it_summer_yet(threshold_temp, first_day_temp, second_day_temp, third_day_temp) -> bool:
    """
    returns whether it is summer yet according to given parameters (threshold_temp, first_day_temp, second_day_temp, third_day_temp)
    notice: - all params are numbers
    """
    over_threshold_cnt = 0
    if first_day_temp > threshold_temp:
        over_threshold_cnt += 1
    if second_day_temp > threshold_temp:
        over_threshold_cnt += 1
    if third_day_temp > threshold_temp:
        over_threshold_cnt += 1
    return over_threshold_cnt >= 2


if __name__ == "__main__":
    print(is_it_summer_yet(7, 5, -2, 11))
