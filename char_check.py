#!/usr/bin/env python3

S = 'ab123' #alphanumeric true test
#S = 'ab123!' #alphanumeric false test
print ('Alphanumeric?',(S.isalnum()))

#S = 'abcd' #alphabetical true test
S = 'ab123' #alphabetical false test
print ('Alphabetical?',(S.isalpha()))

S = '12345' #digit true test
#S = 'abcd' #digit false test
print ('Digits?',(S.isdigit()))

#S = 'abcdefg' #lowercase true test
S = 'ABCDEFg' #lowercase false test
print ('Lowercase?',(S.islower()))

S = 'ABCDEFG' #uppercase true test
#S = 'abcd' #uppercase false test
print ('Uppercase?',(S.isupper()))
