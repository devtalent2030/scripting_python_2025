


"""

class Pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        

dog = Pet("buddy", "rex")
cat = Pet("buddy", True )


print(dog.name, dog.species)
print(cat.name, cat.species)

"""


# Author:   
# Created:  October 6, 2023
# Modified: October 27, 2023
# Description:
# As an experimentation with object-oriented Python and Python's interactions with
# JSON, this has been modified repeatedly. This poorly-documented file includes a
# class definition for an Ec2Instance class, and will attempt to import a file
# containing EC2 instances.
# As of right now, it does NOT attempt to convert the JSON file's content INTO
# EC2 instances. This may or may not be necessary for the student!
# If you instead prefer to destroy the class entirely or design it differently,
# that is okay.

import json

class Ec2Instance:
    def __init__(self, name_value, vcpu_value, memory_value, storage_value, bandwidth_value, availability_value):
        self.name = name_value
        self.vcpu = vcpu_value
        self.memory = memory_value
        self.storage = storage_value
        self.bandwidth = bandwidth_value
        self.availability = availability_value

    def display(self):
        return self.name + " (" + str(self.vcpu) + " vCPUs, " + str(self.memory) + "GiB memory, " + self.storage + " storage)"

    def __str__(self) -> str:        
        return self.name
    
    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, indent=4)
    
# Open the file. Unless changed, this will try to find the file in the current working directory.
filename = "ec2_instance_types.json"
file = open(filename, "r")
# Load the contents of the file as JSON.
ec2_instances = json.load(file)

# This will print the first, singular EC2 instance from the file.
print(ec2_instances[0])

# This will go through each instance and read just the "name" attribute of each one.
for instance in ec2_instances:
    print(instance["name"])

# print("\nInstances Converted to Strings:")
# for instance in ec2_instance_list:
#     print(instance)

# print("\nInstances Using display() Method:")
# for instance in ec2_instance_list:
#     print(instance.display())

# print("\nInstances Shown Using Properties:")
# for instance in ec2_instance_list:
#     print(instance.name, "\t", instance.vcpu, "\t", instance.memory)

# print("\nInstances Shown as JSON:")
# for instance in ec2_instance_list:
#     print(instance.to_json())

