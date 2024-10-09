import math

start = (127, 63.5)
end = (254, 127)

a = abs(end[0]-start[0])
b = abs(end[1]-start[1])

r = math.sqrt(a**2+b**2)
print(r)

radian = math.atan(b/a)

print(math.degrees(radian))