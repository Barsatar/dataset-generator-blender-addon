import bpy

from bpy.types import PropertyGroup
from bpy.props import StringProperty, EnumProperty
from bpy.utils import register_class, unregister_class

from . import tools

class BackgroundScenePropertyGroup(PropertyGroup):
    collection_name : StringProperty(
        name = "",
        description = "A collection containing the backgrounds to render",
        search = tools.Tools.searchCollectionNames
    )
    
    background_name : StringProperty(
        name = "",
        description = "Mesh background from the collection of backgrounds",
        search = tools.Tools.searchBackgroundNames
    )

classes = [
    BackgroundScenePropertyGroup
]

def register():
    for cl in classes:
        register_class(cl)

def unregister():
    for cl in reversed(classes):
        unregister_class(cl)

if __name__ == "__main__":
    register()