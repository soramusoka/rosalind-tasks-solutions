# http://rosalind.info/problems/dna/

data = 'GCCCATAATACAATATGTCGTTACCGTTACGGGCTAAGTTTTTGTGGAATACGGATGACTGGGGATTTTATAATCTCCGCTTTCAATGGAACTATCGGTACTAAAGTCCCCTTGAATCCGCGTTGTTTGTATTCAATAGGAGATGGGGTTAGTGTTCACAACTAAAACTATACTTGGCAGCAAAAAATAGGTACCGACAATCCCAATTGATTAAGGTATGACCATGAGTGCCAGTGTGAGCTGATGGTGTCGCACATCCGAAGCTGGCTATACTCTTAACTCGCATTATTTACGTAGGAAGAATCCTCATGAGCATAAGGTTAAATAACACTAGTGTGAATTAAATTGCAGTATTGATAAGGCCCTTCGTCTAGCGCTTATATGCTTTGCGCATCACATAGCTAGGGATCTTTCCTGGCCGACCGTCGTACGTCAACTAGCGAAGACGGCGAATACGTATCTTAGTCTTACAGGTTATGCAATCTTACTTTACAGGGAGCTACAGGATAGGTTGGTCAATCGGGGTAACTATCTGACACAAATTTTATCATAGTCCAGCTTACCTATAAACCTTCGATACATGAGGAGCTAAGACACCCGGCGTCTTAACCGGGCAGCCAAGGTACTATACCTAAGCAGGATGAGGCTCAGCCGTTGGAATCTAAAGCGCCCGATATCGCTTGCACCGCTGCCATAGCGGTGGCATACGAGATCCTCGTCAAATTAGGCCCGAACTTGGGGAGCCTGTACCGCACTGGCACACATAACCAGCGGCTACAGCACATTCCTGATGAGGTTGCTGCTCGGTAAAAATGACGTGAGACTTTGGACCATGCA'
unique = ''.join(set(data))
unique = ''.join(sorted(unique))
result = ''
for char in unique:
	result += str(data.count(char)) + ' '

print result

#------------------------------------------