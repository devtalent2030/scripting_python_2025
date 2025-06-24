import sys, textwrap

print("Total built-ins:", len(sys.builtin_module_names))
print(textwrap.fill(", ".join(sorted(sys.builtin_module_names)), width=80))

# Peek at a few attributes
import builtins, _io, _thread, gc
print("Example built-in func:", builtins.len)
print("Type of sys.stdout :", type(sys.stdout))
print("GC thresholds:", gc.get_threshold())
