'''
memcache module
'''
# pylint: disable=C0111

class Memcache():
    def __init__(self):
        self.cache = {}

    def set(self, key, value):
        self.cache[key] = value
        return True

    def get(self, key):
        return self.cache.get(key)

    def delete(self, key):
        if key in self.cache:
            del self.cache[key]

    def flush(self):
        self.cache.clear()

def test_memcache():
    mem = Memcache()
    print(mem.set('a', '1'))
    print(mem.set('b', '2'))
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
