n,k=map(int,input().split())
nums=list(map(int,input().split()))
nums.sort()

if(k==len(nums)):
    print(nums[k-1]+1)
elif (nums[k-1]==nums[k] or k==0):
    print(-1)
else:
    print(nums[k-1]+1)
