## A breakdown of the labwork done in the AWS cloud
1. Python
Notes 
a. composite.py
The WITH OPEN syntax statement, keeps a file open while you read data.
It will automatically close the CSV file when the code inside the with block is finished running.
Python does a shallow copy of complex data types. A shallow copy refers, or points, to the storage location of the myVehicle dictionary variable. Without this line, you would have only one storage box, and only the last item in the list would be copied into memory. This line makes sure that new storage boxes are created in memory to store the new tabular data that is being read.

b.conditionals.py
The == symbol is a comparative operator. It means is equal to 0 
pseudocoding - write out the logic of the while loop in written (non-code) sentences
For example<code explanation>:
1. If the user has not guessed the correct answer, enter the loop.
2. Ask the user for a guess.
3. Is the guess the correct number?
4. If the correct guess, tell the user it was the correct guess and exit the loop.
5. If the wrong guess, tell the user it was the wrong guess and continue the loop.
A list is generated by the range() function. The range() function takes a starting number and an ending number, but the ending number is not inclusive

### Bonus: Cleaning preproinsulin-seq.txt programmatically
Cleaning source data files is a common task in computer programming. You could programmatically clean preproinsulin-seq.txt in several ways—for example, by using Bash, Python, or another programming language of choice. Try using regex to programmatically strip the file of ORIGIN, its numbers, the two slashes (//), spaces, and line breaks or return carriages. You could also confirm programmatically that the file has 110 characters.