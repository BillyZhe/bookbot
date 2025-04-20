def main():
    cars = {
        "i": 5 ,
        "t": 7,
        "!": 15
    }
    new_cars = {}
    order_cars = {}
    for key, value in cars.items():
        if str(key).isalpha():
            new_cars[key] = value
        else:
            order_cars[key] = value
    for key, value in new_cars.items():
        new_cars = dict(sorted(new_cars.items(), key = lambda x: x[1], reverse=True))
    for name in new_cars:
        for number in new_cars[name]:
            print(new_cars[name][number])
main()