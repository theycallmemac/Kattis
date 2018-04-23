
def main():

	cases = int(input())
	visited = []
  
	for i in range(0, num_times):
		cities = int(input())
    
		for j in range(0, cities):
			city = input()
			if (city not in visited):
				visited.append(city)
        
		print(len(visited))
		visited = []

if __name__ == '__main__':
    main()
