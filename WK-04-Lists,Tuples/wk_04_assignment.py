"""
The is_palindrome function checks if a string is a palindrome. A palindrome is a string that can be equally read from left to right or right to left, 
omitting blank spaces, and ignoring capitalization. Examples of palindromes are words like kayak and radar, and phrases like "Never Odd or Even". 
Fill in the blanks in this function to return True if the passed string is a palindrome, False if not.
"""
"""
def is_palindrome(input_string):
    
	# We'll create two strings, to compare them
	new_string = input_string.upper().replace(" ","")  #convert to uppercase and remove spaces between words
	reverse_string = input_string[::-1].upper().replace(" ","") # reverse a string and remove spaces between words
	print("New -",new_string, " : Rev - ", reverse_string)

    # Traverse through each letter of the input string
	for x in input_string:
		# Add any non-blank letters to the 
		# end of one string, and to the front
		# of the other string. 
		if new_string[x] == reverse_string[x]:
			new_string = True
			reverse_string = False
	# Compare the strings
	if reverse_string:
		return True
	return False
    

print(is_palindrome("Never Odd or Even")) # Should be True
#print(is_palindrome("abc")) # Should be False
#print(is_palindrome("kayak")) # Should be True
"""


"""
The replace_ending function replaces the old string in a sentence with the new string, but only if the sentence ends 
with the old string. If there is more than one occurrence of the old string in the sentence, only the one at the end 
is replaced, not all of them. For example, replace_ending("abcabc", "abc", "xyz") should return abcxyz, not xyzxyz or 
xyzabc. The string comparison is case-sensitive, so replace_ending("abcabc", "ABC", "xyz") 
should return abcabc (no changes made).
"""
def replace_ending(sentence, old, new):
	# Check if the old string is at the end of the sentence 
	if sentence.endswith(old):
		# Using i as the slicing index, combine the part
		# of the sentence up to the matched string at the 
		# end with the new string
		i = sentence(old)
        
		new_sentence = "hello"
		return new_sentence

	# Return the original sentence if there is no match 
	return sentence
	
print(replace_ending("It's raining cats and cats", "cats", "dogs")) 
# Should display "It's raining cats and dogs"