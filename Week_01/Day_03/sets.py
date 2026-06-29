"""
SETS:
    Learn

        Unique Values
        add()
        remove()
        discard()
"""

numbers = {1,2,3,3,2,1}

print(numbers)

# Set Operations

set_a = {1, 2, 3}
set_b = {3, 4, 5} 

result = set_a.intersection(set_b)
print(result)

result = set_a.intersection(set_b)
print(result)

result = set_a.difference(set_b)
print(result)

result = set_a.symmetric_difference(set_b)
print(result)