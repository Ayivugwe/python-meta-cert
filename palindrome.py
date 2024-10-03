#Function to check if a word is a palindrome

def is_palindrome(s):
    start_index = 0
    end_index = len(s) - 1

    while start_index < end_index:  # Loop until the middle of the string.
        if s[start_index] != s[end_index]:  # Compare corresponding characters from both ends.
            return False  # If a mismatch is found, return False (not a palindrome).
        start_index += 1  # Move the start index towards the center.
        end_index -= 1    # Move the end index towards the center.

    return True  # If no mismatches are found, it's a palindrome.

print(is_palindrome("racecar"))