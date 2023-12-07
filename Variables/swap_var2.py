#!usr/bin/env python3

""" Use of XOR(exclusive or) operator to swap variables
This is also a 3-step method.
"""
x = 20
y = 30

#step 1
x ^= y

#step 2
y ^= x

#step 3
x ^= y

print(f'x is: {x}')
print(f'y is: {y}')

"""In Python, the XOR operation is represented by the '^' (caret) symbol.
The XOR operation returns 1 for bits that are different and 0 
for bits that are the same.

How does XORing 'x' and 'y' works in binary:
    x = 20  # Binary: 10100
    y = 30  # Binary: 11110

Step 1: XOR the values of x and y and store the result in x
    x ^= y
In binary, this operation is equivalent to:
    x = 20 ^ 30
Breaking it down bit by bit:
      10100  (x)
    ^ 11110  (y)
    ---------
      01010  (result) N/B: if both x and y are value 0 or 1, the result is 0, otherwise 1,
After XORing, the binary result is 01010, which is 10 in decimal.

Therefore, after Step 1, the value of x becomes 10. The original value 
of y is still stored in y at this point.


Step 2:
    y ^= x
In binary:
      11110  (y)
    ^ 01010  (x)
    ---------
      10100  (result)

After XORing, the binary result is 10100, which is 20 in decimal. 
Now, the original value of x is stored in y.

Step 3:
    x ^= y
In binary:
      01010  (x)
    ^ 10100  (y)
    ---------
      11110  (result)

After XORing, the binary result is 11110, which is 30 in decimal. 
Now, the original value of y is stored in x.

Now, if you print the values of x and y:
    print(f'x is: {x}')
    print(f'y is: {y}')

output:
    x is: 30
    y is: 20

So, through the series of XOR operations, the values of x and y have
effectively swapped without using a temporary variable. 
Each XOR operation undoes the previous one, leading to the final swapped values.
"""






