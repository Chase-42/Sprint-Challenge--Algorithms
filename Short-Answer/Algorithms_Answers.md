#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) Though the while loop is multiplying 3 times and the inner loop is multiplying 2 times the loop is still based on the size of n. Thus, the loop is running at a runtime complexity of O(n).

b) The first loop will have a complexity of O(n) but the inner loop will double every time we run it thus making the whole code have a runtime complexity of O(n log n).

c) This function iterates a recursive call once for every number from n to 0, thus making it have a runtime complexity of O(n).

## Exercise II

I would prefer to use a Binary Search algorithm. We would start at the middle floor of the n-story building, where we would throw the egg. If the egg breaks, then we would move down to the lower half of the building until the egg is able to fall without breaking, which would determine our f value. If the egg does not break when thrown from the middle, then we would move up the upper half of the building until it does break, which would determine our f value. The runtime complexity of O(log n).
