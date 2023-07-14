import bpy

from bpy.types import Panel
from bpy.props import PointerProperty
from bpy.utils import register_class, unregister_class

from . import model_scene_property_group as ms_pg
from . import model_object_property_group as mo_pg

from . import tools

class OBJECT_PT_ModelPanel(Panel):
    bl_label = "Model"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Dataset Generator"
    
    def draw(self, context):
        layout = self.layout
        props_scene = context.scene.dataset_generator_model
        
        col = layout.column()
        box = col.box()
        
        box.label(text = "Models collection:")
        box.prop(props_scene, "collection_name", icon = "OUTLINER_COLLECTION")
        
        if tools.Tools.isCollection(self, context, context.scene.dataset_generator_model.collection_name) and tools.Tools.isNotEmptyModelCollection(self, context):
            col = layout.column()
            box = col.box()
        
            box.label(text = "Model:")
            box.prop(props_scene, "model_name", icon = "OUTLINER_OB_MESH")
            
            if tools.Tools.isModelFromModelCollection(self, context, context.scene.dataset_generator_model.model_name):
                props_object = context.scene.collection.children.get(context.scene.dataset_generator_model.collection_name).objects.get(context.scene.dataset_generator_model.model_name).dataset_generator_model
                
                box.label(text = "Model class:")
                box.prop(props_object, "class_name")
                
                box.label(text = "Number of model instances:") 
                box.prop(props_object, "model_count")
                
                box.label(text = "Material key:")
                box.prop(props_object, "material_key", icon = "MATERIAL")
                
                box.label(text = "Material mode:")
                box.prop(props_object, "material_mode")
            
            is_scene_material_mode = True
            material_key = None
            
            for model in context.scene.collection.children[context.scene.dataset_generator_model.collection_name].objects.values():
                if tools.Tools.isModelFromModelCollection(self, context, model.name):
                    if material_key == None:
                        material_key = model.dataset_generator_model.material_key
                    else:
                        if material_key != model.dataset_generator_model.material_key:
                            is_scene_material_mode = False
                            break
            
            if is_scene_material_mode == True:
                box = col.box()
                box.prop(props_scene, "material_mode")

classes = [
    OBJECT_PT_ModelPanel
]

def register():
    ms_pg.register()
    mo_pg.register()
    
    for cl in classes:
        register_class(cl)
    
    bpy.types.Scene.dataset_generator_model = PointerProperty(type = ms_pg.ModelScenePropertyGroup)
    bpy.types.Object.dataset_generator_model = PointerProperty(type = mo_pg.ModelObjectPropertyGroup)

def unregister():
    for cl in reversed(classes):
        unregister_class(cl)
    
    mo_pg.unregister()
    ms_pg.unregister()

if __name__ == "__main__":
    register()