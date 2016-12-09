'''
Computer 1.
Receives requests from load balancer and reaches out to the database for assistance
'''
import database as db
# import cache as c
from memcache import Memcache

CACHE = Memcache()

def get_name():
    '''
    return name of server
    '''
    return 'computer 1'

def multiply_handler(first_number, second_number):
    '''
    receives requests from the user
    and then checks the cache for the request
    '''
    cache_key = (first_number, second_number)
    if CACHE.check(cache_key):
        solution = CACHE.get(cache_key)
    else:
        solution = db.russian(first_number, second_number)
        CACHE.add(cache_key, solution)
    return 'The result of {} is {}'.format(cache_key, solution)

