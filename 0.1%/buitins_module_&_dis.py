import builtins
import dis
import time

# Group built-ins
functions = [name for name in dir(builtins) if isinstance(getattr(builtins, name), type(print)) and not isinstance(getattr(builtins, name), type)]
types = [name for name in dir(builtins) if isinstance(getattr(builtins, name), type)]
exceptions = [name for name in dir(builtins) if isinstance(getattr(builtins, name), type(BaseException))]
others = [name for name in dir(builtins) if not (name in functions or name in types or name in exceptions)]

print("Functions:", sorted(functions))
print("Types:", sorted(types))
print("Exceptions:", sorted(exceptions))
print("Others:", sorted(others))

# Disassemble a function using a built-in
def use_len():
    return len([1, 2, 3])
dis.dis(use_len)

# Performance test
def slow_loop():
    lst = [1, 2, 3]
    for _ in range(1000000):
        len(lst)  # LOAD_GLOBAL
def fast_loop():
    lst = [1, 2, 3]
    l = len  # Copy to local
    for _ in range(1000000):
        l(lst)  # LOAD_FAST

start = time.time()
slow_loop()
print(f"Slow (global): {time.time() - start}")
start = time.time()
fast_loop()
print(f"Fast (local): {time.time() - start}")