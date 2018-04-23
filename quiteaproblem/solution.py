
def main():

    word = "problem"
    
    try:
        for i in range(1000):
            line = input().lower()

            if word in line:
                print("yes")
            else:
                print("no")         
    except EOFError:
        sys.exit()
        
if __name__ == '__main__':
    main()
