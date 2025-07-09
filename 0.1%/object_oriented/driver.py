import sys, inspect

print("Importing toy_module …\n")
import toy_module                      # executes the file above

print("\n### After import")
mod = sys.modules["toy_module"]        # the singleton module object

print("type(mod) :", type(mod))        # <class 'module'>
print("mod.__name__  :", mod.__name__)
print("mod.__file__  :", mod.__file__)
print("inspect.getfile(mod) :", inspect.getfile(mod))
print("sys.modules keys … contains 'toy_module'? ->", 'toy_module' in sys.modules)




