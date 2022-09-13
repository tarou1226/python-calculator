from functools import reduce
import fire

class Calculator(int):

    # 足し算機能の追加
    def add(self, *args):
        return reduce(lambda x, y: x + y, args)
    # 引き算機能の追加
    def sub(self, *args):
        return reduce(lambda x, y: x - y, args)
    # 掛け算機能の追加
    def mul(self, *args):
        return reduce(lambda x, y: x * y, args)
    # 割り算機能の追加
    def div(self, *args):
        return reduce(lambda x, y: x // y, args)

if __name__ == "__main__":
    # Calculatorを呼び出す
    fire.Fire(Calculator)