# def capitalize(s):
#     even = ''
#     odd = ''
#     for i in range(len(s)):
#         if i%2 ==0:
#             even += s[i].upper()
#             odd += s[i].lower()    
#         else:
#             odd += s[i].upper()    
#             even += s[i].lower()
# #     return [even, odd]
# # a = capitalize('adetr')
# # print(a)value = 3.456
# value = 98.3423
# approx_value = round(value)
# print(approx_value)  # Output: 3
# Two tortoises named A and B must run a race. A starts with an average speed of 720 feet per hour. Young B knows she runs faster than A, and furthermore has not finished her cabbage.

# When she starts, at last, she can see that A has a 70 feet lead but B's speed is 850 feet per hour. How long will it take B to catch A?

# More generally: given two speeds v1 (A's speed, integer > 0) and v2 (B's speed, integer > 0) and a lead g (integer > 0) how long will it take B to catch A?

# The result will be an array [hour, min, sec] which is the time needed in hours, minutes and seconds (round down to the nearest second) or a string in some languages.

# If v1 >= v2 then return nil, nothing, null, None or {-1, -1, -1} for C++, C, Go, Nim, Pascal, COBOL, Erlang, [-1, -1, -1] for Perl,[] for Kotlin or "-1 -1 -1" for others.
def race(v1, v2, g):
    if v2 < v1:
        return None
    relative_speed = v2 - v1
    time_in_hours = g/relative_speed
    
    hours = int(time_in_hours)
    minutes = int((time_in_hours-hours) *60)
    seconds = int((((time_in_hours-hours)*60)- minutes) *60)
    
    return [hours, minutes, seconds]

# Given a lowercase string that has alphabetic characters only and no spaces, return the highest value of consonant substrings. Consonants are any letters of the alphabet except "aeiou".

# We shall assign the following values: a = 1, b = 2, c = 3, .... z = 26.

# For example, for the word "zodiacs", let's cross out the vowels. We get: "z o d ia cs"

# -- The consonant substrings are: "z", "d" and "cs" and the values are z = 26, d = 4 and cs = 3 + 19 = 22. The highest is 26.
# solve("zodiacs") = 26

# For the word "strength", solve("strength") = 57
# -- The consonant substrings are: "str" and "ngth" with values "str" = 19 + 20 + 18 = 57 and "ngth" = 14 + 7 + 20 + 8 = 49. The highest is 57.
# For C: do not mutate input.

# More examples in test cases. Good luck!


def solve(s):
    vowels = 'aeiou'
    max_value = 0
    current_value = 0
    
    for char in s:
        if char not in vowels:
            # Calculate the value of the consonant (a = 1, b = 2, ..., z = 26)
            current_value += ord(char) - ord('a') + 1
        else:
            # Reset and compare with the max when a vowel is encountered
            max_value = max(max_value, current_value)
            current_value = 0
    
    # Final comparison in case the highest value is at the end
    max_value = max(max_value, current_value)
    
    return max_value
# Given an array (arr) as an argument complete the function countSmileys that should return the total number of smiling faces.

# Rules for a smiling face:

# Each smiley face must contain a valid pair of eyes. Eyes can be marked as : or ;
# A smiley face can have a nose but it does not have to. Valid characters for a nose are - or ~
# Every smiling face must have a smiling mouth that should be marked with either ) or D
# No additional characters are allowed except for those mentioned.
def count_smileys(arr):
    valid_eyes = {':', ';'}
    valid_noses = {'-', '~'}
    valid_mouths = {')', 'D'}

    count = 0
    for face in arr:
        if len(face) == 2:
            if face[0] in valid_eyes and face[1] in valid_mouths:

                count += 1
        elif len(face) == 3:
            if face[0] in valid_eyes and face[1] in valid_noses and face[2] in valid_mouths:
                count += 1
                
    return count

# write the function is_anagram
def is_anagram(test, original):
    str1 = test.lower()
    str2 = original.lower()
    return sorted (str1) == sorted(str2)
# ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.
# If the function is passed a valid PIN string, return true, else return false.

def validate_pin(pin):
    pin_number = str(pin)
    return(len(pin_number) == 4 or len(pin_number) == 6) and pin_number.isdigit()


print(is_anagram('ere','erew'))