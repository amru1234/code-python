n, k = map(int, input().split())
bill = list(map(int, input().split()))
b = int(input())
anna_share = (sum(bill) - bill[k]) // 2
if anna_share == b:
    print("Bon Appetit")
else:
    print(b - anna_share)
