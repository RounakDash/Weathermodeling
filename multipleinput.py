with open('mul.txt', 'r') as f:
    lines = f.readlines()
for line in lines:
    a, b, c = map(float, line.strip().split())
    d = b**2 - 4*a*c
    print(f"\nEquation: {a}x² + {b}x + {c} = 0")
    if d >= 0:
        root1 = (-b + d**0.5) / (2*a)
        root2 = (-b - d**0.5) / (2*a)
        print("Roots:", root1, "and", root2)
    else:
        print("No real roots")
