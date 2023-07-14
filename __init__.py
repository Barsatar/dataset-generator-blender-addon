bl_info = {
    "name": "Dataset Generator",
    "author": "Maxim Zhitenko aka Barsatar",
    "version": (1, 0, 0),
    "blender": (3, 4, 0),
    "location": "View3D > UI > Dataset Generator",
    "description": "Dataset generator for classification and object detection neural networks",
    "warning": "",
    "doc_url": "",
    "tracker_url": "",
    "category": "Scene"
}

import bpy

from . import model_panel
from . import camera_panel
from . import light_panel
from . import background_panel
from . import render_panel
from . import generator_panel

def register():
    model_panel.register()
    camera_panel.register()
    light_panel.register()
    background_panel.register()
    render_panel.register()
    generator_panel.register()

def unregister():
    model_panel.unregister()
    camera_panel.unregister()
    light_panel.unregister()
    background_panel.unregister()
    render_panel.unregister()
    generator_panel.unregister()

if __name__ == "__main__":
    register()