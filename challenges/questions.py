from typing import List, Generator
import argparse

def perfect_square_generator(N: int) -> Generator:
    '''
    Write a generator that takes a number N and returns all perfect squares less than N.
    Hint: use yield
    Example 1: N=30 then the generator will give 1, 4, 9, 16, 25 sequentially

    Answer = The statement "less than N" indicates that even if N is a perfect square,
    it shouldn't be returned by the Generator, thus, an if statement is required to 
    increase the range of N in one if its root square is not int.

    Instead of iterating over all range of N, this function focus on only the ints from 1 until N,
    reducing significantly time complexity.
    '''
    N = int(N**(1/2)) if int(N**(1/2)) == N**(1/2) else int(N**(1/2))+1
    for i in range(1,N):
        yield i*i


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('integer', help='Integer N', type=int)

    args = parser.parse_args()
    print([x for x in perfect_square_generator(args.integer)])
