import bpy

from bpy.types import Panel
from bpy.props import PointerProperty
from bpy.utils import register_class, unregister_class

from . import generator_scene_property_group as gs_pg
from . import generator_operator as g_o

from . import tools

class OBJECT_PT_GeneratorPanel(Panel):
    bl_label = "Generator"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Dataset Generator"
    
    def draw(self, context):
        layout = self.layout
        props_scene = context.scene.dataset_generator_generator
        
        col = layout.column()
        box = col.box()
        
        box.label(text = "Scene count:")
        box.prop(props_scene, "scene_count")
        
        box = col.box()
        
        box.label(text = "Start index:")
        box.prop(props_scene, "start_index")
        
        box = col.box()
        
        box.prop(props_scene, "collision")
        
        if self.isValidSession(context) == True:
            col = layout.column()
            box = col.box()
            
            box.operator("generator.dataset_generator")
    
    def isValidSession(self, context):
        if (
        tools.Tools.isCollection(self, context, context.scene.dataset_generator_model.collection_name) == False or
        tools.Tools.isNotEmptyModelCollection(self, context) == False
        ):
            return Flase
        
        if (
        tools.Tools.isCollection(self, context, context.scene.dataset_generator_camera.collection_name) == False or
        tools.Tools.isNotEmptyCameraCollection(self, context) == False
        ):
            return Flase
        
        if (
        tools.Tools.isCollection(self, context, context.scene.dataset_generator_light.collection_name) == False or
        tools.Tools.isNotEmptyLightCollection(self, context) == False
        ):
            return Flase
        
        if (
        tools.Tools.isCollection(self, context, context.scene.dataset_generator_background.collection_name) == False or
        tools.Tools.isNotEmptyBackgroundCollection(self, context) == False
        ):
            return Flase
        
        for object in context.scene.collection.children[context.scene.dataset_generator_background.collection_name].objects.values():
            if object.type == "MESH":
                if tools.Tools.isVertexGroupFromBackground(self, context, object.dataset_generator_background.vertex_group, object.name) == False:
                    return False
        
        if context.scene.dataset_generator_model.material_mode == True:
            material_key = None
            
            for model in context.scene.collection.children[context.scene.dataset_generator_model.collection_name].objects.values():
                if tools.Tools.isModelFromModelCollection(self, context, model.name):
                    if material_key == None:
                        material_key = model.dataset_generator_model.material_key
                    else:
                        if material_key != model.dataset_generator_model.material_key:
                            return False
        
        return True

classes = [
    OBJECT_PT_GeneratorPanel
]

def register():
    gs_pg.register()
    g_o.register()
    
    for cl in classes:
        register_class(cl)
    
    bpy.types.Scene.dataset_generator_generator = PointerProperty(type = gs_pg.GeneratorScenePropertyGroup)

def unregister():
    for cl in reversed(classes):
        unregister_class(cl)
    
    g_o.unregister()
    gs_pg.unregister()

if __name__ == "__main__":
    register()