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
    def random_list(cls, length, range_, max_count=0):
        limited = False if max_count == 0 else True

        n = 0
        while True:
            result = [random.randint(0, range_ - 1) for x in range(length)]

            if n >= max_count and limited:
                return
            else:
                n += 1
                yield result


if __name__ == '__main__':
    g = Generator.random_list(3, 10)
    for i in g:
        print(i)
