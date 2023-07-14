import bpy

from bpy.types import PropertyGroup
from bpy.props import IntProperty, BoolProperty
from bpy.utils import register_class, unregister_class
	
class GeneratorScenePropertyGroup(PropertyGroup):
    scene_count : IntProperty(
        name = "",
        default = 0,
        min = 0,
        description = "Number of generated scenes to render"
    )
    
    start_index : IntProperty(
        name = "",
        default = 0,
        min = 0,
        description = "The index from which the numbering of titles starts"
    )
    
    collision : BoolProperty(
        name = "Collision",
        default = True,
        description = "Parameter responsible for tracking collision"
    )

classes = [
    GeneratorScenePropertyGroup
]

def register():
    for cl in classes:
        register_class(cl)

def unregister():
    for cl in reversed(classes):
        unregister_class(cl)

if __name__ == "__main__":
    register()