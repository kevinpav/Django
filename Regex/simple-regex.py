# -*- coding: utf-8 -*-
# Simple Searching

#Here's some code to help you get started:
import re
def get_matching_words(regex):
	words = ["aimlessness", "assassin", "baby", "beekeeper", "belladonna", "cannonball", "crybaby", "denver", "embraceable", "facetious", "flashbulb", "gaslight", "hobgoblin", "iconoclast", "issue", "kebab", "kilo", "laundered", "mattress", "millennia", "natural", "obsessive", "paranoia", "queen", "rabble", "reabsorb", "sacrilegious", "schoolroom", "tabby", "tabloid", "unbearable", "union", "videotape"]
  	matches = []
	for word in words:
		if re.search(regex,word):
			matches.append(word)
	return matches

# Starting with the code snippet below, write regular expressions to match:
# * All words that contain a “v”
# print get_matching_words('v')
# print get_matching_words('[v]')

# * All words that contain a double-“s”
# print get_matching_words('ss')

# * All words that end with an “e”
# print get_matching_words('e$')

# * All words that contain an “b”, any character, then another “b”
# print get_matching_words('b.b')

# * All words that contain an “b”, at least one character, then another “b”
# print get_matching_words('b.+b')

# * All words that contain an “b”, any number of characters (including zero), then another “b”
# print get_matching_words('b.+b')

# * All words that include all five vowels in order
# print get_matching_words('[A,a].*[E,e].*[I,i].*[O,o].*[U,u]')

# * All words that only use the letters in “regular expression” (each letter can appear any number of times)
# print get_matching_words('[regular expression]')

# * All words that contain a double letter
print get_matching_words('(.)\\1')	# Had to escape the backslash, why there are two \\
print get_matching_words('(\\w)\\1')	# Had to escape the backslash, why there are two \\
