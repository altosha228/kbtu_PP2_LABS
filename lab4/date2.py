from datetime import datetime


date1 = datetime(2024, 2, 10, 12, 30, 45)  
date2 = datetime(2024, 2, 12, 14, 45, 30)  


difference = date2 - date1


seconds_diff = difference.total_seconds()

print(f"Difference in seconds: {seconds_diff}")
