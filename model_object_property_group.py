import bpy

from bpy.types import PropertyGroup
from bpy.props import StringProperty, IntProperty, EnumProperty
from bpy.utils import register_class, unregister_class

class ModelObjectPropertyGroup(PropertyGroup):
    class_name : StringProperty(
        name = "",
        default = "",
        description = "The class that will be assigned to the model when the dataset is generated"
    )
    
    model_count : IntProperty(
        name = "",
        default = 1,
        min = 0,
        description = "The number of model copies to use when generating the dataset"
    )
    
    material_key: StringProperty(
        name = "",
        default = "",
        description = "The key of the name of the materials that will be used for this model"
    )
    
    material_mode : EnumProperty(
        items = (
        ("SAME_MATERIAL_MODE", "Same material", "All copies of the model will have the same material applied"),
        ("RANDOM_MATERIAL_MODE", "Random material", "A random material will be applied to each copy of the model")
        ),
        name = ""
    )

classes = [
    ModelObjectPropertyGroup
]

def register():
    for cl in classes:
        register_class(cl)

def unregister():
    for cl in classes:
        unregister_class(cl)

if __name__ == "__main__":
    register()