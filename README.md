AoC [readme](https://adventofcode.com/2023/about) says that:
> every problem has a solution that completes in at most 15 seconds on ten-year-old hardware

It happens that one of my computers runs on roughly 10 years old Intel i5-4690k so I decided to use it as a benchmarking machine instead of my daily driver i9-10850k that runs at almost twice the clock.

```
./01/solve_a.py: 16 16 16 16 16 16 16 16 16 16 ms | avg: 16 ms
./01/solve_b.py: 18 19 19 18 18 18 19 18 18 18 ms | avg: 18 ms
./02/solve_a.py: 10 10 9 9 9 9 9 9 9 9 ms | avg: 9 ms
./02/solve_b.py: 9 9 9 9 9 9 9 9 9 9 ms | avg: 9 ms
./03/solve_a.py: 15 15 15 15 15 15 15 15 15 15 ms | avg: 15 ms
./03/solve_b.py: 17 16 16 16 16 16 17 16 16 16 ms | avg: 16 ms
./04/solve_a.py: 17 17 17 17 17 17 17 17 17 17 ms | avg: 17 ms
./04/solve_b.py: 22 18 18 18 18 18 18 18 18 18 ms | avg: 18 ms
./05/solve_a.py: 14 14 14 14 14 14 14 14 14 14 ms | avg: 14 ms
./05/solve_b.py: 74 72 73 72 72 72 72 73 74 74 ms | avg: 72 ms
./06/solve_a.py: 14 14 14 14 14 14 14 14 14 14 ms | avg: 14 ms
./06/solve_b.py: 14 14 14 14 14 14 14 14 14 14 ms | avg: 14 ms
./07/solve_a.py: 22 22 22 22 22 22 22 22 22 22 ms | avg: 22 ms
./07/solve_b.py: 23 24 24 23 23 24 23 23 24 23 ms | avg: 23 ms
./08/solve_a.py: 21 18 19 18 19 19 19 19 19 18 ms | avg: 18 ms
./08/solve_b.py: 45 46 45 45 46 46 45 46 45 45 ms | avg: 45 ms
./09/solve_a.py: 13 13 14 13 13 13 13 13 13 13 ms | avg: 13 ms
./09/solve_b.py: 13 13 13 13 13 13 13 13 13 13 ms | avg: 13 ms
./10/solve_a.py: 60 59 59 59 59 60 59 60 59 59 ms | avg: 59 ms
./10/solve_b.py: 98 98 101 99 96 98 100 96 98 96 ms | avg: 98 ms
./11/solve_a.py: 264 268 276 264 269 264 262 264 264 267 ms | avg: 266 ms
./11/solve_b.py: 268 272 269 268 272 266 267 269 265 266 ms | avg: 268 ms
./12/solve_a.py: 26 26 27 26 26 26 26 27 26 27 ms | avg: 26 ms
./12/solve_b.py: 273 273 273 271 271 270 273 271 270 274 ms | avg: 271 ms
./13/solve_a.py: 12 12 12 12 12 12 12 12 12 12 ms | avg: 12 ms
./13/solve_b.py: 25 25 25 25 25 25 25 25 25 25 ms | avg: 25 ms
./14/solve_a.py: 96 105 98 117 94 96 96 97 96 97 ms | avg: 99 ms
./14/solve_b.py: 1347 1357 1348 1351 1345 1358 1380 1354 1349 1365 ms | avg: 1355 ms
./15/solve_a.py: 24 24 24 24 24 24 24 24 24 24 ms | avg: 24 ms
./15/solve_b.py: 25 25 25 25 25 25 25 25 25 25 ms | avg: 25 ms
./16/solve_a.py: 34 34 34 34 34 34 34 34 34 34 ms | avg: 34 ms
./16/solve_b.py: 1758 1744 1758 1750 1755 1770 1772 1765 1754 1760 ms | avg: 1758 ms
./17/solve_a.py: 923 919 929 911 913 920 934 905 913 910 ms | avg: 917 ms
./17/solve_b.py: 3072 3077 3019 3066 3032 3065 3072 3109 3028 3035 ms | avg: 3057 ms
./18/solve_a.py: 27 27 27 27 27 27 27 27 27 27 ms | avg: 27 ms
./18/solve_b.py: 27 27 27 27 27 27 27 27 27 27 ms | avg: 27 ms
./19/solve_a.py: 44 37 36 36 38 36 36 36 38 36 ms | avg: 37 ms
./19/solve_b.py: 33 35 35 33 33 33 35 33 33 33 ms | avg: 33 ms
./20/solve_a.py: 149 145 147 144 146 146 144 146 145 145 ms | avg: 145 ms
./20/solve_b.py: 448 450 448 455 445 455 448 451 453 447 ms | avg: 450 ms
./21/solve_a.py: 62 61 62 63 62 62 62 62 61 62 ms | avg: 61 ms
./21/solve_b.py: 20238 20570 20020 19616 19930 19667 19441 20601 19911 20072 ms | avg: 20006 ms
./22/solve_a.py: 3300 3358 3256 3293 3350 3337 3311 3364 3327 3325 ms | avg: 3322 ms
./22/solve_b.py: 3347 3398 3383 3365 3321 3385 3296 3335 3304 3331 ms | avg: 3346 ms
./23/solve_a.py: 234 234 236 235 234 232 234 234 234 233 ms | avg: 234 ms
./23/solve_b.py: 21246 21062 20959 21014 21075 21160 21015 21029 21137 20999 ms | avg: 21069 ms
./24/solve_a.py: 148 151 150 148 149 149 149 148 149 145 ms | avg: 148 ms
./24/solve_b.py: 3146 3137 3138 3148 3133 3152 3137 3148 3139 3138 ms | avg: 3141 ms
./25/solve_a.py: 10705 11029 11004 10895 11123 11191 10718 11000 10859 10780 ms | avg: 10930 ms
./_meta/python_startup.py: 8 8 8 8 8 8 8 8 8 8 ms | avg: 8 ms
```
