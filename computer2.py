'''
Computer 2.
Receives requests from load balancer and reaches out to the database for assistance
'''
import database as db
import cache as c

def get_name():
    '''
    return name of server
    '''
    return 'computer 2'

def multiply_handler(first_number, second_number):
    '''
    receives requests from the user
    and then checks the cache for the request
    '''
    cache_key = (first_number, second_number)
    if c.check(cache_key):
        solution = c.get(cache_key)
    else:
        solution = db.russian(first_number, second_number)
        c.put(cache_key, solution)
    return 'The result of {} is {}'.format(cache_key, solution)
