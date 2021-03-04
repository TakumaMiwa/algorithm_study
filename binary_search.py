from typing import Any, Sequence

class BinarySearch:
    def __init__(self, array: Sequence) -> None:
        self.array = array

    def sort_array(self) -> None:
        self.array.sort()

    def get_num(self, num: Any) -> bool:
        pl = 0
        pr = len(self.array) - 1

        while True:
            pc = (pl + pr) // 2
            if self.array[pc]==num:
                return True
            elif self.array[pc]<num:
                pl = pc + 1
            else:
                pr = pc - 1
            if pl>pr:
                return False

if __name__ == '__main__':

    N = int(input())
    array = [None] * N
    for i in range(N):
        array[i] = int(input(f'array[{i}]: '))
    num = int(input('serch for: '))
    binary_search = BinarySearch(array)
    binary_search.sort_array()
    if binary_search.get_num(num):
        print("Exist.")
    else:
        print("Not exist.")