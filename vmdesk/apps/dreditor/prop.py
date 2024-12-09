import bpy
from bpy.types import (
    DriverVariable,
    DriverTarget,
    Driver)

from .  import VMD

# <<< 1mp (VMD.util.types
types = VMD.util.types
RnaDataOps = types.RnaDataOps
RnaFloat = types.RnaFloat
RnaFloatVector = types.RnaFloatVector
RnaBool = types.RnaBool
RnaString = types.RnaString
RnaEnum = types.RnaEnum
RnaButton = types.RnaButton
RnaPointer = types.RnaPointer
Dictlist = types.Dictlist
# >>>



#<RNAS>#
RNAS_driver = {
"idtype": RnaEnum("idtype",
    enum_items = DriverTarget.bl_rna.properties["id_type"].enum_items,
    name = "ID Type",
    description = "",
    default = "OBJECT"),
"id": RnaPointer("id",
    name = "ID",
    description = ""),
"driver": RnaEnum("driver",
    enum_items = (),
    name = "Driver Path",
    description = ""),
"driver_value": RnaString("driver_value",
    name = "Driver Value",
    description = "",
    default = "0.0"),
"enable": RnaBool("enable",
    name = "Enable",
    description = "Let the driver determine this property's value"),
"update_dependencies": RnaButton("update_dependencies",
    name = "Update Dependencies",
    description = "Force update of dependencies - Only use this if drivers are not updating correctly",
    button_text = "Update Dependencies"),
}
#<RNAS>#

RNAS_driver["idtype"].icon = "idtype"
RNAS_driver["driver"].icon = "driver_path"

Driver_bl_rna_properties = Driver.bl_rna.properties
for k in ("type", "expression", "use_self"):
    RNAS_driver[k] = Driver_bl_rna_properties[k]

#<RNAS>#
RNAS_driver_variable = {
"variable_value": RnaString("variable_value",
    name = "Driver Value",
    description = "",
    default = ""),
}
#<RNAS>#

RNAS_driver_variable["type"] = RnaEnum.copy_from_bl_rna(DriverVariable.bl_rna.properties["type"])


def late_import():
    RNAS_driver_variable["type"].icon = VMD.utilbl.blg.D_geticon_DriverVar
    #|
