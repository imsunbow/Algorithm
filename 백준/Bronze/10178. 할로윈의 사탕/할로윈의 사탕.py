#백준 10178

n = int(input())

for _ in range(n):
    a,b = map(int,input().split())
    c = a // b
    d = a % b
    print("You get",c,"piece(s) and your dad gets",d,"piece(s).")


