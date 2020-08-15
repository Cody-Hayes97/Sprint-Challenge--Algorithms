#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)This algorithm has a linear O(n) runtime Because even though there are 3 n inputs being multiplied, they are still the same number so the while loop will depend on just the one n input


b)This algorithm has a runtime of O(n^2) because there is a while loop nested inside of a for loop. Both of which are dependant on the n input to run. since the while loop is linear time and the for loop is linear time, they are multiplied together


c)This algorithm has a runtime of O(n) Because it is calling itself recursively but only once. The if sytatement inside has a constant runtime so since there is only one factor being affected by the input, its linear time 

## Exercise II
Binary search 

loop through the array until we know what f is
find the middle floor of the building and drop an egg
If the egg does not break, set the floor after the middle to be the new ground floor and find the new middle of that shortened array
If the egg does break, set the floor before the middle as the new top floor and find the middle of that shortened array
keep halving the floors and throwing the egg in the middles until we find the floor where where the egg breaks but directly under it the egg does not.

this is a binary search algorithm so the runtime is O(log n)

