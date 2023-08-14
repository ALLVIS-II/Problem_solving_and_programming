import random 
def generate_lotto_number():
    num = []
    for _ in range(7):
        random_digit = random.randint(0, 9)
        num.append(random_digit)
    return num

print(f"generated lotto number: {generate_lotto_number()}")