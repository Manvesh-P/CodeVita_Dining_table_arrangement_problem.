# CodeVita Dining table seating arrangement.

T = int(input("Enter the number of test cases:"))


def fact(q):
    
    f = 1
    while q != 0:
        
        f = f * q
        q -= 1
        
    return f



def ncr(n,r):
    
    if n == r and r == 0:
        return 1
    
    elif r == 1:
        return n
    
    else:
        
        a = fact(n)
        b = fact(n - r)
        c = fact(r)
        
        res = a / b
        res1 = res / c
        
        return res1
    

for i in range(0, T):
    R, N = map(int, input("Enter the number of tables and attendees:").split())
    
    d = N
    pro = 1
    
    type1 = (N % R)
    type2 = R - (N % R)
    
    people1 = (N // R) + 1
    people2 = (N // R)
    
    for i in range(0, type1):
        pro = pro * ncr(d,people1)
        
        d -= people1
        
    for j in range(0, type2):
        pro = pro * ncr(d,people2)
        
        d -= people2
        
    print("%d"%pro)
