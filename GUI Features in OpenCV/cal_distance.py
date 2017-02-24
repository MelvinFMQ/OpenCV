def cal_dis(start, end):
    delta_x = start[0] - end[0]
    delta_y = start[1] - end[1]
    combined = int((delta_x ** 2 + delta_y ** 2) ** 0.5)
    return combined

print(cal_dis((1,2),(3,4)))
