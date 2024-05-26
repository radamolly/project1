def calculate_ferry_fare(num_adults, num_children, is_foreigner=False, is_night=False, is_tour_group=False):
    ADULTS_PRICE = 100

    child_price = num_adults*(ADULTS_PRICE/2)
    adult_price = num_adults * ADULTS_PRICE

    if is_foreigner:
        child_price = child_price + (child_price* 50/100)
        adult_price = adult_price + (adult_price*50/100)

    if is_night:
        child_price = child_price + (child_price* 20/100)
        adult_price = adult_price + (adult_price*20/100)

    if is_tour_group:
        tourist = num_adults + num_children
        if tourist >= 10:
            child_price = child_price - (child_price* 10/100)
            adult_price = adult_price - (adult_price*10/100)

    fair = child_price + adult_price
    return fair

total_fare = calculate_ferry_fare(num_adults=10, num_children=5, is_foreigner=True, is_night=True, is_tour_group=True)
print("The total price is", total_fare)