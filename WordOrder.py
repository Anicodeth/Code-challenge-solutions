# Enter your code here. Read input from STDIN. Print output to STDOUT
uni=set()
words={}
n=int(input())

for _ in range(n):
    word=input()
    uni.add(word)
    words[word]=1+words.get(word,0)
    
print(len(uni))

for word in words:
    print(words[word], end=' ')
