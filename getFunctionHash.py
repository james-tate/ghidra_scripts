# Gets the hash of the current function. Useful for function matching.

# DISCLAIMER: This is meant to be an example. You likely want to use this process in your own script

#@category Tate.AutoScripts

from ghidra.feature.fid.service import FidService;

fs = FidService()

func = getFunctionAt(currentAddress)

hashs = fs.hashFunction(func)

print ("\nFull Hash: {}, \nCode Units used to get fullhash: {}, \nAdditional Code Units: {}, \nSpecificHash: {}\n").format(
	hex(hashs.getFullHash()), 
	hex(hashs.getCodeUnitSize()), 
	hex(hashs.getSpecificHashAdditionalSize()), 
	hex(hashs.getSpecificHash()))
