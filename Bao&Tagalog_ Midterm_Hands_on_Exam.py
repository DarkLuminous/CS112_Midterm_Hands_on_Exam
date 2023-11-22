import random
while True:
    add1 = (random.randrange(1, 99))
    add2 = (random.randrange(1, 99))

    print(f"what is {add1} + {add2}")
    add = int(input(f"{add1} + {add2} = "))
    addE = add1 + add2
    if add == addE:
        print("Your answer is correct!")
    else:
        print("Your answer is incorrect!")
        print(f"The answer is {addE}")

    min1 = (random.randrange(1, 99))
    min2 = (random.randrange(1, 99))

    print(f"what is {min1} - {min2}")
    min = int(input(f"{min1} - {min2} = "))
    minE = min1 - min2
    if min == minE:
        print("Your answer is correct!")
    else:
        print("Your answer is incorrect!")
        print(f"The answer is {minE}")

    mult1 = (random.randrange(1, 99))
    mult2 = (random.randrange(1, 99))

    print(f"what is {mult1} x {mult2}")
    mult = int(input(f"{mult1} x {mult2} = "))
    multE = mult1 * mult2
    if mult == multE:
        print("Your answer is correct!")
    else:
        print("Your answer is incorrect!")
        print(f"The answer is {multE}")

    div1 = (random.randrange(1, 99))
    div2 = (random.randrange(1, 99))

    print(f"what is {div1} / {div2}")
    div = int(input(f"{div1} / {div2} = "))
    divE = div1 / div2
    if div == divE:
        print("Your answer is correct!")
    else:
        print("Your answer is incorrect!")
        print(f"The answer is {divE}")

