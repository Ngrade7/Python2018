#sets_4.py nrg
alpha = {"a","b","c","d","e","f"}
bravo = {"z","y","x","w","v"}
charlie = alpha.union(bravo)
charlie.update("g","h","i","j","k")
for x in charlie:
	print()
#pop all the records.
for i in range(len(charlie)):
	print("pop ",i," ",end="")
	thepop = charlie.pop()
	print (thepop)	
