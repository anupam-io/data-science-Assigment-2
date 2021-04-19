import hashlib


def hash(element, range):
    return int(hashlib.sha256(str(element).encode('ASCII')).hexdigest(), 16) % range


def sgn_hash(element):
    if hash(element, 2) == 0:
        return -1
    else:
        return +1


def median(lst):
    quotient, remainder = divmod(len(lst), 2)
    if remainder:
        return sorted(lst)[quotient]
    return sum(sorted(lst)[quotient - 1:quotient + 1]) / 2


class count_sketch:
    def __init__(self, depth, width):
        super().__init__()
        self.depth = depth
        self.width = width
        self.data = [[0]*self.width]*self.depth

    def add(self, element, c=1):
        for i in range(self.depth):
            position = hash(i*element, self.width)
            self.data[i][position] += c*sgn_hash(i*element)

    def query(self, element):
        min_val = 10**10
        lst = []
        for i in range(self.depth):
            position = hash(i*element, self.width)
            lst.append(self.data[i][position])
        return median(lst)


# obj = count_sketch(5, 100)
# obj.add(51)
# obj.add(51)
# obj.add(51)
# obj.add(52)

# print(obj.query(51))
# print(obj.query(52))
