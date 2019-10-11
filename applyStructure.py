# Applies a structure to the current GLOBAL addres

# DISCLAIMER: This is meant to be an example. You likely want to use this process in your own script

#@category Tate.AutoScripts

from ghidra.program.model.data import StructureDataType
from ghidra.program.model.data import DWordDataType
from ghidra.program.database.data import DataTypeManagerDB
from ghidra.program.model.data import DataTypeConflictHandler

debug = True
applyGlobal = True

#make a structure with size 4
struct = StructureDataType("scriptStruct", 0x4)

if debug == True:
	print "struct before" 
	print struct
# inserts and expands the data type at arg1 offset
# expands structure to size 8
struct.insertAtOffset(0x0, DWordDataType(), 4, "offset 0", None)
struct.replaceAtOffset(4, DWordDataType(), 0, "offset 4", None)

if debug == True:
	print "struct after" 
	print struct

#assign the structure to the address
# when assigning to global, the struct will be auto inserted into the manager
if applyGlobal == True:
	createData(currentAddress, struct)
else:
# if not applying to global, insert into Data Type Manager
# the name will show up in the Data Type Manager window and can be applied post 
	dtm = currentProgram.getDataTypeManager()
	dtm.addDataType(struct, DataTypeConflictHandler.DEFAULT_HANDLER)