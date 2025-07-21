with open('input.txt', 'r') as f:
    a, b, c = map(int, f.readline().split())
d = b**2 - 4*a*c
if d >= 0:
    root1 = (-b + d**0.5) / (2*a)
    root2 = (-b - d**0.5) / (2*a)
    print("Roots are:", root1, "and", root2)
else:
    print("No real roots")