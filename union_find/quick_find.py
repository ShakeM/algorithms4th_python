from union_find.base import Base
from union_find.generator import Generator
from union_find.clocker import cal_time


class QuickFind(Base):
    def union(self, p, q):
        p_block = self.find(p)
        q_block = self.find(q)

        if p_block == q_block:
            return
        else:
            for index, block in enumerate(self.id):
                if block == q_block:
                    self.id[index] = p_block
            self.count -= 1

    def find(self, p):
        return self.id[p]


def union_test():
    @cal_time
    def union(pair_count, union_times):
        uf = QuickFind(pair_count)

        pairs = Generator.pair(union_times, pair_count)
        for p in pairs:
            uf.union(p[0], p[1])

    print('=' * 20 + 'Union测试' + '=' * 20)

    print('Union 千次，十万级数据规模')
    union(100000, 1000)  # 运行耗时：6.506794663813551
    print('Union 千次，百万级数据规模')
    union(1000000, 1000)  # 运行耗时：66.00502315467021

    print('=' * 40)


def find_test():
    @cal_time
    def find(pair_count, find_times):
        uf = QuickFind(pair_count)
        pairs = Generator.pair(find_times, pair_count)
        for p in pairs:
            uf.find(p[0])

    print('=' * 20 + 'Find测试' + '=' * 20)
    print('Find 千次，百万级数据规模')
    find(1000000, 1000)  # 运行耗时：0.09202817782488838
    print('Find 千次，亿级数据规模')
    find(100000000, 1000)  # 运行耗时：9.736806926914154
    print('=' * 40)


if __name__ == '__main__':
    union_test()
    find_test()
