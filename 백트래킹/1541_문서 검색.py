word=input()
target=input()
n=len(target)
visited=[False]*len(word)
cnt=0

def find_docs(idx):
    global cnt

    if idx>len(word)-n:
        return

    for i in range(idx,len(word)):
        if word[i:i+n]==target and not visited[i]:
            for j in range(i,i+n):
                visited[j]=True
            cnt+=1
            find_docs(i+n)

find_docs(0)
print(cnt)
