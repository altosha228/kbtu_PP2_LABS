class myGenerator:
    def __init__(self, N):
        self.start = 0
        self.end = N

    def __iter__(self):
        return self

    def __next__(self):
        while self.start < self.end:
            if self.start % 12 == 0:
                num = self.start
                self.start += 12  # Move to the next multiple of 12
                return num
            self.start += 1  # Ensure we move forward
        raise StopIteration


def divisibleBy3and4():
    myClass = myGenerator(100)
    myIter = iter(myClass)
    listOfGenerator = [str(item) for item in myIter]
    print(", ".join(listOfGenerator))


divisibleBy3and4()
