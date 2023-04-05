N = 10**5
ns = [0,0]+[1]*N

for step in range(2, N//2):
    for n in range(step*2, N+1, step):
        ns[n] += step

for n in range(len(ns)):
    ns[n] = ns[n] > n

def sum_of_abundants(n: int) -> bool:
    for i in range(12, n):
        if ns[i] and ns[n-i]:
            return True
    return False

for _ in range(int(input())):
    n = int(input())
    print("YES" if sum_of_abundants(n) else "NO")
