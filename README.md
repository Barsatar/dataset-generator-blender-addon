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
 
 > Documentation is under development.
</details>

<details>
 <summary><h2>Configuring the «Camera» panel</h2></summary>
 
 > Documentation is under development.
</details>

<details>
 <summary><h2>Configuring the «Light» panel</h2></summary>
 
 > Documentation is under development.
</details>

<details>
 <summary><h2>Configuring the «Background» panel</h2></summary>
 
 > Documentation is under development.
</details>

<details>
 <summary><h2>Configuring the «Render» panel</h2></summary>
 
 > Documentation is under development.
</details>

<details>
 <summary><h2>Configuring the «Generator» panel</h2></summary>
 
 > Documentation is under development.
</details>

<h1>Developers</h1>

+ [Barsatar](https://github.com/Barsatar)

<h1>License</h1>

The **Dataset Generator** add-on for the Blender 3D editor is distributed under the [MIT License](https://github.com/Barsatar/dataset-generator-blender-addon/blob/main/LICENSE.md).

<h1>From the author</h1>

The **Dataset Generator** add-on was developed for personal use, so it may contain various ~bugs~ features, errors, and the like. The created program is well suited for quickly creating and rendering a large number of simple 3D scenes, which can be used for training image processing-related neural networks.

If this add-on has been helpful to you, please consider giving it a star.
