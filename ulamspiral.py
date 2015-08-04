#!/usr/bin/python2

# ulamspiral.py

# See test.py for basic tests this code passes.
# See examples.py for basic examples.


__author__ = "Jason B. Hill"
__email__ = "jason@jasonbhill.com"


# Set a limit on size of numbers inside the spiral
_spiral_max_size_ = 4294967295 # 2**32-1

class UlamSpiral(object):
    """ An Ulam Spiral class.

    A class to create Ulam spirals, i.e., spirals of natural numbers on a square grid.

    When initialized, the spiral starts its existence as a single point inside a list of lists. New
    rows are added to the bottom of the spiral and the current spiral is rotated counter-clockwise.
    This process continues until the spiral contains its end point (maximum point). At this point,
    the spiral is rotated until its smallest and second smallest integers are aligned left and
    right, respectively, in the same row. When a spiral is printed, only values below and including
    its end point are printed.
    """
    def __init__(self, end, start=1):
        """ Initialize an instance of the UlamSpiral class.

        INPUT
        -----
        end : int or long
            The largest natural number represented in the spiral.
        start : int : default=1
            The starting number in the center of the spiral.

        RAISES
        ------
        TypeError : The start or end is not an integer (or long).
        ValueError : The start or end is not positive or zero, the start or end exceeds the cap, or
            the start is greater than the end. 
        """
        # Verify that the spiral start number is valid
        if not isinstance(start,(int,long)):
            raise TypeError('Spiral start must be a positive integer; %s entered' % start)
        elif start < 0:
            raise ValueError('Spiral start must be a positive integer; %s entered' % start)
        elif start > _spiral_max_size_:
            raise ValueError('Spiral start (%s) exceeds cap (%s)' % (start, _spiral_max_size_))

        # Verify that the spiral end number is valid
        if not isinstance(end,(int,long)):
            raise TypeError('Spiral size must be a positive integer; %s entered' % end)
        elif end < 0:
            raise ValueError('Spiral size must be a positive integer; %s entered' % end)
        elif end < start:
            raise ValueError('Spiral end (%s) smaller than start (%s)' % (end, start))
        elif end > _spiral_max_size_:
            raise ValueError('Spiral end (%s) exceeds cap (%s)' % (end, _spiral_max_size_))

        # Store the smallest and largest natural numbers to be represented in this spiral
        self.min_int = start
        self.max_int = end

        # self.rows stores the spiral itself as a list of rows (all spirals contains zero)
        self.rows = [[start]]

        # self.size stores the size of the spiral in a list as [row size, column size]
        self.size = [1,1]

        # Now construct the spiral
        while self.rows[self.size[0]-1][0] < self.max_int:
            # Add a new row if the spiral hasn't included its maximum natural number yet
            self._add_row_()

        # Orient the spiral (0 and 1 in same row with 0 on the left side of 1)
        if max(self.size) != 1: # Don't try to orient the base case spiral ([[0]])
            self._orient_()


    def __str__(self):
        """ Human readable string representation of Spiral class instance."""
        # Determine character width for printing
        char_width = len(str(max([max(i) for i in self.rows]))) + 1
        # Form a string to return
        return_str = ''
        for row in self.rows:
            row_str = ''
            for i in row:
                if i <= self.max_int:
                    row_str += str(i).rjust(char_width)
                else:
                    row_str += ''.rjust(char_width)
            return_str += row_str + '\n'

        return return_str


    def __repr__(self):
        """ Machine readable representation of Spiral class instance."""
        return "UlamSpiral of size %s" % self.max_int


    def _rotate_(self):
        """ Rotate the current spiral 90 degrees counter-clockwise.

        This method is used in constructing the spiral and is not intended to be called explicitly.

        INPUT
        -----
        None        
        """
        rn = self.size[0] # row size
        cn = self.size[1] # column size
        # rotate counter clockwise
        self.rows = [[self.rows[i][j] for i in range(rn)] for j in range(cn-1,-1,-1)]
        # save the row size and column size after rotation
        self.size = [self.size[1], self.size[0]]


    def _add_row_(self):
        """ Add a new row to the bottom of the current spiral.

        This method is used in constructing the spiral and is not intended to be called explicitly.

        INPUT
        -----
        None
        """
        # The largest value in the current spiral (under construction) is the bottom-left corner.
        start_int = self.rows[self.size[0]-1][0]
        end_int = start_int + self.size[0]
        # Rotate the spiral before appending the new row
        self._rotate_()
        # Append the new row
        self.rows.append(range(end_int, start_int, -1))
        # Add a row to the spiral size
        self.size[0] += 1


    def _orient_(self):
        """ Orient the current spiral.

        Rotates the spiral counter-clockwise until the second smallest integer is to the right of
        the smallest integer.

        This method is used in constructing the spiral and is not intended to be called explicitly.

        INPUT
        -----
        None
        """
        r = self.min_int
        s = self.min_int + 1
        while not any([r in i and s in i and i.index(r) < i.index(s) for i in self.rows]):
            self._rotate_()


    def show(self):
        """ Print the spiral.

        Uses the class's __str__ method to pretty-print the spiral.
        """
        print str(self)

