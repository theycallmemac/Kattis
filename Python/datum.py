import calendar

def find_day(day):

	lines = {
			"0":"Monday",
			"1":"Tuesday",
			"2":"Wednesday",
			"3":"Thursday",
			"4":"Friday",
			"5":"Saturday",
			"6":"Sunday"
			}

	for key in day:
		return lines[key]

def main():

	inputs = input().split()

	date = int(inputs[0])
	month = int(inputs[1])
	year = 2009

	n = str(calendar.weekday(year, month, date))
	day = find_day(n)
	print(day)

if __name__ == '__main__':
	main()
