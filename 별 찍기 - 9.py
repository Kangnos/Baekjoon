a = int(input())
b = a
for i in range(1, a+1): # (1, 6)이라는 뜻
    print(' '*(i-1)+'*'*(2*(b-i)+1)) # 핵심중의 핵심 나는 그동안 이 규칙이 이해가 안되서 실수 했던 것이다
    
for k in range(1, b): # (1, 5)라는 뜻
    print(' '*(b-k-1)+"*" *(2*k+1)) 
    # 여기서 b는 5이다