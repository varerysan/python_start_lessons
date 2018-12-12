class PrintNumbers:
    def __init__(self, num):
        self._num = num

    def __call__(self):
        for n in range(self._num):
            print(n)


p = PrintNumbers(5)

p()

