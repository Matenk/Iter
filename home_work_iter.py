class EvenNumbers:
    def __init__(self, start, end):
        self.start = start
        self.end = end


    def __iter__(self):
        return self


    def __next__(self):
        self.start += 2

        if self.start <= self.end+2:

            return self.start - 2
        else:
            raise StopIteration





en = EvenNumbers(10, 25)
for j in en:
    print(j)