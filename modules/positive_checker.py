def positive_checker(prompt):
    while int(prompt) < 1:
        prompt = int(input(f"Please enter a positive Number: "))
    
    return prompt

def zero_checker(prompt):
    while prompt < 0:
        prompt = int(input(f"Please enter at least 0: "))
    
    return prompt