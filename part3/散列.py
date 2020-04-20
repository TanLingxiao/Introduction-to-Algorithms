class hashMap(object):
    def __init__(self, n):
        self.len = n
        self.maps = [0]*n

    def find_map(self, k):
        index = hash(k) % self.len
        return index

    def add(self, k, v):
        index = self.find_map(k)
        self.maps[index] = v

    def get(self, k):
        index = self.find_map(k)
        return self.maps[index]


if __name__ == '__main__':
    h = hashMap(10)
    h.add('a', 56)
    h.add('b', 45)
    h.get('a')