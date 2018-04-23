from sys import stdin

def get_sum(n):
   total = 0
   while n:
       total, n = total + n % 10, n // 10
   return total

def main():

    for line in stdin:
        line = line.strip()
        n = int(line)

        if n == 0:
            break
        
        i = 11
        while True:
            if get_sum(n) == get_sum(n * i):
                print(i)
                break
            i += 1

if __name__ == '__main__':
	main()
