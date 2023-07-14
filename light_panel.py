import bpy

from bpy.types import Panel
from bpy.props import PointerProperty
from bpy.utils import register_class, unregister_class

from . import light_scene_property_group as ls_pg

from . import tools
  
class OBJECT_PT_LightPanel(Panel):
    bl_label = "Light"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Dataset Generator"
    
    def draw(self, context):
        layout = self.layout
        props_scene = context.scene.dataset_generator_light
        
        col = layout.column()
        box = col.box()
        
        box.label(text = "Lights collection:")
        box.prop(props_scene, "collection_name", icon = "OUTLINER_COLLECTION")
        
        if tools.Tools.isCollection(self, context, context.scene.dataset_generator_light.collection_name) and tools.Tools.isNotEmptyLightCollection(self, context):
            box.label(text = "Light mode:")
            box.prop(props_scene, "light_mode")

classes = [
    OBJECT_PT_LightPanel
]

def register():
    ls_pg.register()
    
    for cl in classes:
        register_class(cl)
    
    bpy.types.Scene.dataset_generator_light = PointerProperty(type = ls_pg.LightScenePropertyGroup)

def unregister():
    for cl in reversed(classes):
        unregister_class(cl)
    
    ls_pg.unregister()

if __name__ == "__main__":
    register()