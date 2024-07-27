file = open("input1.txt")
n, t, s = [int(number) for number in next(file).split()]

vel = {}
max_vel = 0
cars = []
index = 0

for i, v in enumerate(next(file).split()):
    v = int(v)
    cars.append([v, 0])


def distance(v):
    return (v * t) / s
    

max_circles = (cars[0][0] * t) / s

result = 0

for i, car in enumerate(cars):
    if i == 0:
        continue

    if car[0] > cars[0][0]:
        continue

    v, x = car
    sub_circles = distance(v)
    diff = (int(max_circles) - int(sub_circles))
    if max_circles % 1 <= sub_circles % 1:
        diff -= 1
    result += int(diff)


print(result)











