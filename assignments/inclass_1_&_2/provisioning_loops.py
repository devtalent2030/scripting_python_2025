"""
Name: Talent Nyota
Date: 22-05-2025
Program Description:
This script simulates a cloud provisioning system that supports multiple resource requests.
Each user submits a request for CPU cores and memory. The system checks if it can grant the request
based on the remaining capacity. Allocated and failed requests are both recorded and shown at the end.
"""


# These are the total available resources your "cloud" can provide.
TOTAL_CPU_CORES = 24           # total virtual cores 
TOTAL_MEMORY = 256.0           # total RAM in GB 


# We need to track what’s already been given away so we know what’s left.
used_cpu = 0                   # running total of cores that have been allocated
used_memory = 0.0              # running total of memory allocated


# We’ll use lists to store accepted and rejected requests.
allocated_resources = []       # this will store each successful request (username, cores, memory)
pending_requests = []          # this will store failed requests that exceeded capacity


# This infinite loop will continue accepting requests until the user types 'no'.
while True:
    print("\n=== New Request ===")
    
    # Identify the user 
    username = input("Enter your username: ")

    try:
        # Ask how many CPU cores the user needs — must be an integer.
        requested_cores = int(input("Enter number of required CPU cores: "))
        
        # Ask how much memory they need — can be a decimal (float).
        requested_memory = float(input("Enter amount of required memory (GB): "))

        # input validation
        if requested_cores < 0 or requested_memory < 0:
            print("Negative values are not allowed. Try again.")
            continue  # send the user back to the top of the loop

        # Check if system has enough to allocate 
        if (used_cpu + requested_cores <= TOTAL_CPU_CORES) and \
           (used_memory + requested_memory <= TOTAL_MEMORY):
            # The request fits — provision it
            allocated_resources.append([username, requested_cores, requested_memory]) 
            used_cpu += requested_cores
            used_memory += requested_memory
            print("Resources provisioned successfully.")
        else:
            # Not enough capacity — record it in pending
            pending_requests.append([username, requested_cores, requested_memory])
            print("  Not enough resources. Request added to pending.")

    except ValueError:
        # User typed letters instead of numbers — keep the system from crashing
        print(" Invalid input. Please enter numeric values only.")
        continue

    # Check if the user wants to continue 
    another = input("Would you like to make another request? (yes/no): ").lower()
    if another != "yes":
        break  # exit the loop


print("\n\n=== Allocation Summary ===")

# Display all approved (allocated) requests
print("\nAllocated Resources:")
for request in allocated_resources:
    print(f"User: {request[0]:<10} CPU cores: {request[1]:<3} Memory (GB): {request[2]:.1f}")

# Display all rejected (pending) requests
print("\nPending Requests:")
for request in pending_requests:
    print(f"User: {request[0]:<10} CPU cores: {request[1]:<3} Memory (GB): {request[2]:.1f}")
