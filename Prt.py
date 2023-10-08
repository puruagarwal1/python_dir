dp = [0]*1502
n = 1411
k = 1411
C = [[0 for x in range(1500)] for x in range(1500)]
MOD = pow(10, 9) + 7 
def binomialCoef(n, k):
	for i in range(n+1):
		for j in range(min(i, k)+1):
			if j == 0 or j == i:
				C[i][j] = 1
			else: 
				C[i][j] = (C[i-1][j-1] + C[i-1][j])% MOD
	return 0
def countBits(val):
	cnt = 0
	while(val > 0):
		val = val >> 1
		cnt+=1
	return cnt

def countSetBits(n):
	count = 0
	while (n):
		count += n & 1
		n >>= 1
	return count 

for i in range(2, 1500):
	dp[i]=  dp[countSetBits(i)] +1

dp[1] = 0
x, y = [int(x) for x in input().split()]
q = binomialCoef(n,k)
sal = countSetBits(x)
li = []
for i in range(1,1500):
	if dp[i]== y-1:
		li.append(i)
#print(li)
def cal( val, i):
	if val <= 0 or i < 0:
		return 0
	n  = countBits(val)
	ans = 0
	ans += C[n-1][i]
	val = val&(pow(2,n-1)-1)
	ans = (ans + cal(val, i-1))%MOD
	return ans%MOD
ans = 0

for i in li:
	val = x
	n1 = countBits(val)
	pos = 0
	c = 0
	if n1 > i:
		ans = (ans + cal(val, i)) %MOD
	if(countSetBits(val) == i):
		ans+=1
print(ans%MOD)