#!/usr/bin/python3
def best_score(a_dictionary):
    best_scor=0
    for key in a_dictionary:
	if a_dictionary[key] > best_scor:
	    best_scor=a_dictionary[key]
    return best_scor
