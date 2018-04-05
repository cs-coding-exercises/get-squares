# get-squares

The algorithm takes attributes of multiple squares from a file and computes the coordinates of the square that would encompass all of them

it takes a list files as arguments and computes the encompassing square for all of the squares in each individual file (not all squares in all files combined)


##### inputs:  squares files
The file names are sent in as arguments

Each line in each file contains a square's
  - bottom X value
  - bottom Y value
  - length
  - height
  
  
##### output
the output will include:
  - the high and low X and Y values for the encompassing square
  - the coordinates of the encompassing square

```
==============================
Lower_X: 5
Lower_Y: 9
Upper_X: 25
Upper_Y: 119
==============================
Bottom Left  : 5,9
Bottom Right : 25,9
Top Left     : 5,119
Top Right    : 25,119
```

