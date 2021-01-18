N = int(input()) 
R = (N-1) * 2 + 1
while True:
    for i in range(R): 
        if i < N: 
            print("*"*(i+1))
        else:
            print("*"*(R-i))
