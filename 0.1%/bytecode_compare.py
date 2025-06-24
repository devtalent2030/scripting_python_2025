import dis
print("Constant folding:")
dis.dis("x = 3 + 2")

print("\nVariable addition:")
dis.dis("a = 3; b = 2; x = a + b")
a = 3
b = 2
x = a + b
print(f"x: {x}, id={id(x)}")