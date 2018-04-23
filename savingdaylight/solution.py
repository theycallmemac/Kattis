import sys

def get_time_difference(start_time,end_time):
	start = start_time.split(":")
	end = end_time.split(":")

	start_hour = start[0]
	end_hour = end[0]

	start_min = start[1]
	end_min = end[1]

	hour = int(end_hour) - int(start_hour)
	minute = int(end_min) - int(start_min)

	if hour < 0:
		hour = 24 + hour

	if minute < 0:
		hour -= 1
		minute = 60 + minute

	return hour, minute

def main():
	try:
		inputs = input().split()
		while inputs != None:

			date = str(inputs[0])
			month = int(inputs[1])
			year = int(inputs[2])
			start_time = str(inputs[3])
			end_time = str(inputs[4])

			time = get_time_difference(start_time,end_time)

			print(str(date) + " " + str(month) + " " + str(year) + " " + str(time[0]) + " " + "hours " + str(time[1]) + " minutes")
			inputs = input().split()
      
	except EOFError:
		sys.exit()
    
	except IndexError:
		sys.exit()


if __name__ == '__main__':
	main()

