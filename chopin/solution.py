from sys import stdin
def main():

	case_no = 1
  
	for line in stdin:
  
		if line[0:2] == "A#" or line[0:2] == "C#" or line[0:2] == "D#" or line[0:2] == "F#" or line[0:2] == "G#":
			line = line.replace("A#", "Bb")
			line = line.replace("C#", "Db")
			line = line.replace("D#", "Eb")
			line = line.replace("F#", "Gb")
			line = line.replace("G#", "Ab")
			print("Case " + str(case_no) + ": " + line.strip())
			case_no += 1
      
		elif line[0:2] == "Ab" or line[0:2] == "Bb" or line[0:2] == "Db" or line[0:2] == "Eb" or line[0:2] == "Gb":
			line = line.replace("Bb", "A#")
			line = line.replace("Db", "C#")
			line = line.replace("Eb", "D#")
			line = line.replace("Gb", "F#")
			line = line.replace("Ab", "G#")
			print("Case " + str(case_no) + ": " + line.strip())
			case_no += 1
      
		elif line[0:1] == "A" or line[0:1] == "B" or line[0:1] == "C" or line[0:1] == "D" or line[0:1] == "E" or line[0:1] == "F" or line[0:1] == "G":
			print("Case " + str(case_no)+ ": " + 'UNIQUE')
			case_no += 1
      
		else:
			break

if __name__ == '__main__':
	main()

