if __name__ == '__main__':
    n = int(input())
    arr=list(map(int, input().split()))
    
    maxscore=max(arr)
    filteredlist=[score for score in arr if score is not maxscore]
    runnerscore=max(filteredlist)
    print(runnerscore)