import bpy

from bpy.types import Panel
from bpy.props import PointerProperty
from bpy.utils import register_class, unregister_class

from . import background_scene_property_group as bs_pg
from . import background_object_property_group as bo_pg

from . import tools

class OBJECT_PT_BackgroundPanel(Panel):
    bl_label = "Background"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Dataset Generator"
    
    def draw(self, context):
        layout = self.layout
        props_scene = context.scene.dataset_generator_background
        
        col = layout.column()
        box = col.box()
        
        box.label(text = "Backgrounds collection:")
        box.prop(props_scene, "collection_name", icon = "OUTLINER_COLLECTION")
        
        if tools.Tools.isCollection(self, context, context.scene.dataset_generator_background.collection_name) and tools.Tools.isNotEmptyBackgroundCollection(self, context):
            box = col.box()
            
            box.label(text = "Background:")
            box.prop(props_scene, "background_name", icon = "OUTLINER_OB_MESH")
            
            if tools.Tools.isBackgroundFromBackgroundCollection(self, context, context.scene.dataset_generator_background.background_name):
                props_object = context.scene.collection.children.get(context.scene.dataset_generator_background.collection_name).objects.get(context.scene.dataset_generator_background.background_name).dataset_generator_background
                
                box.label(text = "Vertex group:")
                box.prop(props_object, "vertex_group", icon = "GROUP_VERTEX")
                
                box = col.box()
                
                box.label(text = "Material key:")
                box.prop(props_object, "material_key", icon = "MATERIAL")

classes = [
    OBJECT_PT_BackgroundPanel
]

def register():
    bs_pg.register()
    bo_pg.register()
    
    for cl in classes:
        register_class(cl)
    
    bpy.types.Scene.dataset_generator_background = PointerProperty(type = bs_pg.BackgroundScenePropertyGroup)
    bpy.types.Object.dataset_generator_background = PointerProperty(type = bo_pg.BackgroundObjectPropertyGroup)

def unregister():
    for cl in reversed(classes):
        unregister_class(cl)
    
    bo_pg.unregister()
    bs_pg.unregister()

if __name__ == "__main__":
    register()