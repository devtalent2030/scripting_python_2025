cores_allocated = 6
memory_allocated_gb = 27.5
monthly_cost_per_core = 0.25
monthly_cost_per_gb = 0.1

months_active = 11

discount = 0

if months_active > 12:
    discount += 0.1
elif months_active > 6:
    discount += 0.05

total_owed = cores_allocated * monthly_cost_per_core
total_owed += memory_allocated_gb * monthly_cost_per_gb
total_owed = total_owed - (total_owed * discount)

print(total_owed)