bl_info = {
    "name": "Privatve Object Loader",
    "author": "Mastermind",
    "version": (1, 0),
    "blender": (2, 80, 0),
}

import bpy

import os
from bpy.types import Operator
from bpy.props import FloatVectorProperty
from bpy_extras.object_utils import AddObjectHelper, object_data_add
from mathutils import Vector
 
 
 
texts = "" 
 
class OBJECT_PT_TextTool(bpy.types.Panel):
    bl_label = "PrivativeObjectLoader"
    bl_idname = "OBJECT_PT_texttool"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Loader"
    
 
    def draw(self, context):
        layout = self.layout
 
        row = layout.row()
        row = layout.row()
        row.label(text= "LoadObject")
        row = layout.row()
        
       # row = layout.split(factor= -0.9)

        row.operator("wm.textopbasic", text= "Set Object One", )
        row = layout.row()
        row.operator("wm.textopbasic2", text="Set Object Two", )
        
 
 
 
 
 

selected_faces = None
 
 
 
 
 
class WM_OT_textOpBasic(bpy.types.Operator):
    """Set The objects"""
    bl_idname = "wm.textopbasic"
    bl_label = "                            FilePath"

    file1 = open("C:\\Users\Gibson\Documents\AddonData\SlotOne.txt", "r")
    text : bpy.props.StringProperty(name="Set your filepath", default=file1.read(100))
    file1.close()
    
    selected_faces = None
    def __init__(self):
        selected_faces = None
        
        
        
    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)
    
   
    
        
 
    def execute(self, context):
        selected_faces =self.text
        file1 = open("C:\\Users\Gibson\Documents\AddonData\SlotOne.txt","a")
        file1.truncate(0)
        file1.write(selected_faces)
        file1.close()
        print("" +selected_faces)
        
       # t = self.text
        
        #bpy.ops.object.text_add(enter_editmode=True)
 
        return {'FINISHED'}


class WM_OT_textOpBasic2(bpy.types.Operator):
    """Set The objects2"""
    bl_idname = "wm.textopbasic2"
    bl_label = "                            FilePath"
    file1 = open("C:\\Users\Gibson\Documents\AddonData\SlotTwo.txt", "r")
    text: bpy.props.StringProperty(name="Set your filepath", default=file1.read(100))
    file1.close()
    selected_faces = None

    def __init__(self):
        selected_faces = None

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)

    def execute(self, context):
        selected_faces = self.text
        file1 = open("C:\\Users\Gibson\Documents\AddonData\SlotTwo.txt", "a")
        file1.truncate(0)
        file1.write(selected_faces)
        file1.close()
        print("" + selected_faces)

        # t = self.text

        # bpy.ops.object.text_add(enter_editmode=True)

        return {'FINISHED'}
    
    
class ImportOne(bpy.types.Operator):
    """ImportOne"""  # Use this as a tooltip for menu items and buttons.
    bl_idname = "add.importone"  # Unique identifier for buttons and menu items to reference.
    bl_label = "ImportOne"  # Display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}
    
        

    def execute(self, context):
        file1 = open("C://Users/Gibson/Documents/AddonData/SlotOne.txt","r")
        my_path = file1.read(100)
        print(my_path)
        file1.close()
        if os.path.exists(my_path):
            print("File loaded")
            bpy.ops.import_scene.fbx(filepath=my_path)
        else:
            print("File could not be found")
        for item in bpy.data.materials:
            item.blend_method = 'OPAQUE'
        return {'FINISHED'}  # Lets Blender know the operator finished successfully.
    
def menu_func(self, context):
    self.layout.operator(ImportOne.bl_idname)


class ImportTwo(bpy.types.Operator):
    """ImportTwo"""  # Use this as a tooltip for menu items and buttons.
    bl_idname = "add.importtwo"  # Unique identifier for buttons and menu items to reference.
    bl_label = "ImportTwo"  # Display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        file1 = open("C://Users/Gibson/Documents/AddonData/SlotTwo.txt", "r")
        my_path = file1.read(100)
        print(my_path)
        file1.close()
        if os.path.exists(my_path):
            print("File loaded")
            bpy.ops.import_scene.fbx(filepath=my_path)
        else:
            print("File could not be found")
        for item in bpy.data.materials:
            item.blend_method = 'OPAQUE'
        return {'FINISHED'}  # Lets Blender know the operator finished successfully.


def menu_func(self, context):
    self.layout.operator(ImportTwo.bl_idname)
 
    
 
 
 
 
 
def register():
    bpy.utils.register_class(ImportOne)
    bpy.types.VIEW3D_MT_mesh_add.append(menu_func)
    bpy.utils.register_class(ImportTwo)
    bpy.types.VIEW3D_MT_mesh_add.append(menu_func)
    bpy.utils.register_class(OBJECT_PT_TextTool)
  #  bpy.utils.register_class(OBJECT_PT_Spacing)
    bpy.utils.register_class(WM_OT_textOpBasic)
    bpy.utils.register_class(WM_OT_textOpBasic2)
 
 
def unregister():
    bpy.utils.unregister_class(ImportOne)
    bpy.utils.unregister_class(ImportTwo)
    bpy.utils.unregister_class(OBJECT_PT_TextTool)
   # bpy.utils.unregister_class(OBJECT_PT_Spacing)
    bpy.utils.unregister_class(WM_OT_textOpBasic)
    bpy.utils.unregister_class(WM_OT_textOpBasic2)
    #bpy.types.VIEW3D_MT_mesh_add.remove(add_object_button)
 
 
if __name__ == "__main__":
    register()