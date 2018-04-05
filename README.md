## get-squares

The algorithm takes attributes of multiple squares from a file and computes the coordinates of the square that would encompass all of them

it takes a list files as arguments and computes the encompassing square for all of the squares in each individual file (not all squares in all files combined)


## Inputs:  squares files
The file names are sent in as arguments

Each line in each file contains a square's
  - bottom X value
  - bottom Y value
  - length
  - height
  
Examples:  
```
#squares_3.dat
5 9 10 40
11 79 10 40
12 17 10 40
15 9 10 40
```
  
## Output
the output will include:
  - the high and low X and Y values for the encompassing square
  - the coordinates of the encompassing square

```
$python3 get_square.py squares_3.dat

File: squares_3.dat
-------------------------------
square_data: ['5', '9', '10', '40']
square_data: ['11', '79', '10', '40']
square_data: ['12', '17', '10', '40']
square_data: ['15', '9', '10', '40']
-------------------------------
Lower_X: 5
Lower_Y: 9
Upper_X: 25
Upper_Y: 119
-------------------------------
Bottom Left  : 5,9
Bottom Right : 25,9
Top Left     : 5,119
Top Right    : 25,119
==============================
```

