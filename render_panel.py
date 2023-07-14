import bpy

from bpy.types import Panel
from bpy.props import PointerProperty
from bpy.utils import register_class, unregister_class

from . import render_scene_property_group as rs_pg

from . import tools

class OBJECT_PT_RenderPanel(Panel):
    bl_label = "Render"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Dataset Generator"
    
    def draw(self, context):
        layout = self.layout
        props_scene = context.scene.dataset_generator_render
        
        col = layout.column()
        box = col.box()
        
        box.label(text = "Render engine:")
        box.prop(props_scene, "render_engine")
        
        if context.scene.dataset_generator_render.render_engine == "CYCLES_MODE":
            box.label(text = "Device:")
            box.prop(props_scene, "device")
            box.label(text = "Samples:")
            box.prop(props_scene, "samples")
        
        col = layout.column()
        box = col.box()
        
        box.label(text = "Resolution:")
        spl = box.split()
        spl.prop(props_scene, "resolution_x")
        spl.prop(props_scene, "resolution_y")
        
        col = layout.column()
        box = col.box()
        
        box.prop(props_scene, "transparent")
        
        col = layout.column()
        box = col.box()
        
        box.prop(props_scene, "mask_render")
        
        col = layout.column()
        box = col.box()
        
        box.label(text = "Save path:")
        box.prop(props_scene, "save_dir_path")

classes = [
    OBJECT_PT_RenderPanel
]

def register():
    rs_pg.register()
    
    for cl in classes:
        register_class(cl)
    
    bpy.types.Scene.dataset_generator_render = PointerProperty(type = rs_pg.RenderScenePropertyGroup)

def unregister():
    for cl in reversed(classes):
        unregister_class(cl)
    
    rs_pg.unregister()

if __name__ == "__main__":
    register()