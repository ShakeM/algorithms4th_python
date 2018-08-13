from union_find.base import Base
from utils.generator import Generator
from utils.clocker import cal_time


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


if __name__ == '__main__':
    def union_test():
        @cal_time
        def union(count, union_times):
            uf = QuickFind(count)

            pairs = Generator.random_list(2, count, union_times)
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
        def find(count, find_times):
            uf = QuickFind(count)
            for p in range(find_times):
                uf.find(p)

        print('=' * 20 + 'Find测试' + '=' * 20)
        print('Find 千次，百万级数据规模')
        find(1000000, 1000)  # 运行耗时：0.09202817782488838
        print('Find 千次，亿级数据规模')
        find(100000000, 1000)  # 运行耗时：9.736806926914154
        print('=' * 40)


    union_test()
    find_test()
