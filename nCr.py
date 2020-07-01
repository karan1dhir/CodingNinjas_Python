number = int(input())
r = int(input())

nfact = 1
for i in range(1,number+1,1):
    nfact = nfact * i;

rfact = 1
for i in range(1,r+1,1):
    rfact = rfact * i;

n_rfact = 1
for i in range(1, number - r + 1):
    n_rfact = n_rfact * i

ans = nfact//(rfact * n_rfact);
print(ans)
