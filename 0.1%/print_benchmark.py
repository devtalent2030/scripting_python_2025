
"""print_benchmark.py
Benchmark different ways of calling print-like functions to measure
the overhead of LOAD_GLOBAL vs. LOAD_FAST look‑ups.

Run with:
    python print_benchmark.py
"""

import timeit, dis, sys, io

# ------------------------------------------------------------
# Helper: silent replacement for print to avoid I/O noise
# ------------------------------------------------------------
def silent_print(*args, **kwargs):
    pass

# ------------------------------------------------------------
# 1) Plain call: uses LOAD_GLOBAL print
# ------------------------------------------------------------
def say_hi():
    silent_print("Hi")

# ------------------------------------------------------------
# 2) Alias inside the function: p = print
#    still incurs one LOAD_GLOBAL per call
# ------------------------------------------------------------
def say_hi_store():
    p = silent_print
    p("Hi")

# ------------------------------------------------------------
# 3) Default‑argument alias: _p=print
#    resolved at *function definition* time; only LOAD_FAST each call
# ------------------------------------------------------------
def say_hi_default(_p=silent_print):
    _p("Hi")

# ------------------------------------------------------------
# 4) Module‑level alias: pre‑bind name at module scope
#    also LOAD_GLOBAL, but no dictionary hash (uses LOAD_GLOBAL 'p')
# ------------------------------------------------------------
p = silent_print
def say_hi_global_alias():
    p("Hi")

variants = {
    "say_hi": say_hi,
    "say_hi_store": say_hi_store,
    "say_hi_default": say_hi_default,
    "say_hi_global_alias": say_hi_global_alias,
}

def disassemble():
    print("="*52)
    print("Byte‑code listing")
    print("="*52)
    for name, func in variants.items():
        print(f"\n{name}:")
        dis.dis(func)

def benchmark(loops=1_000_000):
    print("\n" + "="*52)
    print(f"Timing each variant for {loops:,} calls")
    print("="*52)
    results = {}
    for name, func in variants.items():
        t = timeit.timeit(func, number=loops)
        rps = loops / t
        results[name] = (t, rps)
        print(f"{name:20} {t:10.6f} sec  |  {rps:,.0f} calls/sec")
    return results

if __name__ == "__main__":
    disassemble()
    benchmark()
