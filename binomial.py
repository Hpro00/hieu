import math
def tinhgiaithua(a) :
    k = 1;
    if a <= 1 :
      return 1
    else : 
      for i in range(1,a+1) :
        k = k * i 
    return k
   
def tinhphuctap(a,b):
    k = 1;
    c = a-b
    return  tinhgiaithua(a) / (tinhgiaithua(b) * tinhgiaithua(c))
    
def prob(n,p,N) :
    return tinhphuctap(N, n)*(p ** n)*(1 - p)**(N - n)
    
def infoMeasure(n, p, N):
    return -math.log(prob(n, p, N), 2)
    
   
def sumProb(N, p):
    """
    Tính tổng của xác suất của các symbol n của nguồn thông tin binomial
    """
    tong = 0 
    for i in range(1, N + 1):
        tong = tong + prob(i, p, N)

    return tong
    
def approxEntropy(N, p):
    """
    Tính entropy của phân bố binomial
    """
    sum = 0
    for i in range(1, N + 1):
        sum += prob(i, p, N)*infoMeasure(i, p, N)
    return sum

print(approxEntropy(3, 0.5))