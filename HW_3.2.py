import random

def get_numbers_ticket(min, max, quantity):
    if min < 1 or max > 1000 or quantity < 1 or quantity > (max - min):
        return []
    
    numbers = random.sample(range(min, max), quantity)
    return sorted(numbers)


print(get_numbers_ticket(1, 49, 6))
