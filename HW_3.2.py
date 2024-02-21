import random

def get_numbers_ticket(min, max, quantity):
    quantity = int(quantity)
    value_ticket = []

    while len(value_ticket) < quantity:
        num = random.randint(min, max)
        if num not in value_ticket:
            value_ticket.append(num)

    return value_ticket

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)