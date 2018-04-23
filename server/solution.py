
def main():


    inputs = input().split()
    total_time = 0

    number = int(inputs[0])
    time = int(inputs[1])
    tasks = input().split()

    task_count = 0
    i = 0
    while i < number:
    	total_time += int(tasks[i])
    	
    	if total_time <= time:
    		task_count += 1

    	if total_time > time:
    		break

    	i = i + 1
    print(task_count)

if __name__ == '__main__':
    main()

