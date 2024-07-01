import re

def normalize_phone(phone_number):
   
    cleaned_number = re.sub(r'[^\d+]', '', phone_number)
    
    if cleaned_number.startswith('380'):
        cleaned_number = '+' + cleaned_number
  
    elif not cleaned_number.startswith('+'):
        cleaned_number = '+38' + cleaned_number
    
    return cleaned_number

user_input = input("Введіть номер телефону: ")
normalized_number = normalize_phone(user_input)
print(f"Нормалізований номер: {normalized_number}")
