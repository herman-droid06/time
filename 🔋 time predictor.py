from datetime import datetime, timedelta
print("    \033[36m    ================================================")
print(".         \033[93m                  THE HERMAN CORP. LTD\033[0m")
print(".   \033[97m               72V BATTERY TIME CHARGING PREDICTOR")
print("       \033[36m ================================================\033[0m \033[97m")
percent = float(input("Current Battery \033[32m% \033[0m:\033[35m \033[0m"))

# Constants
full_time = 240  # minutes for full charge

# Calculate remaining percentage
remaining_percent = 100 - percent

# Minutes left
minutes_left = (remaining_percent / 100) * full_time

# Get current time
now = datetime.now()

# Add remaining time
full_charge_time = now + timedelta(minutes=minutes_left)

# Output
print(f"\n {minutes_left:.2f} minutes left")
print(" Battery will be full at:", full_charge_time.strftime("%H:%M:%S"))