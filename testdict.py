def main():
    cars = {
        "i": 5 ,
        "t": 7,
        "!": 15
    }
    new_cars = {}
    not_cars = {}
    for key, value in cars.items():
        if str(key).isalpha():
            new_cars[key] = value
        else:
            not_cars[key] = value
    for key, value in new_cars.items():

        print(dict(sorted(new_cars.items(), key = lambda x: x[1], reverse=True)))
main()