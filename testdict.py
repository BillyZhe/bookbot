def main():
    cars = [
        {"Car": 5 },
        {"truck": 7},
        {"suv": 15}
    ]
    cars.sort(reverse=True, key= sort_on)
    print(cars)
main()