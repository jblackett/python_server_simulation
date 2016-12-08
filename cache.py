'''
cache of used numbers
'''

CACHE = {}

def check(key):
    '''
    check to see if provided key exists in CACHE
    '''
    print('checking cache')
    if key in CACHE:
        print('request is in cache')
        return True
    else:
        return False
def get(key):
    '''
    get data from cache associated with key
    '''
    print('retrieving data from cache')
    return CACHE[key]
def put(key, data):
    '''
    put data into cache
    '''
    print('storing data in cache')
    CACHE[key] = data

