

"""
import keyword
print(keyword.kwlist)
# Output: ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

import dis


def discount(subtotal):
    if subtotal >= 100:
        return subtotal * 0.9
    elif subtotal >= 50:
        return subtotal * 0.95
    else:
        return subtotal
dis.dis(discount)
"""



# LAB1 If I create a variable inside an if block that’s inside a function, does Python treat 
# that variable as only belonging to the if block, or does it belong to the whole function?”

import symtable, inspect, textwrap

def foo():
    if True:
        a = 5
    return a

tbl = symtable.symtable(inspect.getsource(foo), "lab1", "exec")
func_scope = tbl.get_children()[0]          # zoom into foo()
print("Lab 1 identifiers:", func_scope.get_identifiers())
# ➞ {'a'}  ← single locals table, proving ‘if’ adds no scope.



""" LAB2
1. Question in plain English
“If I set a variable inside a function but never read it again, can I make Python tell me that I have useless code?”

2. Why we ask
Unused locals often signal bugs or wasted memory.
Professional linters (e.g., flake8, pylint) flag them so your codebase stays clean.
symtable lets us detect that statically (no execution needed).

"""



def bar():
    b = 99      # <-- assigned once
    return 7    # <-- never reads b

tbl        = symtable.symtable(inspect.getsource(bar), "lab2", "exec")
func_scope = tbl.get_children()[0]           # symbol-table node for bar()
sym_b      = func_scope.lookup("b")          # symbol record for 'b'

print("Lab 2 is 'b' referenced?", sym_b.is_referenced())
print("Lab 2 is 'b' assigned?  ", sym_b.is_assigned())






""" LAB3
What’s a free variable?
A name that inner code uses but didn’t assign locally and isn’t global.
Python closes over it via a cell object, so the inner function can still see it later.

"""

def outer():
    secret = 42
    def inner():
        return secret
    return inner()

tbl = symtable.symtable(inspect.getsource(outer), "lab3", "exec")
outer_scope  = tbl.get_children()[0]        # outer()
inner_scope  = outer_scope.get_children()[0]  # inner()
print("Lab 3 inner free vars:", inner_scope.get_frees())
# ➞ ('secret',)




""" LAB4
“When I reference math inside a function, how does Python know it’s the module I 
imported at the top—rather than some undefined global?”
A static-analysis tool (or linter like pylint) must answer that to avoid false “undefined name” errors.
"""

source = textwrap.dedent("""
    import math
    def trig(x):
        return math.sin(x)
""")

tbl = symtable.symtable(source, "lab4", "exec")  # module-level table

module_scope = tbl                             # top level
trig_scope    = module_scope.get_children()[0]  # function trig()

math_mod_sym  = module_scope.lookup("math")     # symbol in module
math_func_sym = trig_scope.lookup("math")       # symbol in function

print("At module level:  imported?", math_mod_sym.is_imported())  # True
print("At module level:  global?  ", math_mod_sym.is_global())    # True

print("Inside trig():   imported?", math_func_sym.is_imported())  # False
print("Inside trig():   global?  ", math_func_sym.is_global())    # True
