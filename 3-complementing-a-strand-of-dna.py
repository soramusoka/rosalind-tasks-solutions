data = 'AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG'
data = data[::-1]
result = ''
for char in data:
	if(char == 'T'):
		result += 'A'
	elif(char == 'A'):
		result += 'T'
	elif(char == 'C'):
		result += 'G'
	elif(char == 'G'):
		result += 'C'

print result

