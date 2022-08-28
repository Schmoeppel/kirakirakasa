class test_class:

    def __init__(self):
        self.list = [{"A": [1,2,3]}, {"A": [4,5,6]}]

a = test_class()

a.list[1]["A"].append(4)

print(a.list)