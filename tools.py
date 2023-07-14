class Tools:
    def searchCollectionNames(self, context, edit_text):
        collectionNames = []
        
        for collection in context.scene.collection.children.values():
            collectionNames.append((collection.name, ""))
        
        return collectionNames

    def searchModelNames(self, context, edit_text):
        modelNames = []
        
        for object in context.scene.collection.children.get(context.scene.dataset_generator_model.collection_name).objects.values():
            if object.type == "MESH":
                modelNames.append((object.name, ""))
        
        return modelNames
    
    def searchBackgroundNames(self, context, edit_text):
        backgroundNames = []
        
        for object in context.scene.collection.children.get(context.scene.dataset_generator_background.collection_name).objects.values():
            if object.type == "MESH":
                backgroundNames.append((object.name, ""))
        
        return backgroundNames
    
    def searchVertexGroupNames(self, context, edit_text):
        vertexGroupNames = []
        
        for vertexGroup  in  context.scene.collection.children[context.scene.dataset_generator_background.collection_name].objects.get(context.scene.dataset_generator_background.background_name).vertex_groups.values():
            vertexGroupNames.append((vertexGroup.name, ""))
        
        return vertexGroupNames
    
    def searchCameraNames(self, context, edit_text):
        cameraNames = []
        
        for object in context.scene.collection.children.get(context.scene.dataset_generator_camera.collection_name).objects.values():
            if object.type == "CAMERA":
                cameraNames.append((object.name, ""))
        
        return cameraNames
    
    def searchLightNames(self, context, edit_text):
        lightNames = []
        
        for object in context.scene.collection.children.get(context.scene.dataset_generator_light.collection_name).objects.values():
            if object.type == "LIGHT":
                lightNames.append((object.name, ""))
        
        return lightNames
        
    def isCollection(self, context, collection_name):
        for collection in context.scene.collection.children.values():
            if collection_name == collection.name:
                return True
        
        return False
    
    def isModelFromModelCollection(self, context, object_name):
        for object in context.scene.collection.children.get(context.scene.dataset_generator_model.collection_name).objects.values():
            if object_name == object.name and object.type == "MESH":
                return True
        
        return False
    
    def isBackgroundFromBackgroundCollection(self, context, object_name):
        for object in context.scene.collection.children.get(context.scene.dataset_generator_background.collection_name).objects.values():
            if object_name == object.name and object.type == "MESH":
                return True
        
        return False
    
    def isVertexGroupFromBackground(self, context, vertex_group_name, background_name):
        for vertex_group  in  context.scene.collection.children[context.scene.dataset_generator_background.collection_name].objects.get(background_name).vertex_groups.values():
            if vertex_group_name == vertex_group.name:
                return True
        
        return False
    
    def isCameraFromCameraCollection(self, context, object_name):
        for object in context.scene.collection.children.get(context.scene.dataset_generator_camera.collection_name).objects.values():
            if object_name == object.name and object.type == "CAMERA":
                return True
        
        return False
    
    def isLightFromLightCollection(self, context, object_name):
        for object in context.scene.collection.children.get(context.scene.dataset_generator_light.collection_name).objects.values():
            if object_name == object.name and object.type == "LIGHT":
                return True
        
        return False
         
    def isNotEmptyModelCollection(self, context):
        for object in context.scene.collection.children.get(context.scene.dataset_generator_model.collection_name).objects.values():
            if object.type == "MESH":
                return True
        
        return False
    
    def isNotEmptyBackgroundCollection(self, context):
        for object in context.scene.collection.children.get(context.scene.dataset_generator_background.collection_name).objects.values():
            if object.type == "MESH":
                return True
        
        return False
    
    def isNotEmptyCameraCollection(self, context):
        for object in context.scene.collection.children.get(context.scene.dataset_generator_camera.collection_name).objects.values():
            if object.type == "CAMERA":
                return True
        
        return False
    
    def isNotEmptyLightCollection(self, context):
        for object in context.scene.collection.children.get(context.scene.dataset_generator_light.collection_name).objects.values():
            if object.type == "LIGHT":
                return True
        
        return False