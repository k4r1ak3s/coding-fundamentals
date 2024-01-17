
def calculate(amount, percent): 
    return (amount * percent) / 100
  
def calculate_income_tax(total_income:  
                         float) -> float: 
  
    if total_income <= 11850: 
        return 0
    elif total_income <= 34500: 
        return calculate(total_income - 
                         11850, 20) 
    elif total_income <= 149999:
        personal = total_income - 11850
        first_20 = calculate(34501, 20)
        second_40 = calculate(personal - 34501, 40)

        return first_20 + second_40
    elif total_income >= 150000: 
        personal = total_income - 11850
        first_20 = calculate(34501, 20)
        second_40 = calculate(personal - 34501, 40)
        third_45 = calculate(personal - 150000, 45)
        return first_20 + second_40 + third_45
    else: 
        return "Enter a valid number"
  
  
if __name__ == '__main__': 
    total_income = float(input("What's your annual income?\n>>> ")) 
    tax = calculate_income_tax(total_income) 
    print(f"Total tax applicable at £{total_income} is £{tax}") 