# Makes all strings default settings as Constant for nice viewing in the Decompiler

#@category Tate.AutoScripts

from ghidra.program.model.data import MutabilitySettingsDefinition

data = getDataAt(currentAddress)
datat = data.getDataType()
sd = datat.getSettingsDefinitions()
for i in sd:
	if type(i) == ghidra.program.model.data.MutabilitySettingsDefinition:
		i.setChoice(datat.getDefaultSettings(), MutabilitySettingsDefinition.CONSTANT)
