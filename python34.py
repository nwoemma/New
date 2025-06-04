def reverse(string):
    result = ''
    for i in string:
        result = i + result
    return result
String  = 'Emma'
print('The word you want to reverse is', reverse(String))