# set
### Introduction
- A set is a programming data structure where the order of the objects inside does not matter because there can only be one of each piece of data without any duplicates. This means that the position of a data piece in the set can be determined by the information contained in the data piece. For example, if a set contained the numbers 1,4,7,5,3,12,15 it would look something like {1,-,3,4,5,-,7,-,-,-,-,12,-,-,15}. While this method means that you can't have any duplicates, it makes it very easy to find if a set contains a certain piece of data, you just need to go to the place where that data piece would be stored and see if it is there. The technique that allows a data piece to be stored in one index and one index only is called hashing.

### hashing sets
- The most basic hash function is index(n) = n. This function will cause the data to be stored in the location index that equals it. For example, 1 will be stored in index 1, 2 will be stored in index 2, 3 will be stored in index 3, and so on.  The problem with this function is that if you want to store a small number of very large numbers such as 1743, 1438, 3958, and 4853, you would need a set with thousands of spaces for just four number, resulting in a lot of wasted space. One method of reducing the required memory is to use the modulus (%) operator in the hash function. The modulus operator divides the first number by the second (X % Y) and returns the remainder. For example, 22 / 5 is 4 with a remainder of 2, so 22 % 5 = 2.  
- If your hash function is index(n) = n % y where y is equal to the size of the set, the data will be placed at the index equal to the modulus, and thanks to how rounding works, it’s impossible for the index to be outside the set, preventing overflow problems.

### addressing conflicts from hashing
-	There is one problem with using modulus in the hash function. It’s possible for two different numbers to have the same modulus, and thus would be placed in the same index. When this happens, it is called a conflict.
### uses of sets
-	
### set syntax
