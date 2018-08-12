class Base:
    def __init__(self, pair_count):
        self.count = pair_count  # 分量数，即整体块数
        self.id = [x for x in range(self.count)]

    def union(self, p, q):
        pass

    # 所在分量的标识符
    def find(self, p):
        pass

    def connected(self, p, q):
        return self.find(p) == self.find(q)


if __name__ == '__main__':
    uf = Base(10)
    print(uf.count)
