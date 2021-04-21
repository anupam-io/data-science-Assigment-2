from random import randint, shuffle, seed

# Misra-Gries sketch


class misra_gries:
    def __init__(self, k):
        super().__init__()
        assert(k > 0)
        self.k = k
        self.data = [[-1, -1]]*k

    def add(self, element, c=1):
        # Case 1: Finding the element in stored self.data
        for i in range(0, self.k):
            if self.data[i][0] != -1 and self.data[i][0] == element:
                self.data[i][1] += 1
                return

        # Case 2: Storing the element as new item
        for i in range(0, self.k):
            if self.data[i][0] == -1:
                self.data[i] = [element, 1]
                return

        # Case 3: Dropping frequency of each element & removing the ones with 0
        for i in range(0, self.k):
            self.data[i][1] -= 1
            if self.data[i][1] == 0:
                self.data[i][0] = -1

    def query(self, element):
        for i in self.data:
            if i[0] == element:
                return i[1]
        return 0


# Running with simple self.data
# n = 100
# k = 3
# arr = []

# seed(0)
# for _ in range(80):
#     arr.append(randint(1, 3))
# for _ in range(20):
#     arr.append(randint(1, 100))

# shuffle(arr)

# print("target array:", arr)
# print("misra-gries output:", misra_gries().fit(arr, k))
