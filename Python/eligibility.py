
def is_eligible(name,study_year,birth_year,course):
        if study_year >= 2010:
            return(name + " eligible")
        elif birth_year >= 1991:
            return(name + " eligible")
        elif course > 40:
            return(name + " ineligible")
        else:
            return(name + " coach petitions")

def main():

    n = int(input())

    for i in range(n):
        inputs = input().split()

        name = inputs[0]
        study_year = int(inputs[1][0:4])
        birth_year = int(inputs[2][0:4])
        course = int(inputs[3])

        print(is_eligible(name,study_year,birth_year,course))
if __name__ == '__main__':
    main()

