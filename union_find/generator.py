import random


class Generator:
    @classmethod
    def generate(cls, range_):
        while True:
            num1 = random.randint(0, range_ - 1)
            num2 = random.randint(0, range_ - 1)
            pair = (num1, num2)
            yield pair

    @classmethod
    def pair(cls, count, range_):
        for i in range(count):
            num1 = random.randint(0, range_ - 1)
            num2 = random.randint(0, range_ - 1)
            pair = (num1, num2)
            yield pair


if __name__ == '__main__':
    pair = Generator.generate(2)
    print(next(pair))
