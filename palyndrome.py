#Function to check if a word is a palyndrome

def is_palyndrome(str):
    start_index = 0
    end_index = len(str) - 1
    
    for c in str:
        if str[start_index] != str[end_index]:
            return False 
        else:
            return True
    

print(is_palyndrome("racecar"))