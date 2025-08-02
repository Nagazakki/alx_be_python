from datetime import datetime, timedelta

def calculate_future_date(days):
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days)
    return future_date

def main():
    print("Future Date Calculator")

    try:
        days_input = input("Enter the number of days to add to the current date: ")
        days = int(days_input)
        future_date = calculate_future_date(days)
        formatted_date = future_date.strftime('%Y-%m-%d %H:%M:%S')
        print(f"Current date : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Future date (+{days} days): {formatted_date}")
    except ValueError:
        print("Error: Please enter a valid integer for the number of days.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    
if __name__ == "__main__":
    main()