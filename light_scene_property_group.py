import bpy

from bpy.types import PropertyGroup
from bpy.props import StringProperty, EnumProperty
from bpy.utils import register_class, unregister_class

from . import tools

class LightScenePropertyGroup(PropertyGroup):
    collection_name : StringProperty(
        name = "",
        description = "A collection containing the lights to render",
        search = tools.Tools.searchCollectionNames
    )
    
    light_mode : EnumProperty(
        items = (
        ("ALL_LIGHTS_MODE", "Render with all lights", "The mode in which each generated scene will be rendered with all lights"), 
        ("RANDOM_LIGHTS_MODE", "Render with random light", "The mode in which for each generated scene only one random light will be selected for rendering")
        ),
        name = ""
    )

classes = [
    LightScenePropertyGroup
]

def register():
    for cl in classes:
        register_class(cl)

def unregister():
    for cl in reversed(classes):
        unregister_class(cl)

if __name__ == "__main__":
    register()