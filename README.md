Latin Squares Generator
=============
&copy;2013 Kevin Dean

Small set of functions to create latin squares.

=============

Latin squares are NxN grids of n distinct symbols. The squares produced here are digits of 0 through the dimension number, and exactly n squares are produced (a cube of values). Running the latin_squares.py file will run a test script that takes in a dimension and produces random squares to match it.

Note that latin squares of dimension < 4 are considered invalid, as not enough permutations of 3 exist to fill the cube fully.

Also note that an optimization could be to not use the entire set of permutations produced by itertools, but this would significantly reduce the entropy of the squares, as you do not get a chance to shuffle the results.

Feel free to use these functions in any project, no credit required.
