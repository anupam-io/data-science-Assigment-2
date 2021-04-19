import hashlib


def hash(element, range):
    return int(hashlib.sha256(str(element).encode('ASCII')).hexdigest(), 16) % range


class count_min_sketch:
    def __init__(self, depth, width):
        super().__init__()
        self.depth = depth
        self.width = width
        self.data = [[0]*self.width]*self.depth

    def add(self, element, c=1):
        for i in range(self.depth):
            position = int(hashlib.sha256(
                str(i*element).encode('ASCII')).hexdigest(), 16) % self.width
            self.data[i][position] += c

    def query(self, element):
        min_val = 10**10
        for i in range(self.depth):
            position = hash(i*element, self.width)
            min_val = min(min_val, self.data[i][position])
        return min_val


# obj = count_min_sketch(5, 100)
# obj.add(51)
# obj.add(51)
# obj.add(51)
# obj.add(52)

# print(obj.query(51))
# print(obj.query(52))
