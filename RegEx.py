# A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
# RegEx can be used to check if a string contains the specified search pattern.

'''
These are metacharacters used for RegEx pattern identification:
[]	A set of characters	"[a-m]"	
\	Signals a special sequence (can also be used to escape special characters)	"\d"	
.	Any character (except newline character)	"he..o"	
^	Starts with	"^hello"	
$	Ends with	"planet$"	
*	Zero or more occurrences	"he.*o"	
+	One or more occurrences	"he.+o"	
?	Zero or one occurrences	"he.?o"	
{}	Exactly the specified number of occurrences	"he.{2}o"	
|	Either or	"falls|stays"	
()	Capture and group	 
\1, \2, \3 recalls the group section for example ^([ab])\1$ means either a or b, and either the group 1 (a or b)
?: stands for non capturing group which means it's not going to be possible to save its group information with a slash (\1 doesnt work with these)
'''

import re

# lets to a little test, create a regular expresion that valids all strings that start and end with the same character no matter
# what's between them as long as the start and end are the same. An example of valid input is: "aba", "a", "c", "cac", "afiu2o2nchdk2a"

user_input = str(input("write anything u like here but make sure it starts and ends with the same letter:\n"))
print(user_input)

x = re.search(r"^(.)(?:.*\1)?$", user_input)

if x:
    print("Your input was valid.")
else:
    print("Invalid input")