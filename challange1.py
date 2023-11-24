#Converting 12-hour time to 24-hour time

def convert_time(hour, minute, period):
    if period == "pm" and hour != 12:
        hour += 12
    elif period == "am" and hour == 12:
        hour = 0
    return f"{hour:02}{minute:02}"


# Test the function with some examples
print(convert_time(8, 30, "am")) 
print(convert_time(8, 30, "pm")) 
print(convert_time(12, 0, "pm")) 
print(convert_time(12, 0, "am"))
