min_window = input().split()
max_window = input().split()

x_min, y_min, x_max, y_max = int(min_window[0]), int(min_window[1]), int(max_window[0]), int(max_window[1])

def get_m(x1, y1, x2, y2):
    # y = mx + p
    m = (y2 - y1) / (x2 - x1)

    return m

def get_p(m, x = None, y = None):
    return y - m * x

def get_boundary_x(x_min, m, p):
    return int(x_min), int(m * x_min + p)

def get_boundary_y(y_max, m, p):
    return int((y_max - p) / m), int(y_max)

A = input().split()
B = input().split()

m = get_m(int(A[0]), int(A[1]), int(B[0]), int(B[1]))
print(f"slope: {m:.2f}")

x1, y1 = int(A[0]), int(A[1])
x2, y2 = int(B[0]), int(B[1])

p1 = get_p(m, x1, y1)
p2 = get_p(m, x2, y2)

print(get_boundary_x(x_min, m, p1), get_boundary_y(y_max, m, p1))