# Create a notepad and write all commands: only the data, not the query
# Save the notepad in [file.pl]
# Use SWI prolog app
# Open SWI > File > Consult> [Select the text file]
# run the queries

% Addition
add(X, Y, Result) :- Result is X + Y.

% Subtraction
subtract(X, Y, Result) :- Result is X - Y.

% Multiplication
multiply(X, Y, Result) :- Result is X * Y.

% Division
divide(X, Y, Result) :- Y =\= 0, Result is X / Y.

#Till here u save in the notepad....
#------------------------------------

#Operations

add(5, 3, Sum).      
subtract(10, 4, Diff).
multiply(3, 7, Prod).  
divide(10, 2, Quot).  


#For the SWI: Prolog app
#----------------------------------  

#Output

[4]  ?- add(5, 3, Sum).
Sum = 8 .

[4]  ?- subtract(10, 4, Diff).
Diff = 6 .

[4]  ?- multiply(3, 7, Prod).  
Prod = 21 .

[4]  ?- divide(10, 2, Quot).  
Quot = 5 .
