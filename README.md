<p align="left">
 <a href="https://github.com/Barsatar/dataset-generator-blender-addon/blob/main/README.ru.md"><img src="https://img.shields.io/badge/RU-grey"></a>
 <a href="https://github.com/Barsatar/dataset-generator-blender-addon/blob/main/README.md"><img src="https://img.shields.io/badge/EN-grey"></a>
</p>

<picture>
 <img alt="Banner" src="https://github.com/Barsatar/Dataset_Generator_Addon_For_Blender/assets/61797005/26a39b03-83f4-46c9-adc3-56568467b942">
</picture>

<p align="center">
 <img src="https://img.shields.io/badge/Blender%20%20-%203.4.0%20-%20%23FF7400%09?logo=blender">
 <img src="https://img.shields.io/badge/Version%20%20-%20v1.0.0%20(Alpha)%20-%20%234479D4">
 <img src="https://img.shields.io/badge/License%20%20-%20MIT%20-%20%2300CC00">
</p>

<h1>About</h1>

**Dataset Generator** is an add-on for the Blender 3D editor that allows for the automatic assembly and rendering of scenes based on specified models of objects, background models, cameras, light sources, and materials. The objects in the generated scenes can be easily annotated and classified automatically, enabling their use in generating synthetic datasets for training image processing-related neural networks.

<h1>Download</h1>

| Blender | Version | Link |
| --- | --- | --- |
| 3.4.0 | v1.0.0 (Alpha) | [dataset_generator_blender-3.4.0_v1.0.0-alpha.zip](https://github.com/Barsatar/dataset-generator-blender-addon/releases/download/release/dataset_generator_blender-3.4.0_v1.0.0-alpha.zip)

<h1>Installation</h1>

1) Go to the «Edit» panel.
2) Open the «Preferences» window.
3) Navigate to the «Add-ons» section.
4) Click the «Install» button.
5) Choose the zip file containing the add-on and click the «Install Add-ons» button.
6) Check the checkbox next to the add-on to activate it.

<h1>Documentation</h1>

<details>
 <summary><h2>Location of the add-on in Blender</h2></summary>

 > **3D Viewport > UI > Dataset Generator**

 <picture>
  <img src="https://github.com/Barsatar/dataset-generator-blender-addon/assets/61797005/fb047b15-3336-4431-b28b-5ab7db8cf9d9">
 </picture>
</details>

<details>
 <summary><h2>Preparation before using the add-on</h2></summary>
 
 <picture>
  <img src="https://github.com/Barsatar/dataset-generator-blender-addon/assets/61797005/b6c7e514-da64-4316-80e5-d450cdb23551", height=300, align="left">
 </picture>
 
 The process of preparing the scene before using the **Dataset Generator** add-on is quite simple, but several steps need to be followed for the add-on to work correctly.

 <br clear="left">
 
 <h3>Step 1. Creating Collections</h3>
 
 + **«Model Collection»** is a collection intended for storing object models that will be used during scene generation.
 + **«Camera Collection»** is a collection intended for storing cameras that will be used during rendering of the generated scenes.
 + **«Light Collection»** is a collection intended for storing light sources that will be used during rendering of the generated scenes.
 + **«Background Collection»** is a collection intended for storing object models that will serve as the background for the object models from the «Model Collection» during scene generation.

 <picture>
  <img src="https://github.com/Barsatar/dataset-generator-blender-addon/assets/61797005/c1b2b736-c071-492f-9f7c-354de528d01a">
 </picture>

 <p></p>

 > **Note 1**: The names of the collections may differ from the names presented in this documentation.

 <h3>Step 2. Preparing object models for the «Model Collection»</h3>
 
 The «Model Collection» is intended for storing object models that are the target objects for detection, classification, or segmentation by neural networks. This means that only object models from this collection will have masks generated, which are necessary for automatically detecting object boundaries within the generated scene and assigning object classes.

 Before using the **Dataset Generator**, make sure that:
 
 + The object models have the «MESH» type.
 
   <picture>
    <img src="https://github.com/Barsatar/dataset-generator-blender-addon/assets/61797005/8388502d-6977-436e-9da8-a38236a58206">
   </picture>
  
   <p></p>

   > **Note 1**: The «Model Collection» can contain objects with other types, but they will not be used by the add-on during scene generation.\
   > **Note 2**: At least one object with the «MESH» type must be present in the «Model Collection» for the add-on to work.
 
 + The object model's name matches the object data name.
 
   <picture>
    <img src="https://github.com/Barsatar/dataset-generator-blender-addon/assets/61797005/949c31d1-1884-44a9-8e67-67c98c5ec7fb">
   </picture>
 
 + Object models composed of multiple parts are merged into a single object and have a single object data.
 
   <picture>
    <img src="https://github.com/Barsatar/dataset-generator-blender-addon/assets/61797005/4fe6e576-9029-44ea-8535-f0db199a655c" height=150>
   </picture>
  
   <p></p>
   
   > **Note 3**: Parts of a composite object model that are not merged into a single object and do not have a single object data will be treated as separate object models by the add-on.
 
 + The origin points of the object models are located in the desired positions.
 
   <picture>
    <img src="https://github.com/Barsatar/dataset-generator-blender-addon/assets/61797005/7b08aabd-0980-4ac7-ad33-08d70ed5977d" height=150>
   </picture>

 <h3>Step 3. Preparing cameras for the «Camera Collection»</h3>
 
 The «Camera Collection» is intended for storing cameras that will be used for rendering the created scenes. The main task during preparation is to position the cameras in the desired locations within the scene.

 Before using the **Dataset Generator**, make sure that:

 + The camera objects have the «CAMERA» type.

   <picture>
    <img src="https://github.com/Barsatar/dataset-generator-blender-addon/assets/61797005/56237f0a-4c19-41f0-9fd1-fd1623206d88">
   </picture>
   
   <p></p>
   
   > **Note 1**: The «Camera Collection» can contain objects with other types, but they will not be used by the add-on for rendering scenes.
   > **Note 2**: At least one object with the «CAMERA» type must be present in the «Camera Collection» for the add-on to work.

 + The camera object's name matches the camera data name.

   <picture>
    <img src="https://github.com/Barsatar/dataset-generator-blender-addon/assets/61797005/48373a15-bfab-4470-ac1d-29937899a294">
   </picture>
 
 <h3>Step 4. Preparing light sources for the «Light Collection»</h3>
 
 The «Light Collection» is intended for storing light sources that will be used for rendering the created scenes. The main task during preparation is to position the light sources in the desired locations within the scene.

 Before using the **Dataset Generator**, make sure that:

 + The light source objects have the «LIGHT» type.

   <picture>
    <img src="https://github.com/Barsatar/dataset-generator-blender-addon/assets/61797005/bf5a5fc3-cad5-4351-ad4c-643d356e3cd4">
   </picture>
   
   <p></p>
  
   > **Note 1**: The «Light Collection» can contain objects with other types, but they will not be used by the add-on for rendering scenes.\
   > **Note 2**: At least one object with the «LIGHT» type must be present in the «Light Collection» for the add-on to work.

 + The light source object's name matches the light source data name.

   <picture>
    <img src="https://github.com/Barsatar/dataset-generator-blender-addon/assets/61797005/0a9ca4ce-872f-4a53-be70-2174106d7ea4">
   </picture>

 <h3>Step 5. Preparing background object models for the «Background Collection»</h3>

 The «Background Collection» is intended for storing background object models, where the vertices are used as anchor points for the object models from the «Model Collection» during scene generation. The main tasks during preparation are positioning the background object models in the desired locations within the scene and forming vertex groups that will be used to anchor the object models from the «Model Collection».

 <picture>
  <img src="https://github.com/Barsatar/dataset-generator-blender-addon/assets/61797005/cef98e9f-31c1-4770-8887-e6a9ce0c473e" height=200 align="left">
 </picture>

 <picture>
  <img src="https://github.com/Barsatar/dataset-generator-blender-addon/assets/61797005/a75a26ba-bc08-4151-ab64-14e444ca1107" height=200>
 </picture>

 <br clear="left">
 <p></p>

 Before using the **Dataset Generator**, make sure that:

 + The background object models have the «MESH» type.

   <picture>
    <img src="https://github.com/Barsatar/dataset-generator-blender-addon/assets/61797005/630287f1-a143-4edd-b40e-f904bc8f61ed">
   </picture>

   <p></p>
  
   > **Note 1**: The «Background Collection» can contain objects with other types, but they will not be used by the add-on for scene generation.\
   > **Note 2**: At least one object with the «MESH» type must be present in the «Background Collection» for the add-on to work.

 + The background object model's name matches the object data name.

   <picture>
    <img src="https://github.com/Barsatar/dataset-generator-blender-addon/assets/61797005/229c362d-ec82-49ed-b372-545d4d1e5eab">
   </picture>
  
 + Vertex groups are assigned to the background object models.

   <picture>
    <img src="https://github.com/Barsatar/dataset-generator-blender-addon/assets/61797005/f50fb510-687b-4dee-836a-90ed5afabe72">
   </picture>
  
   <p></p>
  
   > **Note 3**: For the add-on to work, each background object model from the «Background Collection»  must have at least one vertex group assigned.

 + Background object models composed of multiple parts are merged into a single object and have a single object data.

   <p></p>

   > **Note 4**: Parts of a composite background object model that are not merged into a single object and do not have a single object data will be treated as separate background object models by the add-on.

 <h3>Step 6. Preparing materials for models</h3>

 Materials for the target object models and background object models do not require any specific preparation. For convenience in assigning materials to models, it is recommended to name the materials according to a methodology that allows for quick grouping of materials. For example, **«Model Type» > «Material Type» > «Material Number»**.

 <picture>
  <img src="https://github.com/Barsatar/dataset-generator-blender-addon/assets/61797005/29756a81-3c1b-4660-8d31-85e290470bcd">
 </picture>

 <p></p>

 It is also recommended to create a separate object that is not involved in scene generation, where all created materials will be stored. This is because there is a risk of losing materials during the process of using this add-on.
</details>

<details>
 <summary><h2>Configuring the «Model» panel</h2></summary>
 
 <picture>
  <img src="https://github.com/Barsatar/dataset-generator-blender-addon/assets/61797005/fb033625-f356-40ef-a383-33fc29937ab0" height=300>
 </picture>

 ---
 
 + **«Models collection»** is a panel component that takes a collection containing object models as input.

 + **«Model»** is a panel component that takes an object model of type «MESH» as input.

 + **«Model class»** is a panel component used to specify the class of the object model, which will be assigned to the copies of the object model during mask generation.

   <p></p>
 
   > **Note 1**: When this parameter is left empty, mask generation for the copies of the object model will not be performed.
   > **Note 2**: The value of this parameter can be the same for multiple object models.

 + **«Number of model instances»** is a panel component that allows specifying the number of copies of the object model to be used during scene generation.

   <p></p>
  
   > **Note 3**: The minimum value of this parameter is 0. The maximum value is unlimited. The default value is 1.

 + **«Material key»** is a panel component that allows specifying a keyword present in the names of materials from which the material for the copies of the object model will be selected during the generation of each scene.

   <picture>
    <img src="https://github.com/Barsatar/dataset-generator-blender-addon/assets/61797005/ed989e90-39a7-4570-bb8e-bd62060fe67b">
   </picture>
   
   Example usage of this parameter:\
   — With «Material key» set to «background_tiles_1», the available materials for scene generation will consist of the material «background_tiles_1».\
   — With «Material key» set to «background_tiles», the available materials for scene generation will consist of the materials «background_tiles_1», «background_tiles_2», «background_tiles_3».\
   — With «Material key» set to «background», the available materials for scene generation will consist of the materials «background_beton_1», «background_covrolin_1», «background_ground_1», «background_linolium_1», «background_tiles_1», «background_tiles_2», «background_tiles_3», «background_wood_1», «background_wood_2».

   <p></p>

   > **Note 4**: When this parameter is left empty, the material for the copies of the object model will be randomly selected from all existing materials in the scene.

 + **«Material mode»** is a panel component that allows selecting the mode for choosing materials for the copies of the object model. The **«Random material»** mode selects a random material for each copy of the object model, while the **«Same material»** mode selects the same random material for all copies of the object model.

   <p></p>

   > **Note 5**: The default value of this parameter is «Same material».

 + **«Scene material mode»** is a panel component that allows selecting the material mode where one random material is chosen for all copies of all object models used in the scene generation.

   <p></p>
  
   > **Note 6**: This panel component is available only when the values of the «Material key» component match for all object models.
</details>

<details>
 <summary><h2>Configuring the «Camera» panel</h2></summary>
 
 <picture>
  <img src="https://github.com/Barsatar/dataset-generator-blender-addon/assets/61797005/91c6ce37-9eea-4191-afca-c0f320f34420" height=300>
 </picture>

 ---
 
 + **«Cameras collection»** is a panel component that takes a collection containing camera objects as input, which will be used for rendering the generated scenes.
 + **«Camera mode»** is a panel component that allows selecting the mode for choosing cameras to be used for rendering the generated scene. The **«Render with all cameras»** mode performs sequential rendering of the generated scene using all cameras, while the **«Render with random camera»** mode performs rendering of the generated scene using only one randomly selected camera.

   <p></p>

   > **Note 1**: The default value of this parameter is «Render with all cameras».
</details>

<details>
 <summary><h2>Configuring the «Light» panel</h2></summary>
 
 <picture>
  <img src="https://github.com/Barsatar/dataset-generator-blender-addon/assets/61797005/314adf25-4140-4fb9-80b9-d3f23586e1f0" height=300>
 </picture>

 ---
 
 + **«Lights collection»** is a panel component that takes a collection containing light source objects as input, which will be used for rendering the generated scenes.

 + **«Light mode»** is a panel component that allows selecting the mode for choosing light sources to be used for rendering the generated scene. The **«Render with all lights»** mode performs rendering of the generated scene using all light sources simultaneously, while the **«Render with random light»** mode performs rendering of the generated scene using only one randomly selected light source.

   <p></p>
   
   > **Note 1**: The default value of this parameter is «Render with all lights».
</details>

<details>
 <summary><h2>Configuring the «Background» panel</h2></summary>
 
 <picture>
  <img src="https://github.com/Barsatar/dataset-generator-blender-addon/assets/61797005/92be8407-e84c-4eb6-849d-199ae249ba82" height=300>
 </picture>
 
 <p></p>
 
 > **Note 1**: During the generation of each scene, the background object model is randomly selected from the models in the corresponding collection.

 ---

 + **«Backgrounds collection»** is a panel component that takes a collection containing background object models as input.

 + **«Background»** is a panel component that takes a background object model with type «MESH» as input.

 + **«Vertex Group»** is a panel component that takes a vertex group belonging to the selected background object model as input.

 + **«Material key»** is a panel component that allows specifying a keyword present in the material names from which the material for the background object model will be chosen during the generation of each scene.

   <p></p>
   
   > **Note 2**: If this parameter is left empty, the material for the background object model will be randomly chosen from all existing materials in the scene.\
   > **Note 3**: The logic of this component works similarly to the «Material key» component from the «Model» panel.
</details>

<details>
 <summary><h2>Configuring the «Render» panel</h2></summary>
 
 <picture>
  <img src="https://github.com/Barsatar/dataset-generator-blender-addon/assets/61797005/a93844f6-7ef1-4032-be45-1ba07bb8f836" height=300>
 </picture>

 ---
 
 + **«Render engine»** is a panel component that allows you to select the rendering technology to be used for rendering the generated scenes. There are two options available: **«Cycles»** and **«Eevee»**.

   <p></p>
 
   > **Note 1**: The default value for this parameter is «Cycles».

 + **«Device»** is a panel component that allows you to select the compute device to be used for rendering the generated scenes. There are two options available: **«GPU»** and **«CPU»**.

   <p></p>
   
   > **Note 2**: The default value for this parameter is «GPU».\
   > **Note 3**: This component is only available for the «Cycles» rendering technology.

 + **«Samples"** is a panel component that allows you to specify the number of samples to be used during the rendering process.

   <p></p>
   
   > **Note 4**: The minimum value for this parameter is 0. There is no maximum limit. The default value for this parameter is 50.\
   > **Note 5**: This component is only available for the «Cycles» rendering technology.

 + **«Resolution»** is a panel component that allows you to specify the horizontal (left component) and vertical (right component) resolution to be used for rendering the scenes.

   <p></p>
   
   > **Note 6**: The values of these parameters are measured in pixels (px).\
   > **Note 7**: The minimum value for these parameters is 0 px. There is no maximum limit. The default values for these parameters are 800 px and 600 px for the horizontal and vertical components, respectively.

 + **«Transparent»** is a panel component that allows you to select the state of the Blender background transparency during rendering. When active, the Blender background will be transparent.

   <p></p>
   
   > **Note 8**: By default, this component is inactive.

 + **«Mask render»** is a panel component that allows you to select the state of rendering masks for the object model copies used in scene generation. When active, the masks for the object model copies will be rendered.

   <picture>
    <img src="https://github.com/Barsatar/dataset-generator-blender-addon/assets/61797005/e9abbd97-83b5-4b0c-922f-9d3c23ff38c3" height=400>
   </picture>
   
   When the mask rendering mode is active, in addition to visualizing the main scene, masks for all object model copies used in scene generation will also be visualized. The generated masks can be divided into two types: object masks (for object model copies that are within the camera's field of view) and «dark masks» (for object model copies that are outside the camera's field of view).

   The naming logic for scene images is as follows:\
   **«DGImage__»** indicates that the image is a scene render.\
   **«4__»** is the number assigned to the created image.

   The naming logic for object model copy masks is as follows:\
   **«DGMask__»** indicates that the image is a mask render for an object model copy.\
   **«4__»** is the number assigned to the corresponding scene image.\
   **«DGObject__Cube_1.001__»** is the name of the object model copy to which the mask belongs.\
   **«DGClass__cube__»** is the class designation of the original object model to which the copy belongs.

   > **Note 9**: By default, this component is active.\
   > **Note 10**: The background of the masks is transparent.\
   > **Note 11**: When using the «Cycles» rendering technology, mask rendering is performed with the «Samples» parameter set to 0.\
   > **Note 12**: The generated scene images and masks are saved in the «PNG» format.\
   > **Note 13**: Double underscore («__») is used to separate elements in the image names.

   ---

   > **Author's note**: There may be a link to software for automatic annotation and labeling of images presented in this format added here later.

 + **«Save path»** is a panel component that allows you to specify the location where the images generated by the **Dataset Generator** add-on will be saved. The path can be entered manually or selected using the file explorer. In the specified location, a folder named «dataset_generator» will be created, which will contain subfolders with the generated scene images and masks.

   <p></p>

   > **Note 14**: By default, the value of this component is empty.
</details>

<details>
 <summary><h2>Configuring the «Generator» panel</h2></summary>
 
 <picture>
  <img src="https://github.com/Barsatar/dataset-generator-blender-addon/assets/61797005/5c773bb5-68b1-4293-baa3-33ecf1f7368f" height=300>
 </picture>

 ---
 
 + **«Scene count»** is a panel component that allows specifying the number of scenes to be generated by the add-on.
   
   <p></p>
   
   > **Note 1**: The minimum value of this parameter is 0. The maximum value is unlimited. The default value is 0.\
   > **Note 2**: The final number of images obtained as a result of the add-on's operation depends on the selected mode of the «Camera mode» component from the «Camera» panel, the number of cameras used, and the number of generated scenes. For example, with a «Camera mode» value of «Render with all cameras», 5 used cameras, and a «Scene count» value of 10, 10 scenes will be generated and 50 images will be visualized.

 + **«Start index»** is a panel component that allows specifying the index from which the visualization image names will start.
   
   <p></p>
   
   > **Note 3**: The minimum value of this parameter is 0. The maximum value is unlimited. The default value is 0.

 + **«Collision»** is a panel component that allows selecting the collision detection mode during the placement of object model instances on the background object model during scene generation. Collision detection is enabled in the active state.

   <picture>
     <img src="https://github.com/Barsatar/dataset-generator-blender-addon/assets/61797005/089b5e3a-9806-4b10-b52b-96fa6bdabd27" height=150>
   </picture>
   
   The collision detection mechanism is based on the use of bounding boxes that can be represented as cubes. Using such a simplified representation of object boundaries does not allow for precise collision detection of object model instances with complex shapes. Therefore, there may be inefficient use of space on the background object model when the «Collision» mode is active.
   
   <p></p>
   
   > **Note 4**: By default, this component is active.\
   > **Note 5**: In situations where it is not possible to place an object model instance on the background object model without colliding with already placed object model instances, such an instance does not participate in scene generation.\
   > **Note 6**: The selection of object model instances for placement on the background object model is not random, so there may be situations where not all original object models are present in the generated scene. This is because there was not enough space to correctly place instances of some object models on the background object model.

 + **«Start»** is a panel component designed to initiate the process of scene generation and rendering.
   
   This component becomes interactable under the following conditions:\
   — The «Models Collection» component from the «Model» panel is not empty.\
   — The collection specified in the «Models Collection» component from the «Model» panel contains at least one object of type «MESH».\
   — The «Cameras Collection» component from the «Camera» panel is not empty.\
   — The collection specified in the «Cameras Collection» component from the «Camera» panel contains at least one object of type «CAMERA».\
   — The «Lights Collection» component from the «Light» panel is not empty.\
   — The collection specified in the «Lights Collection» component from the «Light» panel contains at least one object of type «LIGHT».\
   — The «Backgrounds Collection» component from the «Background» panel is not empty.\
   — The collection specified in the «Backgrounds Collection» component from the «Background» panel contains at least one object of type «MESH».\
   — Each object of type «MESH» from the collection specified in the «Backgrounds Collection» component from the «Background» panel has at least one vertex group that has been passed to the corresponding «Vertex group» component from the «Background» panel.

   <p></p>
   
   > **Note 7**: During the operation of the add-on, the Blender graphical interface may become unresponsive.
</details>

<h1>Developers</h1>

+ [Barsatar](https://github.com/Barsatar)

<h1>License</h1>

The **Dataset Generator** add-on for the Blender 3D editor is distributed under the [MIT License](https://github.com/Barsatar/dataset-generator-blender-addon/blob/main/LICENSE.md).

<h1>From the author</h1>

The **Dataset Generator** add-on was developed for personal use, so it may contain various ~bugs~ features, errors, and the like. The created program is well suited for quickly creating and rendering a large number of simple 3D scenes, which can be used for training image processing-related neural networks.

If this add-on has been helpful to you, please consider giving it a star.
