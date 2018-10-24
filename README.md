# CS2302-find-duplicate-ids

## Running the program: 
This program requires two .txt files to run, an Activision ID file and a Vivendi ID file.
The Activision file must contain:
  * Any number of ID's ranging from 0 to 6000 (inclusive)
  
The Vivendi file must contain:
  * Any number of ID's ranging from 0 to 5000 (inclusive)
  
After providing the .txt files to the program, it will create linked lists to 
facilitate the tests, which may take some time depending on the size of the
two files. Then, the program will prompt the user with the operations 
and which one they wish to perform.


To find duplicates the program can:
  * Use nested loops
  * Sort the list using bubble sort, then find duplicates
  * Sort the list using merge sort, then find duplicates
  * Use a boolean array to find duplicates
  
After running any of the functions provided, the program will print the
time it took to run in milliseconds.


## Testing runtimes of each function:
Inside the main() function in the code, there are commented blocks 
that when uncommented, run each function 100 times and get the average 
runtime of the function. If using the test mode, it is best to comment 
the prompting part of the main() function to avoid interruptions.
