"""Homework:
Fibonacci sonlarini iterator orqali chiqarib kelinglar
"""
from colorama import Fore


class FibonacciLogic:
    def __init__(self, count_fib: int):
        self.count_fib = count_fib
        self.count = 0
        self.num_one = 0
        self.num_two = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.count_fib:
            raise StopIteration
        if self.count == 0:
            self.count += 1
            return self.num_one
        elif self.count == 1:
            self.count += 1
            return self.num_two
        else:
            self.num_one, self.num_two = self.num_two, self.num_one + self.num_two
            self.count += 1
            return self.num_two


num_fib_count = int(input(Fore.GREEN + "Enter number of count fibonacci sequence: " + Fore.RESET))
result_fib_with_iterator = FibonacciLogic(num_fib_count)
fib_list = list(result_fib_with_iterator)
print(Fore.GREEN + f"Numbers fibonacci of list with {num_fib_count} count: {fib_list}" + Fore.RESET)

# for fib in fib_list:
#     print(fib)
