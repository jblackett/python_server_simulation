'''
memcache module
'''
# pylint: disable=C0111

MEMORY = {}

class Memcache():
    def __init__(self):
        global MEMORY
        self.cache = MEMORY

    def add(self, key, value):
        print('storing data in cache')
        self.cache[key] = value
        return True

    def get(self, key):
        print('retrieving data from cache')
        return self.cache.get(key)

    def delete(self, key):
        if key in self.cache:
            del self.cache[key]

    def flush(self):
        self.cache.clear()

    def check(self, key):
        if key in self.cache:
            print('request is in cache')
            return True
        else:
            return False

def test_memcache():
    mem = Memcache()
    print(mem.add('a', '1'))
    print(mem.add('b', '2'))
    print(mem.cache)
    print(mem.get('a'))
    print(mem.get('b'))
    print(mem.get('c'))
    mem.delete('b')
    mem.delete('c')
    print(mem.cache)
    mem.flush()
    print(mem.cache)

if __name__ == '__main__':
    test_memcache()
