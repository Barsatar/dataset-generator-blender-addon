import bpy

from bpy.types import PropertyGroup
from bpy.props import StringProperty, EnumProperty
from bpy.utils import register_class, unregister_class

from . import tools

class CameraScenePropertyGroup(PropertyGroup):
    collection_name : StringProperty(
        name = "",
        description = "A collection containing the cameras to render",
        search = tools.Tools.searchCollectionNames
    )

    camera_mode : EnumProperty(
        items = (
        ("ALL_CAMERAS_MODE", "Render with all cameras", "The mode in which each generated scene will be rendered from all cameras"),
        ("RANDOM_CAMERAS_MODE", "Render with random camera", "The mode in which for each generated scene only one random camera will be selected to render")
        ),
        name = ""
    )

classes = [
    CameraScenePropertyGroup
]

def register():
    for cl in classes:
        register_class(cl)

def unregister():
    for cl in reversed(classes):
        unregister_class(cl)

if __name__ == "__main__":
    register()