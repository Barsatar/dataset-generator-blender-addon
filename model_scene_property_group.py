import bpy

from bpy.types import PropertyGroup
from bpy.props import StringProperty, BoolProperty
from bpy.utils import register_class, unregister_class

from . import tools

class ModelScenePropertyGroup(PropertyGroup):
    collection_name : StringProperty(
        name = "",
        description = "A collection containing the models to generate the dataset",
        search = tools.Tools.searchCollectionNames
    )
    
    model_name : StringProperty(
        name = "",
        description = "Mesh model from the collection of models",
        search = tools.Tools.searchModelNames
    )
    
    material_mode : BoolProperty(
        name = "Scene material mode",
        default = False,
        description = "All copies of models in the scene will have one material (individual material mode settings are not taken into account)"
    )

classes = [
    ModelScenePropertyGroup
]

def register():
    for cl in classes:
        register_class(cl)

def unregister():
    for cl in reversed(classes):
        unregister_class(cl)

if __name__ == "__main__":
    register()