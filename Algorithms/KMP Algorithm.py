# O(n + m) time | O(m) space
def KMPAlgorithm(string, substring):
	pattern = buildPattern(substring)
	return doesMatch(string, substring, pattern)

def buildPattern(substring):
	j = 0
	i = 1
	pattern = [-1] * len(substring)
	while i < len(substring):
		if substring[i] == substring[j]:
			pattern[i] = j
			i += 1
			j += 1
		elif j > 0:
			j = pattern[j - 1] + 1
		else:
			i += 1
	return pattern

def doesMatch(string, substring, pattern):
	i = 0
	j = 0
	while i + len(substring) - j <= len(string):
		if string[i] == substring[j]:
			if j == len(substring) - 1:
				return True
			i += 1
			j += 1
		elif j > 0:
			j = pattern[j - 1] + 1
		else:
			i += 1
	return False


print(KMPAlgorithm("akramakaeeanany", "aka"))
