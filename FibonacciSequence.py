from typing import Any, Union, Generator


class FibIter:
    def __init__(self):
        self.prev = 0
        self.curr = 1

    def __iter__(self):
        return self

    def __next__(self):
        value = self.curr
        self.curr += self.prev
        self.prev = value
        return value

def FibGenerator():
    prev, curr = 0, 1
    while True:
        yield curr
        prev, curr = curr, prev + curr


from itertools import islice
f1 = FibIter()
ls = list(islice(f1,0,10))
print(ls)

f2: Generator[Union[int, Any], Any, None] = FibGenerator()
ls = list(islice(f2,0,20))
print(ls)

print(next(f2))

a = (x*x for x in range(10))
print(sum(a))