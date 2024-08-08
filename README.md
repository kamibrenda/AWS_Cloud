## A breakdown of the labwork done in the AWS cloud
1. **Python <br />**
   *a. composite.py <br />*
    The WITH OPEN syntax statement, keeps a file open while you read data.
    It will automatically close the CSV file when the code inside the with block is finished running. Python does a shallow copy of complex data types. <br />
   A shallow copy refers, or points, to the storage location of the myVehicle dictionary variable. Without this line, you would have only one storage box, and only the last item in the list would be copied into memory. This line makes sure that new storage boxes are created in memory to store the new tabular data that is being read. <br />
   
    *b. conditionals.py <br />*
    The == symbol is a comparative operator. It means is equal to 0 
    **Pseudocoding** - write out the logic of the while loop in written (non-code) sentences
    For example; <br />
        1.If the user has not guessed the correct answer, enter the loop. <br />
        2.Ask the user for a guess. <br />
        3. Is the guess the correct number? <br />
        4. If the correct guess, tell the user it was the correct guess and exit the loop. <br />
        5. If the wrong guess, tell the user it was the wrong guess and continue the loop. <br />
        
    A list is generated by the range() function. The range() function takes a starting number and an ending number, but the ending number is not inclusive

    *c. calc_weight_json.py <br />*
    #code exp a:*open* -returns a file handler to the files/insulin.json file. <br />
    #code exp b:*json.load*- reads the JSON file and returns the content as a Python dictionary. <br />

    *d.debug-ceaser-1.py*
     A traceback is a stack trace that starts from the point of an exception handler which then goes down the call chain to the point where the exception was raised in short an error occurred. <br />

    ### Bonus: Cleaning preproinsulin-seq.txt programmatically
    Cleaning source data files is a common task in computer programming. You could programmatically clean preproinsulin-seq.txt in several ways—for example, by using Bash, Python, or another programming language of choice. Try using regex to programmatically strip the file of ORIGIN, its numbers, the two slashes (//), spaces, and line breaks or return carriages. You could also confirm programmatically that the file has 110 characters.

**2. SQL**
    • IBM and Oracle: When you are processing code that you write, IBM and Oracle database management systemsautomatically convert identifiers to uppercase. (That is, they will ignore the case that you used.) To retain the case that you used for your identifiers, you must enclose them in double quotation marks (" ").

    •Microsoft SQLServer: Microsoft SQLServer can be configured to be case sensitive or not case sensitive, but it is case sensitive by default. Case sensitivity is associated with the collation properties of SQL Server, which determine the sorting rules, case, and accentsensitivity properties for your data.
    
    •MySQL Server:MySQL Server is case sensitive by default except in Microsoft Windows.
    
**3. Amazon Lambda**
     The *salesAnalysisReportDataExtractor-v3.zip* file is a Python implementation of a Lambda function that makes use of the PyMySQL open-source client library to access the MySQL café database. This library has been packaged into the pymysql-v3.zip which is uploaded to Lambda layer next.
