from math import atan, cos, tan
import sys
H, V = map(float, sys.stdin.readline().rstrip().split())

theta = atan(V/H) / 2
newH = H / cos(theta) / 2
newV = (V - H * tan(theta)) * cos(theta)

print(f'{newH:.2f} {newV:.2f}')
