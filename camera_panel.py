import bpy

from bpy.types import Panel
from bpy.props import PointerProperty
from bpy.utils import register_class, unregister_class

from . import camera_scene_property_group as cs_pg

from . import tools

class OBJECT_PT_CameraPanel(Panel):
    bl_label = "Camera"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Dataset Generator"
    
    def draw(self, context):
        layout = self.layout
        props_scene = context.scene.dataset_generator_camera
        
        col = layout.column()
        box = col.box()
        
        box.label(text = "Cameras collection:")
        box.prop(props_scene, "collection_name", icon = "OUTLINER_COLLECTION")
        
        if tools.Tools.isCollection(self, context, context.scene.dataset_generator_camera.collection_name) and tools.Tools.isNotEmptyCameraCollection(self, context):
            box.label(text = "Camera mode:")
            box.prop(props_scene, "camera_mode")

classes = [
    OBJECT_PT_CameraPanel
]

def register():
    cs_pg.register()
    
    for cl in classes:
        register_class(cl)
    
    bpy.types.Scene.dataset_generator_camera = PointerProperty(type = cs_pg.CameraScenePropertyGroup)

def unregister():
    for cl in reversed(classes):
        unregister_class(cl)
    
    cs_pg.unregister()

if __name__ == "__main__":
    register()