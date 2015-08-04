# ulamspiral
Python code to generate and print Ulam Spirals.

## Synopsis
A Python module to create Ulam Spirals. An Ulam spiral is a regular rectangular grid of integers,
starting at 1 (or, optionally, some other positive integer) at the center and spiraling outwardly.

This code implements Ulam Spirals spiraling clockwise.

## Example

The module implements a class which is initiated with an end integer (and an optional start
integer).

```python
>>> import ulamspiral
>>> S = ulamspiral.UlamSpiral(24, start=0)
>>> S.show()
 20 21 22 23 24
 19  6  7  8  9
 18  5  0  1 10
 17  4  3  2 11
 16 15 14 13 12
```
