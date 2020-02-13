class EvenIterator:

    def __init__(self, lst):
        self.lst = lst
        self.elem = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.elem < len(self.lst):
            self.elem += 2
            return self.lst[self.elem - 2]
        else:
            raise StopIteration


for x in EvenIterator([6, 1, 0, 8, 5, 13, 24]):
    print(x)
