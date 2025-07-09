"""
Name: Talent Nyota
Date: 22-05-2025
Program Description: 
This script Simulates a cloud provisioning system that checks if requested
resources (CPU and memory) can be provisioned based on current system limits.
"""

# Constants (total available resources)
TOTAL_CPU_CORES = 24
TOTAL_MEMORY = 256.0

# Default remaining resources (initially all available)
remaining_available_cpu = TOTAL_CPU_CORES
remaining_available_memory = TOTAL_MEMORY

try:
    # Get user input
    cpu_cores = int(input("Please enter the number of required CPU cores: "))
    memory = float(input("Please enter the amount of required memory in GB: "))

    # Validation for negative numbers
    if cpu_cores < 0 or memory < 0:
        print("Please enter positive values only.")
    # Provisioning check
    elif cpu_cores <= TOTAL_CPU_CORES and memory <= TOTAL_MEMORY:
        print("Resources provisioned successfully.")
        # Update remaining resources
        remaining_available_cpu -= cpu_cores
        remaining_available_memory -= memory
    else:
        print("Resource request exceeds capacity. Provisioning failed.")

except ValueError:
    print("Invalid input. Please enter numeric values only.")

# Always display remaining resources  even if provisioning failed
print(f"\n Total remaining available CPU cores: {remaining_available_cpu}")
print(f" Total remaining available memory: {remaining_available_memory:.2f} GB")
