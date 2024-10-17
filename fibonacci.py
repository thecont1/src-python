def fibonacci(n):

    if n == 0: return 0
    if n == 1: return 1
    F = [0, 1]
    for i in range(2, n+1):
        F.append(F[-1] + F[-2])
        
    return F[-1]

n = int(input())
print(f"F({n}) = {fibonacci(n)}")