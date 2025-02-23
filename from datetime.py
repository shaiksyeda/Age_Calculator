from datetime import datetime

def calculate_age(dob):
    # Get today's date
    today = datetime.today()
    
    # Convert DOB string to a datetime object
    dob = datetime.strptime(dob, '%Y-%m-%d')
    
    # Calculate the difference between today and DOB
    age_in_days = (today - dob).days
    age_in_years = age_in_days // 365  # Approximate age in years
    age_in_hours = age_in_days * 24  # Total hours
    age_in_minutes = age_in_hours * 60  # Total minutes
    age_in_seconds = age_in_minutes * 60  # Total seconds
    
    return age_in_years, age_in_hours, age_in_minutes, age_in_seconds

# Input your DOB in YYYY-MM-DD format
dob_input = input("Enter your date of birth (YYYY-MM-DD): ")

years, hours, minutes, seconds = calculate_age(dob_input)

print(f"You are {years} years, {hours} hours, {minutes} minutes, and {seconds} seconds old.")
