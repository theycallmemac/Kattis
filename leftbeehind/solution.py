
def main():

    jars = [int(i) for i in input().split()]
    while jars != [0,0]:

        sweet = jars[0]
        sour = jars[1]

        if sour + sweet == 13:
            print('Never speak again.')
        elif sour > sweet:
            print('Left beehind.')
        elif sweet > sour:
            print('To the convention.')
        else:
            print('Undecided.')
        jars = [int(i) for i in input().split()]

if __name__ == '__main__':
    main()
