def Text(i,k,text):
        subsetArr = []
        for letter in range(i,i+k):
                subsetArr.append(text[letter])
        subset = str(''.join(subsetArr))
        return subset

#-------------------------------------------------

def HammingDistance(string1, string2):
        distance = 0
        for i in range(len(string1)):
                if string1[i] != string2[i]:
                        distance = distance + 1
        return distance

#-------------------------------------------------

def ApproximatePatternLocation(text, pattern, d):
	location = []
	for i in range(len(text)-len(pattern)):
		pattern2 = Text(i, len(pattern),text)
		if HammingDistance(pattern, pattern2) <= d:
			location.append(i)
	return ' '.join([i for i in location])

print(ApproximatePatternLocation("GTTGGATACGCAGCGCCGTCATCTGCAACGTTTCTGAGTGTTTCGCGTTTAGCGCCAGACACAGAATTTTTGAGGGCACTGTAAAGAAGAATGCGACATGACGCCGACTCTACTGATAAAGTACAGGCTGACTCAGAACCGTTAAGATACGGATATGGTAACGAGCACAGGTAATTTGGGGGGTGACCAGATAGTCCGGCAGCTGCACAACTGTGAACAGTAGTCCCCCCACACTGCATAATGGATGGGTATGGGAACATTCCGTGACGTAATCACTACTTTAGAAGCTTTGACTCGATTCCGACCATGAGCCCATTGCGGCAGCAGAGCTTCAGAAGGATACGGAGAAGTTAAGCTGGTTGGTATCATTCCATGATGATGGTAATTCCTACATCGCTGAGTTGGGTAGTTGTGTATGAAGAACATGGGTGGACGATGAAGCCCCAGTATGACGACTAAGTGTGCCAAATGCTAGTCATGAAAGTCCTTTAAGCCCAGACGTCAATGACACACCAAGCAGCTTAAGATGTTCGTCTTCCAAATAAGATGGTGCGGTCCCTATCCGAAACTAATTAGTTCAAGCTCGGATTGCCGAGGGCCCTAGACACCCTGAATTCTTGTGCTCTAGGGAGACGATAAGAATGGGGCACTATTGCTATTCGCATATTAACACAGGCTGCCTGTAAATGCTTGGGCTAAGAGCAGCTATCTCTGGGTCCCGCCCCAATAATGCCGCACATTTTTGCAGGGGCAGTTTCTTGCATCACTCAACTCAACCCAGTGTGTATATTATCAGCTGGTAAACTTTAATGACAAGAAAACGAGGCGCTTAGCTAGTGGCAAAATCCTGCAGAGATTGGTGGTGCCCGCACTTCGACGGCGCACCGGATAAGTCCTTTCTCACATCTCAGATCTCAAGCGGCGTGGAATCTTAGCATTACTGTCCCACAGCCTTGCGGATTACAGTCCAAGCGAGTCAAGATACGACCCGTTCCAGGCTGGCTTCCCTAGGGCTATCGGGTAAACAGAACTTCATTTCACCCTAAAAAGTGTCATCATTTACCTCTTGCTCCAGTCTAAAGAGCGCCTAGTCTTAGAGTGGAGGGTTTCGGCCCCCTTGTCATTTATCAAGTCCCGTCCGTTGCAAGACTGAGAAGGAGGAGTGCCGCGCAGACTAAAGCGTCGTAAGCATGTGGAGCGCCTAGAGGGCGTGACTGATCATAATGGTTGACCGACAGTTCAACCCGGAACCGAGCGGCACAATATCCCCTAGGAAGAATTCACCGTGTTCGATGTCTTAGTTGCGACCGCTGATTTGACTGGGTGCATAGTATAAACCAAACTTCATTCCTGTGGGTGCTGCATTAAGGGTATTACTCTGATGCGAGATCCCCAGTCTAGCTGGTTTCCCGTTGTGGGCCGGGCCCTGCAGGCCCGCGCAACTTGCACTGCAAAGATTATGAACTCGGTAGCAGTCTTAGCAGGATTCTTCGAAACGGCGCTCCGTGTTAGGTTTGCAAGTAGATGTCCCCCAAAGATAGCTCAATGCCCACACTAGAAGAAGGGTAATAGAGTCATCACTCTTAGGGGCGTGTTACACACCGAGTATGCTACCTTACGCTCGAACAAGTATCAGATGTTCTTGGATTCGCGCGGTAGACCATCCTTCTGAGGGACCCTCCAGATGTTGTACTATGCGAGCGTCGGAATCGCAGCTGTGACACCATTCTGACGTTCCGTAAAGCTTGAGCACCGTTAGTCGAGCGTGATAGCCAACTCCCGCTGGTTTGTATTCAGGGCCAGATGGCTGAAGGAGGTTTGGTGAGTTGGCACGCAACGAGGTCACGAAGTGTCTTGTGCTGGAAGGACAATTGTGGGTAAAGGCTAACACGGTTAAACAAACCGTACTAGTCCTCATCACGGCATTCCCCTAACGAAATATCCGTGCCCTTATAGGAACGGCCGTTGACTCAGTGGACCAGATAGCTAGAATAGGAAAGAGGCATGAGAGTGGCTCGGTTTCAGGAAGCGAGGCAATCCCACTACCGAAACTCCTAGAGTTATCCACAATAGAACCGTTGCGTCATTGTTTGATGGTCCTCTAAGCTAAACTATGGTCATTTCCCACACCCAACCTTATGCGTAAGTAATTGGCACAAACAAGGACAATCCGAAAGAAAAGGAAAGCGCGTCACAGGAGGTTGGGTACACGGCTAACTCAGAAGGCCACGGACTATTAAACGGGTTGAAGGCTGAGTGCAGCAACGAGTCTCTACGCTTTATGTGACTATGAGCAGTACAAAGTGCTCCTGCAGGTTTGGCTATAGTTCCATGTTGGCCACATCACCCGCAGTAGCGCACATGTACCCTTTCGAGACACCCTATCCGGTGACTAGATGCAATAATCTCGTGCCCGACTGCGGGCAATGTAGAGAGGCAAGCCCGAGCGGTGCCCTCATACGCTGGCTCCTTCCTAGCAGCGGTGTCCCCGTAGGCCGTCTCATGTGCGGACCATCAGTAATTCTTGGCAGGAGGAGGCTACTTAGACGGTTCATAATTTTGGGCTGCTTTTGCCCCGCGGTATTTGGGTTCGTACATGAGCCTTGCGTCGTGTTTGCCGAGTGACAGTGTTCGAGTATCAGTCGGAAAGATATATGTAAATCATCCGATCGTTCGGGGGAGTTAAACGGGGCCCTTCAAATAAAACCTAGCACAGATGTCGAGAGTCCAGGGATGCACGGAGTTACATGAATTACAAGTCCGAGGCAGTCTCTTATCCCGCAAGTTTGCTTAAGAGTTCCCTGCTAGACTGCTTATTGACGCATTAATACAATTGTAACCCGTCCCATTTAAATCAAAACACCTAAACCTGTCATGGACACTCAGCCTTCGAAGTTTTAGCATGGACCAATAACCTGCCATCCGATGAGGAAGTCTATCGAGGCACGATCCTCGCTGCAATCTACGGTAGAGAATCTGACGCGCGTTGCGTCCGATGCGTACCACCGTGACATTGGAGCCAATTACAGGGTTCCTCCAAAGAAAAGTAAGGTATTAGCAGCTGCACTTTCATTTTGTCAAGCATGTTCTTTAGCATAGGTCCTATCCCCATACACCCAAGTACAATCACCCATTCAGTGTCACTGCTGCCCACTGTACTAAACTATGGTGGTCGACTGTCACGGTCGTTAGTGTTTCTGCATATGGGTGGCTCGCATAGTATAGAAGTTACAGTCCTTTTCAGAAAAAACGCGACACAATATCGCACAAGGACCGAAAAGTCCCTAGAACGCATAGGGGACGCACATAGTCCAGACAGTTCCCTGCCCGTTCTACCGTGAGCTGTTCAACCTGTAGTATCTGTGGTAGCCATGCGTCCACGGACCGGCAGCCACGTACCTGTCAAGGCTGAATTACGCGCAAAGTTCCCGACCCGCGTCAGGCCGCCATTCTCCACAGCCTTATTATCCAGACGACCGATGGGAATTCAGGTGAATCAGAAAGGGTTTTCCCGCGTATTCCCTAGACCCGCGAACATAAACCAGATATTCAAGTAGGGGAACCGCAAGCGGTTATTTCAGGTATATAGGCCCACCTAGACGTAAGGAAGAACATTATTTCTGGGTCACGGTTATTAAGTATCTCTAGACGAGATATCGGAGTTATTGAAAATAGCCGCAGATTGCTCCTTTCAAAATTGCCGGTATAGCCTACTTCAAGAATCAGAGCAGTTGCACCGCCACATCGAAAAGGACTGATGGTCAGGTTTCTGGACTCCCCTCGGTCATGCGTCAGACAATGGCATTCTATCCCCACTGCCTAGGATGTTGATCTCGCTGGTTTGACACGCTTTAAACCAGGAATACGGTGATAGAATACATAGCTCCACGATAAGGTCCGCATGCTCGCTACCGTAGTCGCGCTAGGGGAGTGGAGTGCATTGGATAAACATCTCATATACCACCTTGCTTCAGCCTCTCACAATAAGTTCGAGTTAATGAGCAAATCAGAGACCCGTGCCTGCCGCCTACTCCTGGGTCGATGAAATAAAACCTTGTTCGGAATGTAATAAGGAGCGTAACCACTAAGGGAGATGAACGTTCGAATGGGTGCGAACTTGTTTATCGGCGAACCACACGTCCATATGTACGGAATATAATCCGGTAGCGTTACTAACGTACGCGCGCTCGATGCGGTCCGCTGTCAGAGAAAGGGCTATGCATTGCTCAGTAAATCCTACAACAGCCTCCACTGCGAGGGAGGCGCATGAGAGGCAGGAGTACGTTTGTCGCCTTGTAAGGTTCACTCTCCCTTGGTTTGAGTTAGTTCTCCGAGTGTACTTATAGCCAATGCGTACGCCGATTGCGATTACGTCCGGATCGATAGATTCTTCTTTCCTATGCGCGGCACCACCCATGCACGCCACACAGGACAGACCTATAATCTTAGTAGACGTCGAGTCATGTATTCTTGCTCGGGGCGCGGAGGGAGGGACGGGGACAGGAAGCCGGTAGATGTGACTTGCGGAACTTTTGGGTTGACGCAGCGCTAGGGGGACTGGATCGATTAGATCAACATTTCTCACGGTCTGAAGGCACGCATTGGTCAGTAATAGTTAAAGCGTTTACTGCTAGCTATCCTATGGGATAATATTAAATGTGGCTAGCTGGGCTATCGTTGTCCACAATATGTTATGGAGCGACCCAACTGCGGAGATTGCTCGGCGTATTAGCAATCATTAGTGGCCTGGCGTGCAACGCCACAGTCCATGATTGTACCTCCAGGTCTGACTGGAGAGCGTTGCTTCGCCCTAATTTTGCTGTTGGTTAGGTTGCGGCCTGAGGTGGTGTAAGGCACGGACAAACGTTAGCATCGTTTACAGGTTAAGGAGCGTCGTACAGAGGCGTCCCCCATTGAGTTTCTCGAGAAGCCTGCGTTGCGGACTTTTCTCTGTAGATCAACATTATGCCGAATTTCCTAAAATTTCACAGGAATTTAGACACTACTTCTTATTACTATCAACGCTTCAAGTCGGTTCTCTGAGGGGACTGCGTTCGATCGTTGCTTCAGGCCATTCGCGACAGTCCATCGCGACGATTCCATTACCGCCACATACGCGCGCGTGGATGAGCATATTTCGGACACCAAGGCGAAGATCAATTGTAATATCTAGAGCCCAGCCGCTTTCTCGCGCTGTGTGTCGATCCAACGCACAATAATCTGGATTGAGTCGCCGACTGTGGGTCTTTACTGGAGATGTACCTTGGCCCGCCAATCAATGTGCTTGTCGGCAACTTCCGAATCGACTGATAGCTCGACCGACGCAGTAATATAATTCAGCGGTAGGGCTGCCTTAAACAAGGCGGGCCAAAGGCAGTCATTTCATCCAAATCCCGGTGGGCGGTGCAGAGTGAATCTTGTTTCAGTCTTACGAGTTTGTGATTCATTTTGTGTGCGGAGTATTACCGGACAAGGTGGGCGATCTCGTCTGGAGTGGTTAAATGGCCAACCAAATAAGGGGAATGCCCGACCAGTCAAGATCTGATTTATAGTCTTGAGACGACTACGCTGTTATCAAATTTGAAACCATCTGAGCCACACTTACACCAGGGAAAAGCTGAAGGCCTCTTCTAGAGTCTCCAAGTACCTCCTACCACTATTTCTGGTTTATGCGCCTTAGCGCGTTGTGCTAATAATTCCGGAGGCCCGGTCAATTGAAGCTCCGCTATACGCGCACACGCGGCATATAATCCTCTTCCGTATGCTTCTCAGGCTGCTTCGAAGGCTGAAAGTTTTGTGTAGATACAAGGGTAAGTGCGCTTTTGAGGAGGTCGTCTCACGACTTAGGAATAAGACATGAGCACCCCTTTGATTGAATTTGGAACTTGTGCGGTTGCGTAGATAGAATGCCGCTGTGTTGAGTAGTATATGATTTCGAATAGCTTGGGTCTGGCCCCTACTTACCCTACAGCGTACTTGCGGACACTGTAAGTAGGCAACCAAATATTGATTTTGCAAATGTTGCTATGAAGACTCTCTCAGTGCGTAGTCAACTGCGGGGTCACGAGCTGTGCCTATAGCGGACACGGGGATGCACGTTCATAACCGACGCAGGCGCGTTACCTCTAGCAGTCAATAATGACCACTAAGCGCGCGTTCAGGTAAAGCGTCTACAAGCAGTTTCGACGTTTTGTTCGCCTGGGATCCATTAAGTCCAGGACGTCTCGAGATACCAGTACTTGGAGATTCTACCCCAATAGCGACACGACAATTTCAAAAAGGGTCAAATTCGCATAGCTCGCCCTCATCCGTATTATGACTCATCCTCTAAGCCTAATGTCAGCGGGCTATATTCCGAGTCAGAAACCTAAGACCGACAGTCATAGTCGACAAAGCTTGAAACACCGTCTTGTCCCGGTTCACAAGAACTCTAGACTTGTATGTATTGGAGAGATGCAAGTAGGTGCCAGGCCTGTCTGACCGCCTTGTAGCTATTAATACAGAGTTACTAGGCTAGTAGAGGTTTGACAGTAGTACGGCCAATGCTACTTAAATTGATCGTTCTATCTCTCATGATAAGACGTACCGGCGTAGATTAGATGGTTATTACTACACGAATTATCGAAAAGTGGGACATGCCGGCACCGGATTGAAATAGAGTACTGTAATTCTCCGTCATGCGCAACAGTACTGGAGAGTGATTTCTGGTCGGTTGGTCGTCCTCTTTCTTTTCTTAACTGGAAAAGGGCTTTTGGTTAAACTAATTGCAAAGAGATCTCATGAGACTGCTACCAGTCTCCGGTTCATACAAATGGGCTTGGTTGTCCAAGTTCCTACAGTCATTACCTCGCCAACAATGCGTGCACGACATGGCACTTCATTTTATGGTCATGTTCAGTGTCATTCCAAAAGACCTGATACTGCTGCTCGGAACCTATCTTCATTTGGGGACTGACCCATGATCCGATCTAGTCGACCTAGCACTGAACCTTGGATACCGGAAATAGGGTAAGGTTTAAGTGACCCGGCTTTCTATATCCTCGTCCTAAGTATGGCGCATCCAGGGCGCGTCTTCACGTTGAGTGCTGCCATCATTGACCAAACTGTGTGACTGTCGGAGTAGTGGAGGTAAAAAGCGCCGTCCGGGTCCGAGGTACATCATGGACGAGGCCTAGCCAAACAAGAAACAGCTGCATCAGTCCCACGTTTGTCGGCGCGCGTTCATCCTACGGAGTGCTTTCGTTGTCAACGCGTCTTGGCATCTAGTGCCACCTTCTGACTTTGGGACTAGCATCTGCGGTACGACAGGCCAATATAGGCTCCCTAAGTAATGGAATTGGATAAAGTTACAGCTTAAAGAATTCACTTCCAGTAGCACGGCTTACTAGGGCTGGGACGTAAAGGGCAGTGTACCCTACTCGAATTACGAATGCTGTCATGCGAGGTTTGGCCTAGCCTTTCGGAACGTCGTAGGATGGATGCAAGCAGTGTACTGACCCAACCATACCCGATTATGAGATTTTTATGGAGTCCGAAAAATCAGCCCTGTGGAAGAGCCCAGCTAGCGTATGGGCCCGTGCCCCTTTTTTAAATGATATTTTTCCCAAAACTTTTGTATGGCTCGGCTCCCGAATACTTTCCCGTGATGATGGGAAGTTTCTTCCGTAGCGAACTCTCTACACCTCTGCCCGATACGTCGGGCCTCCATTAGGATACGCTGGCGCCTCTATTGCTGGCATTTCAAGAGGCTTCGTGATCATCTCAGTGAGCCGCTCGAAACGGGGCAACCCCTCATGTTATCATGACCTTTATGAGTTCGAATGCGCTTGGTTGACATACTAACTGCATACCGCGTTATTTTAGACTCAATGTGACTTGTTCTAAGTTTGACTCGCATGATCGCCATACTTTGAAGACATAAGACCGTCCATCTGCTAGTTCCGCAGTGAATGACTCGGGAGAGGAGTTAAGGCGGTACACCCGGGGTGATTGATCTGAAACCGGCAACGCCTACATCCTCGAGGGAACAAGTTCGATACCTCTCCCGCCGTGTGAGTTATGTGATTACTCCAAGCTTGCACTCTAGGTACGGTTATCCAAAGTCAAAGTTGTGGACGAGGACGGCGTCGACTGAAGATATATAACAGTTAATCTCCGCCTAGTAGGCAGGGCTGGATACCTCTTTTCAGTGCCTACACTAATCCGTGGACGCGATGGCGACCCTCACGGATTCGGAATTGTTTGCGAAGTAGTTGGACCTACCACAACGCTTGGATTGCGTGACTGGCTACCAAGAGGTACGTTAGTGCCGATCTCTATCCATTTTTACACCATCATCACCGGTGAAACCACAGCGACCTCGCGTAAGCTGGAAATCCTGCAGCCATATCCCTCGCGGAAGGAAAAGGTGGTGGAGCTATACGCGGCTTGAGTGAGATGGGACTTTAGACTATGAACTCTCTCACTAAGATCTCGTTCCAGCCATGCGAAGAGATACCAGTACTAATTTCATAGTCTCGTTTGGAAATGCCTGGGCGGACTGCTAGATGACAGTGGAGTGAGCGTGGTTGGCTTTTAGAATGATAGTCAGAGGGTGGATGCATTGGACCTCTTAGGGCGACCGATAATTCCTTACGGGCAATGGCCATAACACTAGTGCAGAAGGACAAGGTGTGGTAGACTCCTGACCGTTAGTATCTCAATTCGTGCTGGCGGCGTCAACCTTCAAGGCGGTTGACATCTTTACTCTCCGTGCTGAGATTCATGATTCCCAAACGACTTGTACTCTCCTGAAGGGATTTCGACGGTGATCCTCCCAAGTACTGAACTGGTTTGTATGCTTAGTACCCTGGCCGGAGGGAGTTCAAACCCGACACATAAGCTGGGGTGTAACTATCCCGCTAAGATTCACCTCTAACTTCTGCTGTGTACAACGCCCCCTGGATAGACACACAACGGTAAATTTTGAAGCTCATGGTGTCCCGAACCGGAGCATTTACCGTCATCGTTAGCTGGCTGAGTTCTGGCGCGGCGCGTAAAGACCACTGGCACGCGGTTTACTTTTTAACACAAACGCAATCTGAATCTGTTTGCAAGCAGGTGTGCCAGGTCACTAGGCCGCCGGTCGTCCAAATAATGGAGCCAGTCGCCGAATGCTTTGTCGTCAAGTATCTCAAACGCTTTGAAACCCAGTCCCGTGCGAAAGATCGCCAAGCCTTGAGGGACTCTCATCTGCGCAGCATAACTCACACCACGTCTGTTCGGGGCGTGGATAAGCCCACATAGGATTCGGAGAACGGCGGACGGTTGATCAACTGCCATTCGATCACAGAGGAGTCGGCGGGAGAACACACGCCTTCTCGGCGATCCACCCGAACAGCCTTGGACCTTGAACAGTGGAGTACAACCCAGTTCCCGGCTATGCACCATTTAAGTAGATTACGCTTATATGTGCAGGATGCGTGAGAAGAAGCTGCTGTTAGGGCCGCCGGCATAAATCGCGGAAAAGATTACATGGCACTCTTAGACCATCGAATGTCGCCTCCTGTTGAGTTGGGGTCGCAGAGATGCGCGGGCTTGGTCTGCTTCCTGAGAGGCATCTCCAGTGATCTGTGATGTGAGGTATTCGCCGGTGCGATAGACATCATCTTCACATTCTTACATGGATAGCCATAAAAAATACGCAGAGCAGTTCCGCAGCGTTGGATCTAGAAAAGCTACTTGACGGGCTAGCGAAATTCGTAAGGTACAGTGGGCCTTTTAACTCCCGCGTTAGCCGGACCGAGACTTACACTCATGTCGCGATGAAAGCAATCCGTCAGAGGTACGCGTCTATGCCGGTAGAAGTCCAGTTCTGCGAAGGCTCGCACTACACTTCGCGGGCCCCCCGCCCACTACATTCAAGTGTACGTTCGGTTGACGCAAGTGTCTATCAAATAATGAGGTATTAGGTCGATTCCAGCCTAGCTGGCGTCGGTGTTATGCCATTTATGTACTCATTTAAAAAGTAGAGCGCATCCAGCACCGTTGAACGTTGTTCTAACGCACTGAAGCTAAGCATTAAAATTTCGCAGACTGCTAAGCTGTTTTTAGAGGGAGGCTCGGCCGCGCACCCCGATCTAGCATCTGACCTTTTATTTCATAAACGTCACCGGCCGTACGGGGATGTGGTCTTCTCAGTGCATGCTTAGTATCGGGACAGCGTGGGCATTTCGGAGAAAGGTTTTACCATCACTGGCGATCGAAGCCGAATACTACACCGATACTTTTCCTTCTCTTGCTGGACAGTATCCTATCGTATCGGACAACAGGCACTGGGGAAGAACGGAAGACCTCTTCTTTTGAAATCCCGCCCGGTTGAGAGGAGCAGGCGTCCTCCCTCAGCGCCGATGTGGGAAAAATTACTTGGGTGATGAACACTCACGAAGAGGCATCGCCGAGGTTCAGATTGATTTTTTATGTTATACTGTCGCTGATACCTACTCGGGACAGCTACCGCTGTGTATTGCTATGCGTCGAACTCCCGTGAGGGTCTTAGAGTTGGCAGGGCGTCTACGGCTTTTCGAAGCCGTAATATAACGGCTCGTCGCATCAAGTGGGCGCCGGGCTTCCCAAGCTTTTAGGGCCGTCGTACTCGAAAGGCGCTGAAGCTACCACTCACATCACAACCCGTCTAAGAGGACTGGACGTTGGGCATCAAGCTTCGGTAGAGGGTACCTAAGCGACCATTAATTGTCGATAAAGCTATACGTTAGGCGCGATCCTTACATATAGAGACCGTTCAGGCACTTGTCCGTCGATGGTCAAGCCTTGGGTGGCCTTGTCGGTGAGACAGACTCCTTAGCAGAGTGCCCCTGTTTAGTCAATGAAGTGGAGAGTGCCTCTGACTTCGGGTGGAGTACCGCTACTTCCGCTTATCTTGGCGCGCATTAGTGCTCATAACGTGCAGCACGCAGGAGATGGTCCGGCGGATTTCCCTTTACGTCACCCCTATTAGCACCCGCAGTTCAGCTGAACGTCGGACGTCAAAGCTGTGTTTCCATTGAGGCAGCAAGTAGGGTATTGGTCAGTCGGCACCAGATAAACTTAAGCAGCAGTCCCAAATATAGCTCCATCTAGTATATGTCTAGATTACCCGCCGATGTAGATAACTGATAAGCCCAAATACTGTCAAGTTAGGGCCGGGAGCTCTACTAGCCGGACAGAGTTGCAGAACCGCCCAAAGTTGAGTGACCCGTGAGATGTAAGCGTGACGATCCGAATCCCTCACTCTGGGTTTGCCAGACTTGAGAGGGTGCCACGCGGTACCGATTAGCTATTCCATCGTGTGGTTGAGTAAGGTCCAGTGACGCAACTGCCATGGATGCGATACATAACCTTTCGCCCCCTAGCCGCGCGCAGGACGGTTACGAGTAAGGATTACACGAGATTCCACGGCTGATCCAGGAACACGTTGACGAGGACGTGGCCAGTTTCTTCCCTTTGGCAATTACCGAAATAGGGTGTGATTCGCTATCTAATCCAGGGGTGCTGAATTTGGACTAAGAGCCTCGTCATAAGATCGTGAGCCACTTGGTTTCTACTGGGTAAGGTGAGTACCCAATCAAGTCAAATATGATGTTTTAAGGGGAACCTTCCCGCTCAACTGTCGATCGGCTCGTGGATAGGACCCATTTGCGTGAACCGGACGGATTCGGGCTTCGCCTTATAGTATCTATGCTCAGAAGCAGATGGAGTTCGTTGGCAAGATGCAGAGATACACCCACCACGACTGCGCGGAACGGGAGACTTGAAACAACAGCAAGTGCGTTGAAACGGAAATACTTCATTCATCGCCAATTCAGTTCTAAGATACAGGAAGTCTATCGTAAAGGTGCAGGCTGTTTCAATTACTCTTTGACTATAGGATGTCAATCGCATCCCGCTCGCACGATGCCCCCGCAGGGCCAATCATAGTCGTATAAAGTCATGGCTGCAGATGTCGGGGTAAATGACTGCCCTCCAAAGTCGGTTCCTGAACAAGGACCACCGGTTCGCGGTCGAATGTCTGCATTGCCCGGATTGTTGCAACTCCTCCATATGAATTACCTTCGACCTGATGGCTGCTCGGTTGAAAGGAATGAAACTCTCTGAATTGTTACCGCCCGGTGTTGTTGGATGCTCGCGGTACCATATATTTATTTCAAGAAGACGCTGGTGCGGCGACGCGTGATGTGAACGGAAAGCTTGAACCCACTCGGCTCTGGGCATATATCGTAACGAAGGGACCGGAAGCTAGTGACACTCGGCCCTATGCTGAGAATTCATCTTTTACTGAGACCACAACGCGGGGATCTGAGTCTTCGATCACTACGATATTCCCGTTGCTTGACCCTGAACTTTTGACCAACTAACCGCCCAGCAGACCGGTGCATGCGCAGGAGGAGCCATTCAAATAAGTGTGTCCGTAAAAACGTAAAAGATAATATACGAAAGTGATTCCGACAATGAGGCCTTATCTTATAACTAATTACAACGCGTGCCATAGTAGCAGTACCCGACGCCTTAAGCAGGAAACAGCTGTATGGACGGTCTGCCGATGAGCGCGGATCTAGCCCGTGATGATCGGTTTTTAAATAGTCCGATTGCTGCCCCCGGACGGGCCATGTTGCCTCAGACCGCAATCTATGCAGCCTGTTACGGATAGTTTGCGATCAATCCTCAGAGTGTAATGTGTGTCCTCTATAGATGTTGAGGGCGGGTACTATCCTAGCTCTACCGAGGGTCTAACTGTCCCAACTTGCACAGGATATTGGGGGCTTTTCCCTAACGCAGACTTTGTTATTTTGAACATGTACTAAGGATCTTCGAGTTGAGAGTCCCGATTTGCAGATTGTGATCCTTCACTAATCCTAGAGTCAGCGTCGGGCTGCTGCACCGTCACCGTTTCAAAACTGACCTCCGAAATCCGATAAAGTCGGGACAGGCCATACTTCGGCAAGCACATGGTGGTCCAAGACATCTAATGCTTTCGTGGAACGAACAATACTACTGCGGCTCGGACAGATCAACGGTGTATCGGCCATAACCCGTAGCTCTGCAACAGTAGTGGCCGTGAATTACAGGCGGTACAGTTTAAGAATTCCAGCCGGGGTCTGAGTTTTAAACGTCGCTGGTCTGTTCGCTTGTGTCATGCGAGGTAGCTTGCTACCCATCGGGGGGGCTGTTAAATATGCTTAACTAAATGGATTGATAATGTGTGTGCTAGAGTAACCCTCCACCCCCGCCCAGGCTATCTCTCGGTCTGCGAACATTACTGTCCCCCCAACGATGTGTTGCCATTCACCATCATGCAGCGTAACATTTGGGGTAGATCGATCTGAGACGAAGCCCGATTGGCTCTCCGTTCAGATTTCCTTGCCCAGATGAATGCACTCTGTAGAACGTCTTGTCATAACCCCTACACATCAGTGACGTTGACACGACCTTTGTTGTTCTCCATCGTCGACAGCTCCTTCTAAGCGAATTCCGGGAAGTCCGCGCCACCCCCGACGCGCTATTATCAGTCATGGCCCCCTGAGGCATTTGGCTGCTTACGATCAACCATTCGCTAACGTTTATGAGATCAGTGTACATAACCGACTCATCACGAACACGAAGCTAGTAAAAGTTGAGCGTAGACAGGCGGGCCATAGATGGATTACGAACCTCCGAAGTCCCCTGACATATCTAAGCCGTAATCCCGGCACGTTTTCGACGTATGGGAAGACGTACGCCTCATTTGCCCTCCTTTCAGGACTTGTTTTCTGAAATGCGCGACGAGGCGCTGCACCGAACGTCAGCCCAAATCTTCTGACAGTCACGGAAATTAGCCAAACCCCTCGTAGACTCCTTGCGGTCCGGGGGGACTGGTCCCTCCTTGCATCGCCAATTGGGTCTGAACCGTTATGCCGCTGCACTCGATAGTTCCTCCTCTATTAATTAAACAGCATTCTACGTTTGCGGTCGGCGCTTGCATTGAGCTTCGCGCCCATGATTATTAGACCAGGTACGAACGGCCGTATCTTGGACGTTTTCCGAGATGCACAGGGGGGCGCCACGCCTAGCGCGCAGCGTTCGGAGCTTTCGTCCATCTCTATGCTGGCTGACTGACTCAGAGCGAATATAGCTTGCGTCTAACGAGATATAACCTGCTGTCCAGGAGGTACGGTGCCTATGCAGGACGGTTTAGTGGCACGGGAGGCGTCACCGCGACGATGAAGAAAGACATTCCTACTCTACTGCAGTGAAGTCGTTCAGGTGATCCACTGATCTTTTACCACCCCGTCGGAAATGGCCACGACACACCAAATCAGTCTGTGCCGTTGGCTACTCGTGACTTTATGCTGCGTGGACAGATTCTTAATACATGATAATCATCACCGGGTGAGCACCGGAAAAGCCGGTCTGACTGCGCAGGTTACAGGAGGATCTCAACCCTATCTAGATGGAGGTCGAGGGTTCGAGAACCTGCTTACGCGCTAGTTATATGTTAGTTTCAGCCGTATAGAAAGACCTTGGGGAAATGAATAGATGAGGAATGGTCCCAAATCTGGGCCAAGATAGGCATCTAACATCACATGACCTAATGCTTGTAATAGTCAACCGGTTTTATTCGGGATCAGGATCCTGTGAGTTAGCGTTCAGGGGCTAGAGGTTGTAAGGCGACGCGTGAAAACTACACCCTGAGGAGTCCGAAGTGCACTCTGTGCAACGCACCCGTGAGTTCTATGTCCATACATAGTCAATATAGGGCTCATGGAACTAGCATCAATATAGTCACTAAACGCGTCGAAAAAACGTCCCATGTGTAAGCATCGAACCGCCCTGCAAGGACCTCGTCCACAAGGACGGTGAAGGGAACATTCAGGTGGAGTCCAAAAACGCTAGGTGAAAATCTCCTCATAAAGCGGCTATCCAGCGCACTCATCCACTGCTACCGCTGTTTATACTCTCCGTCCGTCCTGAGAGGTTACGTTCTAGCTATGATTCGAATCACCCCATTCGAATGGTACCCGTTCAGCCTTCAAATTTATGGACGAATCATTTCCCCTCATTGTGTGACGGACACGATCATTCGGTGTAATATAATATCCCCGCCACGCTTAGGATGTAAATTTAGTCCCGGAAATCTCATATGCGTGTCACGTGTCGATTTCGACCCGGCACTGCGCGTCTTAGGATAGGATAGTGATGATTTGTGAATCTGAACTGCAGCTATAGGCACCTCGTCCCGATATATACCACTCAAGGTTGACCAGCTTATGCCCCGAGCATCCCGTGAGTGGCATCCTTAAAGTTAACGACCGCAGGCGCTCCGATTCGAGTACCACCTTAGAGTAAGATCTTCGCAATATCCGTTGCCTAAGCGGCTGGGTGCTGTGGGGTTCCCGTCATGCAACGTCCTAGGCAGGCTTGATTAACTGCAAACCCCTCACGAGCCTGTATCAGTATAGAACATCTCTTTTCGAACATAACATCTAATCAGGTGGCGATCGAGATTTACCTCTTGCATAAGATGGTCCGAGGTCGTGTATGGGCCACGAACCAAGGAACATGATTAGACTAAGCGCTGTCTTTATGGACCCACGAGGCCTGTCGTACCGTCTGATACGCGTTCCTCTCACAGGAAGGCGATCCCACACTGGACATCTAGTGCGTAGCGATTAACTGATCAGCTGGGGGACTGGGACTGCCTTACGAAGCAGGTCGCTCATTTAAGGTGGTACGGGTCAGCTTAGCGCCACTGGCTACCTATCAAGGGCGCATAGCACGATGGGCCAATGAGTCTCGTTCGCCGCAAGCGAACGATTACTTTCTTGTGGGACTAACGCTACAAACTTGGGCGCCATACTTGCCATCGAGTCAAAGCGGGAGGGTCGGTGGCCCTCATGGTACTGTCATTGTCATAACTAATAAGAACCCTAGCTAAGGGACAGTCCTCAATTAAACCAGCTCTTCTACGCAACAATAGAACAAGACTTCTTCCCGCGGACATATTTTCTGTGCAGCTAAACTACGCTACTGAGCGGTAGTCGCTTTCTAGATTCGCCTAGGGGTTCTATAGCTCTATACCTGTGATCGAAAACTGCTTCCGTGTTCGATCCGCGAAGTCTTGGCGATTCTGATACGCATGGTTTGCACGATATGGTCGTATATGCCAGGACCCTGAACATTTATATCCCAGGGCCACAAGCGTTTTGTCTCCTGCCA","AGGTTGAAGGG",4))
	