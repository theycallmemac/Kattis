def main():
    
    n = int(input())
    lst = [int(input()) for _ in range(n)]
    
    lst.sort(reverse=True)
    answer = sum(lst)
    
    for i in range(2, len(lst), 3):
        answer -= lst[i]
        
    print(answer)

if __name__ == '__main__':
    main()
