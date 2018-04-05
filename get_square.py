import sys

def get_encomapsing_square(file_name):

    Lower_X    = None
    Lower_Y    = None
    Upper_X    = None
    Upper_Y    = None

    with open(file_name, 'r') as file:
        for line in file:
            square_data_arr = line.split()
            print("square_data: " + str(square_data_arr))

            low_x = int(square_data_arr[0])
            upp_x = int(square_data_arr[0]) + int(square_data_arr[2])
        
            low_y = int(square_data_arr[1])
            upp_y = int(square_data_arr[1]) + int(square_data_arr[3])

            print("low_x: " + str(low_x) )
            print("upp_x: " + str(upp_x) )
            print("low_y: " + str(low_y) )
            print("upp_y: " + str(upp_y) )

            if Lower_X is None:   Lower_X = low_x
            elif low_x < Lower_X: Lower_X = low_x

            if Upper_X is None:   Upper_X = upp_x
            elif upp_x > Upper_X: Upper_X = upp_x

            if Lower_Y is None:   Lower_Y = low_y
            elif low_y < Lower_Y: Lower_Y = low_y

            if Upper_Y is None:   Upper_Y = upp_y
            elif upp_y > Upper_Y: Upper_Y = upp_y

        print("==============================")
        print("Lower_X: " + str(Lower_X) )
        print("Lower_Y: " + str(Lower_Y) )
        print("Upper_X: " + str(Upper_X) )
        print("Upper_Y: " + str(Upper_Y) )
        print("==============================")
        print("Bottom Left  : " + str(Lower_X) + "," + str(Lower_Y) )
        print("Bottom Right : " + str(Upper_X) + "," + str(Lower_Y) )
        print("Top Left     : " + str(Lower_X) + "," + str(Upper_Y) )
        print("Top Right    : " + str(Upper_X) + "," + str(Upper_Y) )


##===============================
argv_len = len(sys.argv)
files=[]
for x in range (1 , argv_len):
    file[x-1] = sys.argv[x]

#files = ['squares_1.dat','squares_2.dat','squares_3.dat']
for file in files:
    get_encomapsing_square(file)
