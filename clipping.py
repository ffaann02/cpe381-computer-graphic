class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

min_window = input("X_min Y_min: ").split()
max_window = input("X_max Y_max: ").split()

x_min, y_min = int(min_window[0]), int(min_window[1])
x_max, y_max = int(max_window[0]), int(max_window[1])

def get_m(x1, y1, x2, y2):
    # y = mx + p
    m = (y2 - y1) / (x2 - x1)
    return m

def get_p(m, x, y):
    return y - m * x

def get_intersection_point(x, y, m, p):
    intersection_point = Point(0, 0)
    if x < x_min and y_min < y < y_max:
        intersection_point.x = x_min
        intersection_point.y = m * x_min + p
    
    elif x > x_max and y_min < y < y_max:
        intersection_point.x = x_max
        intersection_point.y = m * x_max + p

    elif y < y_min and x_min < x < x_max:
        intersection_point.x = (y_min - p) / m
        intersection_point.y = y_min
    
    elif y > y_max and x_min < x < x_max:
        intersection_point.x = (y_max - p) / m
        intersection_point.y = y_max

    return intersection_point
    
while 1:
    point1 = input("Point 1: ").split()
    if point1[0] == "-":
        break
    point2 = input("Point 2: ").split()
    if point2[0] == "-":
        break
    else:
        x1, y1 = int(point1[0]), int(point1[1])
        x2, y2 = int(point2[0]), int(point2[1])
        m = get_m(x1, y1, x2, y2)
        print(f"Slope: {m:.2f}")
        p = get_p(m, x1, y1)
        point1_intersection = get_intersection_point(x1, y1, m, p)
        point2_intersection = get_intersection_point(x2, y2, m, p)
        print(f"Intersection point 1: ({point1_intersection.x:.2f}, {point1_intersection.y:.2f})")
        print(f"Intersection point 2: ({point2_intersection.x:.2f}, {point2_intersection.y:.2f})")