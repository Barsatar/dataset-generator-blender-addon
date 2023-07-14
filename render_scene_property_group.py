import bpy

from bpy.types import PropertyGroup
from bpy.props import StringProperty, IntProperty, BoolProperty, EnumProperty
from bpy.utils import register_class, unregister_class

class RenderScenePropertyGroup(PropertyGroup):
    render_engine : EnumProperty(
        items = (
        ("CYCLES_MODE", "Cycles", "Rendering will be done on the Cycles engine"), 
        ("EEVEE_MODE", "Eevee", "Rendering will be done on the Eevee engine")
        ),
        name = ""
    )
    
    device : EnumProperty(
        items = (
        ("GPU_MODE", "GPU", "Rendering will be done by the GPU"),
        ("CPU_MODE", "CPU", "Rendering will be done by the CPU")
        ),
        name = ""
    )
    
    samples : IntProperty(
        name = "",
        default = 50,
        min = 0,
        description = "Number of samples to render"
    )
    
    resolution_x : IntProperty(
        name = "",
        default = 800,
        min = 0,
        subtype = "PIXEL",
        description = "Number of horizontal pixels in the rendered image"
    )
    
    resolution_y : IntProperty(
        name = "",
        default = 600,
        min = 0,
        subtype = "PIXEL",
        description = "Number of vertical pixels in the rendered image"
    )
    
    transparent : BoolProperty(
        name = "Transparent",
        default = False,
        description = "Parameter responsible for background transparency"
    )
    
    mask_render : BoolProperty(
        name = "Mask render",
        default = True,
        description = "Parameter responsible for rendering model masks"
    )
    
    save_dir_path : StringProperty(
        name = "",
        default = "",
        subtype = "DIR_PATH",
        description = "The path where the images will be saved"
    )

classes = [
    RenderScenePropertyGroup
]

def register():
    for cl in classes:
        register_class(cl)

def unregister():
    for cl in reversed(classes):
        unregister_class(cl)

if __name__ == "__main__":
    register()