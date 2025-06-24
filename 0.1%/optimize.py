import dis
print("Slow loop:")
dis.dis("total = 0; for i in range(5): total += i")
print("\nFast sum:")
dis.dis("total = sum(range(5))")





"""
Interview-Ready Phrases

“Python’s compiler folds 3 + 2 into LOAD_CONST 5, optimizing runtime by skipping BINARY_OP, as I saw in my bytecode tests.”

“Bytecode like STORE_NAME binds names globally, but STORE_FAST is faster for locals, critical for Meta’s high-performance pipelines.”

“Understanding bytecode helps optimize Meta’s data processing by minimizing operations, like using sum over + loops.”

“In ceval.c, BINARY_OP calls int.__add__, but folding constants in peephole.c saves cycles, as I explored with dis.dis.”

"""