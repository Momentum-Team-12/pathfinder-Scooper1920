# Pathfinder

## Description

Using object-oriented programming and testing, pathfinder is a program to read elevation data, draw an elevation map as a `.png` file, and chart the best path across the map.



## Deliverables

- A Git repo containing:
  - A Python file called `pathfinder.py` that when run, creates a file called `map.png`.
  - One or more test files to test the program
  - A `Pipfile` with your dependencies listed in it

## Approach

As you I went through this assignment,  I used test-driven development as much as possible to write your code. It was be difficult to test that the appropriate `.png` file is generated, but all the data transformation should is testable.




The data from `elevation_small.txt` was converted into an appropriate data structure to get the elevation data. This file is made up of multiple lines. Each line has a list of numbers representing elevation in meters. The elevation is the maximum elevation for a 90m x 90m square.

The numbers in this file are lined up like x-y coordinates. If the file contains the following:

```
150 175 150 200
170 191 190 182
179 191 180 182
193 195 190 192
```


Using the [Pillow library](https://pillow.readthedocs.io/en/3.0.x/index.html), I created an elevation map from the data. Higher elevations are brighter; lower elevations darker.




Once you I had that working, I added the ability to start from the left edge of the map on any row (y-position) and calculate and draw a path across the map using a provided algorithm. 


