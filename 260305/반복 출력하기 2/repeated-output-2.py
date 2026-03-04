n = int(input())

# Please write your code here.
def rep(n):
    if n:
        n -= 1
        print('HelloWorld')
        rep(n)
rep(n)