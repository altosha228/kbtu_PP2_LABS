from datetime import datetime


now = datetime.now()
precise_hour = now.hour % 12 + now.minute / 60 + now.second / 3600
precise_hour = round(precise_hour, 2)
# print(precise_hour)
current_minute = float(datetime.now().strftime("%M").lstrip("0")) / 5
# print(current_minute)  
