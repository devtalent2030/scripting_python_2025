import dis
import builtins
x = len("hello")
dis.dis("x = len('hello')")
print(f"len: id={id(builtins.len)}, type={type(builtins.len)}")