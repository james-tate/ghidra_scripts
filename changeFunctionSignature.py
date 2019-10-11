# Changes the signature of the current function

# DISCLAIMER: This is meant to be an example of how to change a signature from a script. You likely want to use this process in your own script

#@category Tate.AutoScripts

from ghidra.program.util import FunctionUtility
from ghidra.app.cmd.function import SetFunctionNameCmd
from ghidra.program.model.symbol import SourceType
from ghidra.program.model.data import FunctionDefinitionDataType
from ghidra.program.model.data import Pointer32DataType
from ghidra.program.model.data import DWordDataType
from ghidra.program.model.data import ParameterDefinitionImpl
from ghidra.program.model.symbol import SourceType
from ghidra.app.cmd.function import ApplyFunctionSignatureCmd

debug = True

# ghidra data types for more see see http://hwreblog.com/9.1-BETA/api/ghidra/program/model/data/DataType.html
pointer32 = Pointer32DataType()
dword = DWordDataType()

#parameter definitions
#WARNING, a NEW definition will need to be created for each of the same instance in a signature
#to give the parameter a default name change the first argument
pointer32Def = ParameterDefinitionImpl("p32", pointer32, "32 bit pointer")
dwordDef = ParameterDefinitionImpl(None, dword, "double word")

# list of functions to change signatures
functionsToChange = [					
	"foo",
	"bar"
        #...
	]

#function definitions
fooDef = FunctionDefinitionDataType("foo")
fooDef.setArguments([pointer32Def, dwordDef])
barDef = FunctionDefinitionDataType("bar")
barDef.setArguments([pointer32Def])
functionDefs = [
	fooDef,
	barDef
	]

func = getFirstFunction()

#loop though functions looking names that match our list
while func is not None:
    func_name = func.getName()
    if func_name in functionsToChange:
    	for defi in functionDefs:
    		if func_name == defi.getName():
    			cmd = ApplyFunctionSignatureCmd(func.getEntryPoint(), defi, SourceType.USER_DEFINED)
    			runCommand(cmd)
    			if debug == True:
    				print "Address {} -> Name {}".format(func.getEntryPoint(), defi.getName())
    				print cmd.getStatusMsg()
    func = getFunctionAfter(func)