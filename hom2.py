import random

def get_numbers_ticket(min, max, quantity):
    if min < 1 or max > 1000 or quantity > (max - min + 1):
        return []
    
    numbers = random.sample(range(min, max + 1), quantity)
    numbers.sort()
    
    return numbers

min_num = int(input("Введіть мінімальне число: "))
max_num = int(input("Введіть максимальне число: "))
quantity = int(input("Введіть кількість чисел: "))

ticket_numbers = get_numbers_ticket(min_num, max_num, quantity)

if ticket_numbers:
    print(f"Згенеровані номери квитків: {ticket_numbers}")
else:
    print("Невірні вхідні параметри.")