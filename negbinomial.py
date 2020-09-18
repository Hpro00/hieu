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
    c = a - b + 1
    d = b - 1
    return  tinhgiaithua(a) / (tinhgiaithua(c) * tinhgiaithua(d))

def prob(n, p, r):
    return tinhphuctap(n,r)*(p ** n)*(1 - p)**r
    
def infoMeasure(n, p, r):
    return -math.log(prob(n, p, r), 2)
    
def sumProb(N, p, r):
    """
    Tính tổng xác suất của các symbol n từ nguồn thông tin negbinomial
    """
    tong = 0 
    for i in range(1, N + 1):
        tong += prob(i, p, r)

    return tong
    
def approxEntropy(N, p, r):
    """
    Tính entropy của nguồn thông tin negative binomial
    """
    tong = 0
    for i in range(1, N + 1):
        tong += prob(i, p, r)*infoMeasure(i, p, r)
    return tong    
    
print(approxEntropy(5, 0.5, 2))