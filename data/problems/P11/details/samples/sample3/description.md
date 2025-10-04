Here is the trace for A=100 and B=25:
1. `func(100, 25)`: Since A > B, this calls `func(25, 75)`.
2. `func(25, 75)`: Since A < B, this calls `func(25, 50)`.
3. `func(25, 50)`: Since A < B, this calls `func(25, 25)`.
4. `func(25, 25)`: Since A = B, the function returns A, which is `25`.