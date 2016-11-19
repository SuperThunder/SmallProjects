A standard library to give interoperable, sane, and reliable functionality that would often be found in the standard library, but must be hand written for assignments by requirement.


#Common string and input functions:

##Convert string containing number to int
1. A leading + or - should be handled
2. A number that is too big for int type should be handled
3. Any invalid characters should be noticed, and the function must pass back an appropriate error

##Compare two strings: memory unsafe
1. Two strings will be compared, with the reliance that the null terminator will exist in both
2. Appropriate and well defined feedback will be returned

##Compare two strings: memory safe
1. Two strings will be compared, with a given upper bound on length
2. Appropriate and well defined feedback will be returned

##Find the instances of one string inside another
1. Each instance, and its index, of a given token inside a string will be found
2. Returned will be the next instance, from a given starting point
3. When there are no more instances, a signal will be sent

##Find the instances of any string in another, as delineated by a token: Simple
1. The token is selectable and passed as an argument
2. As with string comparing, there is the possibility for out of bounds access; potentially requiring an upper bound to be given

##Find the instances of a string in another, as delineated by tokens: Adaptable
1. Both the string and any numbers of tokens should be arbitrily selecteable; "" as the string meaning any string
2. An alternate version may be non-strict delineation, the delineaters on both sides can be different chars; ex 'token] being valid
3. As with string comparing, there is the possibility for out of bounds access; potentially requiring an upper bound to be given

##Return the length of a string
1. By normal C methods, this relies on a null terminator, or some other delineator, existing in the string. This is of course extremely unsafe to expect.
2. It may be necesarry to create a string object/class

##Slice a string out of an original string
1. Options may be required for what is to be done with the leftover parts of the string on both the left and right

##Combine two strings together
1. The most common use is likely to append or prepend one string onto another
2. However, insertion may also be required

##A generic datatype for the contents and metadata of a string
+ Struct is most immediate option, but class may be more suitable long term

##General string operations
1. A function to convert a string to upper case
2. A function to convert a string to lower case
3. A function to check if a string is entirely whitespace

##General character operations
1. A function to check if a character is a letter
2. A function to check if a character is numeric
3. (A function to check if a character is punctuation)?  

#Sorting and lists
##Sort integer array
+ Ascending or descending

##Check for the existence of a number in an array of numbers
+ The indices will be returned of each instance
+ An alternate option may only check if it exists at all
+ A further option may be number of times it exists

##Sort array of strings
+ Ascending or descending
+ Case sensitive or insensitive

##A function for the stable sorting of a list of structs that contain multiple parameters

##Check for the existence of a string in an array of strings
+ Indices, number of instances, or whether it exists at all

##Creation of a dictionary; or some such key-value array
1. It must be as easy to use as an array, and no less safe

#Files
##A generic datatype for the contents of a file
1. Containing all the lines of the file, and the total number of lines, the filename, and potentially the filestream (if all the lines were already read, there isn't really a reason to keep the stream open)
2. Basic functions for filling an instance of the datatype

#General notes
+ Where a function may have an option, such as case sensitive or insensitive, an enumeration shall be used in the function argument with clear values
+ Express versions of functions with default behaviour may exist, as may versions with different parameters, provided using the wrong one will cause a clear compilation failure

