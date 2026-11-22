DAYS_IN_WEEK: int = 7

day: int = int(input("Day: "))

days_to_wait: int=  int(input("days to wait: "))

delivery_day = day + days_to_wait

if delivery_day > DAYS_IN_WEEK:
    delivery_day -= DAYS_IN_WEEK

print("delivery Day: ",delivery_day)

assert 1 <= delivery_day <= 7