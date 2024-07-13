xA, yA = map(int, input().split())
xB, yB = map(int, input().split())
xC, yC = map(int, input().split())
s = lambda x1, y1, x2, y2: (x2 - x1) ** 2 + (y2 - y1) ** 2
AB, BC, CA = s(xA, yA, xB, yB), s(xB, yB, xC, yC), s(xC, yC, xA, yA)
print("Yes" if AB + BC == CA or AB + CA == BC or BC + CA == AB else "No")

