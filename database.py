'''
this is the database
it simulates fetching of data by running the russian algorithm requests
'''
def russian(integer_a, integer_b):
    '''
    multiplies two integer parameters
    '''
    print('running russian peasants algorithm')
    first_number = integer_a
    second_number = integer_b
    solution = 0
    while first_number > 0:
        if first_number % 2 != 0:
            solution += second_number
        second_number = second_number << 1
        first_number = first_number >> 1
    return solution
