import re

n = int(input())
s = input()

def delete_brackets(s):
	s = re.sub('\([^\(|^\)]*\)', "", s)
	return delete_brackets(s) if sum( [1 if re.search('\([^\(|^\)]*\)', s) else 0] ) > 0 else s 

r = delete_brackets(s)
print(r)
