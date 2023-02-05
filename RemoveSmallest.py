test=int(input())
for _ in range(test):
    n=int(input())
    nums=list(map(int,input().split()))
    nums.sort()
    yes=True
    for i in range(len(nums)-1):
        if(abs(nums[i]-nums[i+1])<=1):
            continue
        else:
            yes=False
            break
    
    if(yes):
        print("YES")
    else:
        print("NO")
