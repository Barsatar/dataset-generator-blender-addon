import bpy

from bpy.types import PropertyGroup
from bpy.props import StringProperty
from bpy.utils import register_class, unregister_class

from . import tools

class BackgroundObjectPropertyGroup(PropertyGroup):
    vertex_group: StringProperty(
        name = "",
        description = "The group of points within which the scene will be generated",
        search = tools.Tools.searchVertexGroupNames
    )
    
    material_key: StringProperty(
        name = "",
        default = "",
        description = "The key of the name of the materials that will be used for this background"
    )

classes = [
    BackgroundObjectPropertyGroup
]

def register():
    for cl in classes:
        register_class(cl)

def unregister():
    for cl in reversed(classes):
        unregister_class(cl)

if __name__ == "__main__":
    register()