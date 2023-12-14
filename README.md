AoC [readme](https://adventofcode.com/2023/about) says that:
> every problem has a solution that completes in at most 15 seconds on ten-year-old hardware

It happens that one of my computers runs on roughly 10 years old Intel i5-4460 so I decided to use it as a benchmarking machine instead of my daily driver i9-10850k that runs at almost twice the clock.

```
./01/solve_a.py: 57 19 20 20 21 20 22 23 23 23 ms | avg: 24 ms
./01/solve_b.py: 26 25 24 23 25 24 25 23 23 25 ms | avg: 24 ms
./02/solve_a.py: 14 13 13 12 13 13 13 13 15 13 ms | avg: 13 ms
./02/solve_b.py: 13 13 13 14 14 13 14 14 14 15 ms | avg: 13 ms
./03/solve_a.py: 22 21 20 20 20 20 21 22 20 20 ms | avg: 20 ms
./03/solve_b.py: 22 23 22 26 24 23 24 23 25 22 ms | avg: 23 ms
./04/solve_a.py: 24 23 23 23 22 24 24 25 24 26 ms | avg: 23 ms
./04/solve_b.py: 30 26 26 24 25 26 24 26 26 26 ms | avg: 25 ms
./05/solve_a.py: 26 20 20 20 19 21 20 19 19 19 ms | avg: 20 ms
./05/solve_b.py: 108 100 99 95 98 98 103 97 100 99 ms | avg: 99 ms
./06/solve_a.py: 19 18 19 19 20 21 19 18 18 20 ms | avg: 19 ms
./06/solve_b.py: 21 21 19 21 20 20 20 19 19 20 ms | avg: 20 ms
./07/solve_a.py: 31 32 31 31 33 39 33 34 32 30 ms | avg: 32 ms
./07/solve_b.py: 32 32 32 33 34 32 31 33 33 35 ms | avg: 32 ms
./08/solve_a.py: 29 27 27 26 29 25 27 26 26 25 ms | avg: 26 ms
./08/solve_b.py: 63 59 64 71 64 68 64 61 58 62 ms | avg: 63 ms
./09/solve_a.py: 23 23 20 21 20 21 19 19 20 17 ms | avg: 20 ms
./09/solve_b.py: 21 18 20 23 19 20 19 18 19 18 ms | avg: 19 ms
./10/solve_a.py: 85 84 82 78 76 79 78 80 78 80 ms | avg: 80 ms
./10/solve_b.py: 136 125 130 135 135 130 130 127 129 131 ms | avg: 130 ms
./11/solve_a.py: 351 356 357 343 348 351 336 351 353 344 ms | avg: 349 ms
./11/solve_b.py: 346 353 344 356 346 332 327 337 342 349 ms | avg: 343 ms
./12/solve_a.py: 35 34 35 35 34 34 34 34 34 34 ms | avg: 34 ms
./12/solve_b.py: 340 343 356 340 341 347 351 352 340 343 ms | avg: 345 ms
./13/solve_a.py: 18 17 17 17 17 17 16 16 16 16 ms | avg: 16 ms
./13/solve_b.py: 32 33 33 32 34 33 32 33 32 33 ms | avg: 32 ms
./14/solve_a.py: 121 119 120 118 123 122 122 122 133 123 ms | avg: 122 ms
./14/solve_b.py: 45224 44486 44622 45312 45397 44398 44496 46201 44338 45745 ms | avg: 45021 ms
./_meta/python_startup.py: 12 12 12 12 11 12 13 14 13 12 ms | avg: 12 ms
```
