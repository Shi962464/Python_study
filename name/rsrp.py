import math
def rsrp(number):
    a = math.log10(int(number)) * 10
    b = (10 ** (a / 10)) * 1.35 + 3
    return math.ceil(b)


count = 0
sum = 0
while True:
    count += 1
    rs = input(f"一秒内的第{count}个有效值，输入有效的RSRP值：")
    if rs.upper() == 'Q':
        break
    aa = (rsrp(rs))
    print(f"转化完后的值为：{aa}")
    sum += aa
    print(f"有效值的总和是：{sum}，平均值是:{math.ceil(sum / count)}")
