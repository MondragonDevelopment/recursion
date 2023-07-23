def countUpandDown(number):
    print(number)
    if number >= 30:
        print('Reached the base case')
        return
    else:
        countUpandDown(number + 1)
        print(number, 'returning')
        return


countUpandDown(0)
