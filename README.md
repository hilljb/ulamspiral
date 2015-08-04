# ulamspiral
Python code to generate and print [Ulam Spirals](https://en.wikipedia.org/wiki/Ulam_spiral).

## Synopsis
A Python module to create Ulam Spirals. An Ulam spiral is a regular rectangular grid of integers,
starting at 1 (or, optionally, some other positive integer or zero) at the center and spiraling
outwardly.

This code implements Ulam Spirals spiraling clockwise.

## Example

The module implements a class which is initiated with an end integer (and an optional start
integer).

```python
>>> import ulamspiral
>>> S = ulamspiral.UlamSpiral(24)
>>> S.show()
 21 22 23 24   
 20  7  8  9 10
 19  6  1  2 11
 18  5  4  3 12
 17 16 15 14 13

>>> S = ulamspiral.UlamSpiral(24, start=0)
>>> S.show()
 20 21 22 23 24
 19  6  7  8  9
 18  5  0  1 10
 17  4  3  2 11
 16 15 14 13 12

>>> ulamspiral.UlamSpiral(200, start=0).show()
     156 157 158 159 160 161 162 163 164 165 166 167 168 169
     155 110 111 112 113 114 115 116 117 118 119 120 121 170
     154 109  72  73  74  75  76  77  78  79  80  81 122 171
     153 108  71  42  43  44  45  46  47  48  49  82 123 172
     152 107  70  41  20  21  22  23  24  25  50  83 124 173
     151 106  69  40  19   6   7   8   9  26  51  84 125 174
     150 105  68  39  18   5   0   1  10  27  52  85 126 175
     149 104  67  38  17   4   3   2  11  28  53  86 127 176
     148 103  66  37  16  15  14  13  12  29  54  87 128 177
 200 147 102  65  36  35  34  33  32  31  30  55  88 129 178
 199 146 101  64  63  62  61  60  59  58  57  56  89 130 179
 198 145 100  99  98  97  96  95  94  93  92  91  90 131 180
 197 144 143 142 141 140 139 138 137 136 135 134 133 132 181
 196 195 194 193 192 191 190 189 188 187 186 185 184 183 182
```

## Installation

Clone this repository (minimally, all that is needed is the `ulamspiral.py` file) and place the
`ulamspiral.py` file in your Python's path. (There is no setup script currently.)

## Diagonal Primes

The interest in this rectangular spiral of integers comes from the fact that primes are arranged
in diagonal lines with a probability higher than one might expect. We can view this phenomenon as
follows.

We write the following script, which generates primes with a sieve and then displays only prime
integers in an Ulam spiral.

```python
#!/usr/bin/python2                                                                                  
                                                                                                    
import ulamspiral                                                                                   
                                                                                                    
limit = 700                                                                                                                                    
                                                                                                    
def primes_range(stop):                                                                             
    """ Form a prime sieve and return a list of primes below 'stop'."""                             
    primes = [True] * stop                                                                          
    primes[0], primes[1] = [False] * 2                                                              
    L = []                                                                                          
    for ind, val in enumerate(primes):                                                              
        if val:                                                                                     
            primes[ind*2::ind] = [False] * (((stop - 1)//ind) - 1)                                  
            L.append(ind)                                                                           
    return L                                                                                        
                                                                                                    
# Form the Ulam Spiral                                                                              
S = ulamspiral.UlamSpiral(limit)                                                                    
                                                                                                    
# Form the list of primes                                                                           
P = set(primes_range(limit))                                                                        
                                                                                                    
# Show only primes in the spiral                                                                    
# Determine character width for printing                                                               
char_width = len(str(max([max(i) for i in S.rows]))) + 1                                            
for row in S.rows:                                                                                  
    row_str = ''                                                                                    
    for i in row:                                                                                   
        if i <= S.max_int and i in P:                                                               
            row_str += str(i).rjust(char_width)                                                     
        else:                                                                                       
            row_str += ''.rjust(char_width)                                                         
    print row_str
```

```text
$ python diagonal_primes.py

     601                     607                     613             617     619                            
                 509                                             521     523                                
     599     421                                     431     433                     439                    
                                 347     349             353                     359             443        
             419                     277             281     283                                            
         503             211                                             223                             631
                     271     157                     163             167             227                    
                                         113                                             293                
     593             269              73                      79                     229     367            
         499     337             109      43              47              83     173             449        
                                      71              23                                                    
 691                             107      41       7                                                        
                             151              19           2  11      53     127     233             541    
                                                   5       3      29                                        
     587     409     263     149      67      17              13                             373            
                 331             103      37                      31      89     179                     641
                                                      61      59             131                            
         491             199     101              97                             181             457     643
                                                     139     137                     239             547    
 683                     197             193     191                                                        
                     257                     251                                     241     379            
         487                                     317             313     311             307     461     647
             401             397                             389                     383                    
                                 479                                             467             463        
     577                     571     569                     563                     557                    
 677             673                                             661     659                     653
```

