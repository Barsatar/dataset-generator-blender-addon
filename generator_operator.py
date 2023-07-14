import bpy
import os
import math

from bpy.types import Operator
from bpy.utils import register_class, unregister_class

from random import randint
from mathutils import Vector

class GeneratorOperator(Operator):
    bl_idname = "generator.dataset_generator"
    bl_label = "Start"
    bl_description = "Starting the generation of data sets"
    
    def execute(self, context): 
        self.createDatasetGeneratorCollection(context)
        parent_child_dict = self.createModelCopies(context)
        self.createCameraCopies(context)
        self.createLightCopies(context)
        self.createBackgroundCopies(context)
        
        self.modelSetting(context)
        self.cameraSetting(context)
        self.lightSetting(context)
        self.backgroundSetting(context)
        self.renderSetting(context)
        self.sceneSetting(context)
        
        index = self.getStartIndex(context)
        
        for i in range(0, self.getSceneCount(context)):
            self.prepareModel(context, parent_child_dict)
            cameras = self.prepareCamera(context)
            self.prepareLight(context)
            background = self.prepareBackground(context)
            
            self.sceneGenerate(context, background)
            
            for camera in cameras:
                context.scene.camera = camera
                
                self.sceneRender(context, self.getSaveDirPath(context) + "\\dataset_generator" + "\\image_" + str(index) + "\\", "DGImage__" + str(index) + "__.png")
                
                if self.getMaskRenderMode(context) == True:
                    self.maskRender(context, self.getSaveDirPath(context) + "\\dataset_generator" + "\\image_" + str(index) + "\\", "DGMask__" + str(index))
                
                index += 1
        
        self.removeBackgroundCopies(context)
        self.removeLightCopies(context)
        self.removeCameraCopies(context)
        self.removeModelCopies(context)
        self.removeDatasetGeneratorCollection(context)
        
        return {"FINISHED"}
    
    def sceneGenerate(self, context, background):
        set_models = []
        
        vertices = [vert for vert in background.data.vertices if background.vertex_groups[background.dataset_generator_background.vertex_group].index in [i.group for i in vert.groups]]
        
        for model in context.scene.collection.children.get("Dataset Generator Scene Collection").children.get("Dataset Generator Scene Model Collection").objects.values():
            if len(vertices) != 0:
                index_for_model = list(range(0, len(vertices)))
                
                while True:
                    if len(index_for_model) != 0:
                        isSetModel = True
                        index = randint(0, len(index_for_model) - 1)
                        vertex_coordinate = background.matrix_world @ Vector((vertices[index_for_model[index]].co))
                        self.setModelLocation(context, model, vertex_coordinate[0], vertex_coordinate[1], vertex_coordinate[2])
                        
                        if self.getCollisionMode(context) == True:
                            for set_model in set_models:
                                if self.checkModelCollision(context, set_model, model) == True:
                                    index_for_model.pop(index)
                                    self.setModelLocation(context, model, 0, 0, 0)
                                    isSetModel = False
                                    
                                    break
                        
                        if isSetModel == True:
                            vertices.pop(index_for_model[index])
                            set_models.append(model)
                            
                            break
                    else:
                        self.hideRenderModel(context, model.name)
                        
                        break
            else:
                self.hideRenderModel(context, model.name)
    
    def sceneRender(self, context, output_dir_name, output_file_name):
        context.scene.render.filepath = os.path.join(output_dir_name, output_file_name)
        bpy.ops.render.render(write_still = True)
    
    def maskRender(self, context, output_dir_name, output_file_name):
        if self.getRenderEngine(context) == "CYCLES_MODE":
            context.scene.cycles.samples = 0

        if self.getTransparentMode(context) == False:
            context.scene.render.film_transparent = True
            context.scene.render.image_settings.color_mode = "RGBA"
     
        for model in context.scene.collection.children.get('Dataset Generator Scene Collection').children.get('Dataset Generator Scene Model Collection').objects.values():
            model.is_holdout = True
        
        for background in context.scene.collection.children.get('Dataset Generator Scene Collection').children.get('Dataset Generator Scene Background Collection').objects.values():
            background.is_holdout = True
        
        for model in context.scene.collection.children.get('Dataset Generator Scene Collection').children.get('Dataset Generator Scene Model Collection').objects.values():
            if model.dataset_generator_model.class_name != "":
                model.is_holdout = False
                self.sceneRender(context, output_dir_name, output_file_name + "__DGObject__" + model.name + "__DGClass__" + model.dataset_generator_model.class_name + "__.png")
                model.is_holdout = True
        
        for model in context.scene.collection.children.get('Dataset Generator Scene Collection').children.get('Dataset Generator Scene Model Collection').objects.values():
            model.is_holdout = False
        
        for background in context.scene.collection.children.get('Dataset Generator Scene Collection').children.get('Dataset Generator Scene Background Collection').objects.values():
            background.is_holdout = False
     
        if self.getTransparentMode(context) == False:
            context.scene.render.film_transparent = False
        
        if self.getRenderEngine(context) == "CYCLES_MODE":
            context.scene.cycles.samples = self.getSamplesCount(context)
    
    def createDatasetGeneratorCollection(self, context):
        collection = bpy.data.collections.new("Dataset Generator Scene Collection")
        context.scene.collection.children.link(collection)
        
        collection = bpy.data.collections.new("Dataset Generator Scene Model Collection")
        context.scene.collection.children["Dataset Generator Scene Collection"].children.link(collection)
        
        collection = bpy.data.collections.new("Dataset Generator Scene Camera Collection")
        context.scene.collection.children["Dataset Generator Scene Collection"].children.link(collection)
        
        collection = bpy.data.collections.new("Dataset Generator Scene Light Collection")
        context.scene.collection.children["Dataset Generator Scene Collection"].children.link(collection)
        
        collection = bpy.data.collections.new("Dataset Generator Scene Background Collection")
        context.scene.collection.children["Dataset Generator Scene Collection"].children.link(collection)
    
    def removeDatasetGeneratorCollection(self, context):
        collection = bpy.data.collections.get("Dataset Generator Scene Background Collection")
        context.scene.collection.children["Dataset Generator Scene Collection"].children.unlink(collection)
        bpy.data.collections.remove(collection)
        
        collection = bpy.data.collections.get("Dataset Generator Scene Light Collection")
        context.scene.collection.children["Dataset Generator Scene Collection"].children.unlink(collection)
        bpy.data.collections.remove(collection)
        
        collection = bpy.data.collections.get("Dataset Generator Scene Camera Collection")
        context.scene.collection.children["Dataset Generator Scene Collection"].children.unlink(collection)
        bpy.data.collections.remove(collection)
        
        collection = bpy.data.collections.get("Dataset Generator Scene Model Collection")
        context.scene.collection.children["Dataset Generator Scene Collection"].children.unlink(collection)
        bpy.data.collections.remove(collection)
        
        collection = bpy.data.collections.get("Dataset Generator Scene Collection")
        context.scene.collection.children.unlink(collection)
        bpy.data.collections.remove(collection)
    
    def createModelCopies(self, context):
        model_collection = context.scene.collection.children[context.scene.dataset_generator_model.collection_name]
        parent_child_dict = {}
        
        for object in model_collection.objects.values():
            if object.type == "MESH":
                child_name_list = []
                
                for _ in range(0, object.dataset_generator_model.model_count):
                    model_copy = object.copy()
                    data_copy = model_copy.data.copy()
                    model_copy.data = data_copy
                    context.scene.collection.children["Dataset Generator Scene Collection"].children["Dataset Generator Scene Model Collection"].objects.link(model_copy)
                    
                    child_name_list.append(model_copy.name)
                
                parent_child_dict[object.name] = child_name_list
        
        return parent_child_dict
    
    def removeModelCopies(self, context):
        for model in context.scene.collection.children['Dataset Generator Scene Collection'].children["Dataset Generator Scene Model Collection"].objects.values():
            name = model.name
            bpy.data.objects.remove(bpy.data.objects[name], do_unlink = True)
            bpy.data.meshes.remove(bpy.data.meshes[name], do_unlink = True)
    
    def createCameraCopies(self, context):
        camera_collection = context.scene.collection.children[context.scene.dataset_generator_camera.collection_name]
        
        for object in camera_collection.objects.values():
            if object.type == "CAMERA":
                camera_copy = object.copy()
                data_copy = camera_copy.data.copy()
                camera_copy.data = data_copy
                context.scene.collection.children["Dataset Generator Scene Collection"].children["Dataset Generator Scene Camera Collection"].objects.link(camera_copy)
    
    def removeCameraCopies(self, context):
        for camera in context.scene.collection.children['Dataset Generator Scene Collection'].children["Dataset Generator Scene Camera Collection"].objects.values():
            name = camera.name
            bpy.data.objects.remove(bpy.data.objects[name], do_unlink = True)
            bpy.data.cameras.remove(bpy.data.cameras[name], do_unlink = True)
    
    def createLightCopies(self, context):
        light_collection = context.scene.collection.children[context.scene.dataset_generator_light.collection_name]
        
        for object in light_collection.objects.values():
            if object.type == "LIGHT":
                light_copy = object.copy()
                data_copy = light_copy.data.copy()
                light_copy.data = data_copy
                context.scene.collection.children["Dataset Generator Scene Collection"].children["Dataset Generator Scene Light Collection"].objects.link(light_copy)
    
    def removeLightCopies(self, context):
        for light in context.scene.collection.children['Dataset Generator Scene Collection'].children["Dataset Generator Scene Light Collection"].objects.values():
            name = light.name
            bpy.data.objects.remove(bpy.data.objects[name], do_unlink = True)
            bpy.data.lights.remove(bpy.data.lights[name], do_unlink = True)
    
    def createBackgroundCopies(self, context):
        background_collection = context.scene.collection.children[context.scene.dataset_generator_background.collection_name]
        
        for object in background_collection.objects.values():
            if object.type == "MESH":
                background_copy = object.copy()
                data_copy = background_copy.data.copy()
                background_copy.data = data_copy
                context.scene.collection.children["Dataset Generator Scene Collection"].children["Dataset Generator Scene Background Collection"].objects.link(background_copy)
    
    def removeBackgroundCopies(self, context):
        for background in context.scene.collection.children['Dataset Generator Scene Collection'].children["Dataset Generator Scene Background Collection"].objects.values():
            name = background.name
            bpy.data.objects.remove(bpy.data.objects[name], do_unlink = True)
            bpy.data.meshes.remove(bpy.data.meshes[name], do_unlink = True)
    
    def modelSetting(self, context):
        for model in context.scene.collection.children.get("Dataset Generator Scene Collection").children.get("Dataset Generator Scene Model Collection").objects.values():
                self.showRenderModel(context, model.name)
    
    def cameraSetting(self, context):
        for camera in context.scene.collection.children.get("Dataset Generator Scene Collection").children.get("Dataset Generator Scene Camera Collection").objects.values():
                self.showRenderCamera(context, camera.name)
    
    def lightSetting(self, context):
        if self.getLightMode(context) == "ALL_LIGHTS_MODE":
            for light in context.scene.collection.children.get("Dataset Generator Scene Collection").children.get("Dataset Generator Scene Light Collection").objects.values():
                self.showRenderLight(context, light.name)
        elif self.getLightMode(context) == "RANDOM_LIGHTS_MODE":
            for light in context.scene.collection.children.get("Dataset Generator Scene Collection").children.get("Dataset Generator Scene Light Collection").objects.values():
                self.hideRenderLight(context, light.name)
    
    def backgroundSetting(self, context):
        for background in context.scene.collection.children.get("Dataset Generator Scene Collection").children.get("Dataset Generator Scene Background Collection").objects.values():
                self.hideRenderBackground(context, background.name)
    
    def renderSetting(self, context):
        if self.getRenderEngine(context) == "CYCLES_MODE":
            context.scene.render.engine = "CYCLES"
            
            if self.getDevice(context) == "CPU_MODE":
                context.scene.cycles.device = "CPU"
                context.preferences.addons["cycles"].preferences.compute_device_type = "NONE"
            elif self.getDevice(context) == "GPU_MODE":
                for compute_device_type in ("CUDA", "OPENCL", "HIP", "NONE"):
                    try:
                        context.scene.cycles.device = "GPU"
                        context.preferences.addons["cycles"].preferences.compute_device_type = compute_device_type
                        
                        break
                    except TypeError:
                        pass
            
            context.scene.cycles.samples = self.getSamplesCount(context)
        elif self.getRenderEngine(context) == "EEVEE_MODE":
            context.scene.render.engine = "BLENDER_EEVEE"
        
        context.scene.render.resolution_x = self.getResolutionX(context)
        context.scene.render.resolution_y = self.getResolutionY(context)
        
        if self.getTransparentMode(context) == True:
            context.scene.render.film_transparent = True
            context.scene.render.image_settings.color_mode = "RGBA"
        elif self.getTransparentMode(context) == False:
            context.scene.render.film_transparent = False
    
    def sceneSetting(self, context):
        for collection in context.scene.collection.children.values():
            if collection.name != "Dataset Generator Scene Collection":
                collection.hide_render = True
    
    def prepareModel(self, context, parent_child_dict):
        scene_material = None
        parent_material_dict = {}
        
        for parent in parent_child_dict.keys():
            parent_material_dict[parent] = self.getRandomMaterial(context, self.getModelMaterialKey(context, context.scene.collection.children["Dataset Generator Scene Collection"].children["Dataset Generator Scene Model Collection"].objects.get(parent_child_dict[parent][0])))
            
        for model in context.scene.collection.children.get("Dataset Generator Scene Collection").children.get("Dataset Generator Scene Model Collection").objects.values():
            self.setModelLocation(context, model, 0, 0, 0)
            self.setModelRotation(context, model, 0, 0, 0)
            self.showRenderModel(context, model.name)
            self.clearMaterial(context, model)
            
            if self.getSceneMaterialMode(context) == True:
                if scene_material == None:
                    scene_material = self.getRandomMaterial(context, self.getModelMaterialKey(context, model))
                
                if scene_material != None:
                    self.appendMaterial(context, model, scene_material)
            else:
                if self.getModelMaterialMode(context, model) == "SAME_MATERIAL_MODE":
                    for parent in parent_child_dict.keys():
                        if model.name in parent_child_dict[parent]:
                            material = parent_material_dict[parent]
                            
                            if material != None:
                                self.appendMaterial(context, model, material)
                elif self.getModelMaterialMode(context, model) == "RANDOM_MATERIAL_MODE":
                    material = self.getRandomMaterial(context, self.getModelMaterialKey(context, model))
                    
                    if material != None:
                        self.appendMaterial(context, model, material)
    
    def prepareCamera(self, context):
        cameras = context.scene.collection.children.get("Dataset Generator Scene Collection").children.get("Dataset Generator Scene Camera Collection").objects.values()
        
        if self.getCameraMode(context) == "ALL_CAMERAS_MODE":
            return cameras
        elif self.getCameraMode(context) == "RANDOM_CAMERAS_MODE":
            return [cameras[randint(0, len(cameras) - 1)]]
    
    def prepareLight(self, context):
        if self.getLightMode(context) == "RANDOM_LIGHTS_MODE":
            for light in context.scene.collection.children.get("Dataset Generator Scene Collection").children.get("Dataset Generator Scene Light Collection").objects.values():
                self.hideRenderLight(context, light.name)
            
            lights = context.scene.collection.children.get("Dataset Generator Scene Collection").children.get("Dataset Generator Scene Light Collection").objects.values()
            
            self.showRenderLight(context, lights[randint(0, len(lights) - 1)].name)
    
    def prepareBackground(self, context):
        for background in context.scene.collection.children.get("Dataset Generator Scene Collection").children.get("Dataset Generator Scene Background Collection").objects.values():
            self.hideRenderBackground(context, background.name)
    
        backgrounds = context.scene.collection.children.get("Dataset Generator Scene Collection").children.get("Dataset Generator Scene Background Collection").objects.values()
        background = backgrounds[randint(0, len(backgrounds) - 1)]
        
        self.showRenderBackground(context, background.name)
        self.clearMaterial(context, background)
        
        material = self.getRandomMaterial(context, self.getBackgroundMaterialKey(context, background))
        
        if material != None:
            self.appendMaterial(context, background, material)
        
        return background
    
    def showRenderModel(self, context, model_name):
        object = bpy.data.objects[model_name]
        
        if object.type == "MESH": 
            object.hide_render = False
    
    def hideRenderModel(self, context, model_name):
        object = bpy.data.objects[model_name]
        
        if object.type == "MESH": 
            object.hide_render = True
   
    def showRenderCamera(self, context, camera_name):
        object = bpy.data.objects[camera_name]
        
        if object.type == "CAMERA":
            object.hide_render = False

    def showRenderLight(self, context, light_name):
        object = bpy.data.objects[light_name]
        
        if object.type == "LIGHT": 
            object.hide_render = False
    
    def hideRenderLight(self, context, light_name):
        object = bpy.data.objects[light_name]
        
        if object.type == "LIGHT": 
            object.hide_render = True
    
    def showRenderBackground(self, context, background_name):
        object = bpy.data.objects[background_name]
        
        if object.type == "MESH": 
            object.hide_render = False
    
    def hideRenderBackground(self, context, background_name):
        object = bpy.data.objects[background_name]
        
        if object.type == "MESH": 
            object.hide_render = True 
    
    def clearMaterial(self, context, model):
        if model.type == "MESH":
            model.data.materials.clear()
    
    def appendMaterial(self, context, model, material):
        model.data.materials.append(material)
    
    def setModelLocation(self, context, model, x, y, z):
        model.location.x = x
        model.location.y = y
        model.location.z = z
        
        context.view_layer.update()
    
    def setModelRotation(self, context, model, x, y, z):
        model.rotation_euler.x = math.radians(x)
        model.rotation_euler.y = math.radians(y)
        model.rotation_euler.z = math.radians(z)

        context.view_layer.update()        
    
    def getBoundPlane(self, context, model):
        return [
            model.matrix_world @ Vector([model.bound_box[0][0], model.bound_box[0][1], model.bound_box[0][2]]),
            model.matrix_world @ Vector([model.bound_box[3][0], model.bound_box[3][1], model.bound_box[3][2]]),
            model.matrix_world @ Vector([model.bound_box[7][0], model.bound_box[7][1], model.bound_box[7][2]]),
            model.matrix_world @ Vector([model.bound_box[4][0], model.bound_box[4][1], model.bound_box[4][2]])
        ]
    
    def checkVertexCollision(self, context, bound_plane, vertex):
        if (bound_plane[0][1] <= vertex[1] and bound_plane[2][1] >= vertex[1]) and (bound_plane[0][0] <= vertex[0] and bound_plane[2][0] >= vertex[0]):
            #print(str(bound_plane[0][1]) + "     " + str(vertex[1]))
            #print(str(bound_plane[2][1]) + "     " + str(vertex[1]))
            #print(str(bound_plane[0][0]) + "     " + str(vertex[0]))
            #print(str(bound_plane[2][0]) + "     " + str(vertex[0]))
            #print("\n\n")
            return True
        
        return False
    
    def checkModelCollision(self, context, model_1, model_2):
        bound_plane_model_1 = self.getBoundPlane(context, model_1)
        bound_plane_model_2 = self.getBoundPlane(context, model_2)
        
        for vertex in bound_plane_model_2:
            if self.checkVertexCollision(context, bound_plane_model_1, vertex):
                return True
        
        return False
    
    def getRenderEngine(self, context):
        return context.scene.dataset_generator_render.render_engine
    
    def getDevice(self, context):
        return context.scene.dataset_generator_render.device
    
    def getSamplesCount(self, context):
        return context.scene.dataset_generator_render.samples
    
    def getResolutionX(self, context):
        return context.scene.dataset_generator_render.resolution_x
    
    def getResolutionY(self, context):
        return context.scene.dataset_generator_render.resolution_y
    
    def getTransparentMode(self, context):
        return context.scene.dataset_generator_render.transparent
    
    def getMaskRenderMode(self, context):
        return context.scene.dataset_generator_render.mask_render
    
    def getCollisionMode(self, context):
        return context.scene.dataset_generator_generator.collision
    
    def getSaveDirPath(self, context):
        return context.scene.dataset_generator_render.save_dir_path
    
    def getSceneCount(self, context):
        return context.scene.dataset_generator_generator.scene_count
    
    def getCameraMode(self, context):
        return context.scene.dataset_generator_camera.camera_mode
    
    def getLightMode(self, context):
        return context.scene.dataset_generator_light.light_mode
    
    def getStartIndex(self, context):
        return context.scene.dataset_generator_generator.start_index

    def getModelMaterialKey(self, context, model):
        return model.dataset_generator_model.material_key
        
    def getModelMaterialMode(self, context, model):
        return model.dataset_generator_model.material_mode
    
    def getSceneMaterialMode(self, context):
        return context.scene.dataset_generator_model.material_mode
    
    def getBackgroundMaterialKey(self, context, background):
        return background.dataset_generator_background.material_key
   
    def getRandomMaterial(self, context, material_key):
        materials = []
        
        for material in bpy.data.materials.values():
            print(material.name)
            if material.name.find(material_key) != -1:
                materials.append(material)
                
        material = None
        
        if len(materials) != 0:
            material = materials[randint(0, len(materials) - 1)]
        
        return material
   
classes = [
    GeneratorOperator
]

def register():
    for cl in classes:
        register_class(cl)

def unregister():
    for cl in reversed(classes):
        unregister_class(cl)

if __name__ == "__main__":
    register()