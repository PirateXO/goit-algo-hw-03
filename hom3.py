from datetime import datetime, date

def get_days_from_today(date_str):
    try:
        
        input_date = datetime.strptime(date_str, '%Y-%m-%d').date()
        
        current_date = date.today()
    
        delta = current_date - input_date
      
        return delta.days
    except ValueError as e:
       
        return str(e)

date_string = input("Введіть дату форматі 'YYYY-MM-DD': ")
days_difference = get_days_from_today(date_string)
print(f"Days from {date_string} to today: {days_difference}")
