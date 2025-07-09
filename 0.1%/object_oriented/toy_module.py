"""Demonstrate file → module morph (safe version)."""

print("• Inside toy_module.py")

print("  __name__    :", __name__)      # '__main__' when run, 'toy_module' when imported
print("  __file__    :", __file__)      # Absolute path to this .py
print("  __package__ :", __package__)   # '' or None when script, package name when imported

# __spec__ is None when the file is executed as a script (__main__)
if __spec__ is not None:
    print("  __spec__.origin :", __spec__.origin)
else:
    print("  __spec__ is None (running as a script)")
