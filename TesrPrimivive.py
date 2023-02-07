bl_info = {
    "name": "Privatve Object Loader",
    "author": "Mastermind",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "description": "An addon for adding custom objects to ADD>MESH"
}

import bpy

import os
from bpy.types import Operator
from bpy.props import FloatVectorProperty
from bpy_extras.object_utils import AddObjectHelper, object_data_add
from mathutils import Vector


from pathlib import Path
home = str(Path.home())
print(home + "\Documents\AddonData\SlotOne.txt")

#f = open(str(Path.home()) + "\Documents\ObjectLoader","x")
if os.path.exists(str(Path.home()) + "\Documents\ObjectLoader"):
    print("Folder Exists")
else:
    os.mkdir(str(Path.home()) + "\Documents\ObjectLoader", 0o666)
    f = open(str(Path.home()) + "\Documents\ObjectLoader\SlotOne.txt","x")
    f = open(str(Path.home()) + "\Documents\ObjectLoader\SlotOneName.txt", "x")
    f = open(str(Path.home()) + "\Documents\ObjectLoader\SlotTwo.txt", "x")
    f = open(str(Path.home()) + "\Documents\ObjectLoader\SlotTwoName.txt", "x")
    f = open(str(Path.home()) + "\Documents\ObjectLoader\SlotThree.txt", "x")
    f = open(str(Path.home()) + "\Documents\ObjectLoader\SlotThreeName.txt", "x")


 
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
        row.label(text= "Name Won't Show Up Unless You Restart Blender")
        row = layout.row()
        row.label(text= "LoadObject")
        row = layout.row()
        
       # row = layout.split(factor= -0.9)

        row.operator("wm.textopbasic", text= "Set Object One", )
        row = layout.row()
        row.operator("wm.textopbasic2", text="Set Object Two", )
        row = layout.row()
        row.operator("wm.textopbasic3", text="Set Object Three", )
        
 
 
 
 
 

selected_faces = None
 
 
 
 
 
class WM_OT_textOpBasic(bpy.types.Operator):
    """Set The objects"""
    bl_idname = "wm.textopbasic"
    bl_label = "                            FilePath"
    home = str(Path.home())
    file1 = open(str(Path.home())+"\Documents\ObjectLoader\SlotOne.txt", "r")
    file2 = open(str(Path.home())+"\Documents\ObjectLoader\SlotOneName.txt", "r")


    text : bpy.props.StringProperty(name="Set your filepath", default=file1.read(100))
    text2: bpy.props.StringProperty(name="Set the name", default=file2.read(100))
    file1.close()
    file2.close()
    
    selected_faces = None
    def __init__(self):
        selected_faces = None
        
        
        
    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)
    
   
    
        
 
    def execute(self, context):
        nameFile = self.text2
        selected_faces =self.text
        home = str(Path.home())
        file1 = open(str(Path.home())+"\Documents\ObjectLoader\SlotOne.txt","a")
        file1.truncate(0)
        file1.write(selected_faces)
        file1.close()

        home = str(Path.home())
        file2 = open(str(Path.home())+"\Documents\ObjectLoader\SlotOneName.txt", "a")
        file2.truncate(0)
        file2.write(nameFile)
        file2.close()
        print("" +nameFile)
        
       # t = self.text
        
        #bpy.ops.object.text_add(enter_editmode=True)
 
        return {'FINISHED'}


class WM_OT_textOpBasic2(bpy.types.Operator):
    """Set The objects2"""
    bl_idname = "wm.textopbasic2"
    bl_label = "                            FilePath"
    home = str(Path.home())
    file1 = open(str(Path.home())+"\Documents\ObjectLoader\SlotTwo.txt", "r")
    file2 = open(str(Path.home())+"\Documents\ObjectLoader\SlotTwoName.txt", "r")
    text : bpy.props.StringProperty(name="Set your filepath", default=file1.read(100))
    text2 : bpy.props.StringProperty(name="Set the name", default=file2.read(100))
    file1.close()
    file2.close()
    selected_faces = None

    def __init__(self):
        selected_faces = None

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)

    def execute(self, context):
        selected_faces = self.text
        home = str(Path.home())
        file1 = open(str(Path.home())+"\Documents\ObjectLoader\SlotTwo.txt", "a")
        file1.truncate(0)
        file1.write(selected_faces)
        file1.close()
        print("" + selected_faces)
        nameFile = self.text2

        file2 = open(str(Path.home())+"\Documents\ObjectLoader\SlotTwoName.txt", "a")
        file2.truncate(0)
        file2.write(nameFile)
        file2.close()
        print("" + nameFile)

        # t = self.text

        # bpy.ops.object.text_add(enter_editmode=True)

        return {'FINISHED'}





class WM_OT_textOpBasic3(bpy.types.Operator):
    """Set The objects3"""
    bl_idname = "wm.textopbasic3"
    bl_label = "                            FilePath"
    home = str(Path.home())
    file1 = open(str(Path.home())+"\Documents\ObjectLoader\SlotThree.txt", "r")
    file2 = open(str(Path.home())+"\Documents\ObjectLoader\SlotThreeName.txt", "r")
    text: bpy.props.StringProperty(name="Set your filepath", default=file1.read(100))
    text2: bpy.props.StringProperty(name="Set the name", default=file2.read(100))
    file1.close()
    file2.close()
    selected_faces = None

    def __init__(self):
        selected_faces = None

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)

    def execute(self, context):
        selected_faces = self.text
        home = str(Path.home())
        file1 = open(str(Path.home())+"\Documents\ObjectLoader\SlotThree.txt", "a")
        file1.truncate(0)
        file1.write(selected_faces)
        file1.close()
        print("" + selected_faces)
        nameFile = self.text2

        file2 = open(str(Path.home())+"\Documents\ObjectLoader\SlotThreeName.txt", "a")
        file2.truncate(0)
        file2.write(nameFile)
        file2.close()
        print("" + nameFile)

        # t = self.text

        # bpy.ops.object.text_add(enter_editmode=True)

        return {'FINISHED'}


class ImportOne(bpy.types.Operator):
    """ImportOne"""  # Use this as a tooltip for menu items and buttons.
    bl_idname = "add.importone"  # Unique identifier for buttons and menu items to reference.
    home = str(Path.home())
    file1 = open(str(Path.home())+"\Documents/ObjectLoader/SlotOneName.txt", "r")
    my_path = file1.read(100)
    bl_label = my_path  # Display name in the interface.
    file1.close()
    bl_options = {'REGISTER', 'UNDO'}
    
        

    def execute(self, context):
        home = str(Path.home())
        file1 = open(str(Path.home())+"\Documents/ObjectLoader/SlotOne.txt","r")
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
    



class ImportTwo(bpy.types.Operator):
    """ImportTwo"""  # Use this as a tooltip for menu items and buttons.
    bl_idname = "add.importtwo"  # Unique identifier for buttons and menu items to reference.
    home = str(Path.home())
    file1 = open(str(Path.home())+"\Documents/ObjectLoader/SlotTwoName.txt", "r")
    my_path = file1.read(100)
    bl_label = my_path  # Display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        home = str(Path.home())
        file1 = open(str(Path.home())+"\Documents/ObjectLoader/SlotTwo.txt", "r")
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


class ImportThree(bpy.types.Operator):
    """ImportThree"""  # Use this as a tooltip for menu items and buttons.
    bl_idname = "add.importthree"  # Unique identifier for buttons and menu items to reference.
    home = str(Path.home())
    file1 = open(str(Path.home())+"\Documents/ObjectLoader/SlotThreeName.txt", "r")
    my_path = file1.read(100)
    bl_label = my_path  # Display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        home = str(Path.home())
        file1 = open(str(Path.home())+"\Documents/ObjectLoader/SlotThree.txt", "r")
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
    self.layout.operator(ImportTwo.bl_idname)
    self.layout.operator(ImportThree.bl_idname)
 
    
 
 
 
 
 
def register():
    bpy.utils.register_class(ImportOne)
   # bpy.types.VIEW3D_MT_mesh_add.append(menu_func)
    bpy.utils.register_class(ImportTwo)
    bpy.utils.register_class(ImportThree)
    bpy.types.VIEW3D_MT_mesh_add.append(menu_func)
    bpy.utils.register_class(OBJECT_PT_TextTool)
  #  bpy.utils.register_class(OBJECT_PT_Spacing)
    bpy.utils.register_class(WM_OT_textOpBasic)
    bpy.utils.register_class(WM_OT_textOpBasic2)
    bpy.utils.register_class(WM_OT_textOpBasic3)
 
 
def unregister():
    bpy.utils.unregister_class(ImportOne)
    bpy.utils.unregister_class(ImportTwo)
    bpy.utils.unregister_class(ImportThree)
    bpy.utils.unregister_class(OBJECT_PT_TextTool)
   # bpy.utils.unregister_class(OBJECT_PT_Spacing)
    bpy.utils.unregister_class(WM_OT_textOpBasic)
    bpy.utils.unregister_class(WM_OT_textOpBasic2)
    bpy.utils.unregister_class(WM_OT_textOpBasic3)
    #bpy.types.VIEW3D_MT_mesh_add.remove(add_object_button)
 
 
if __name__ == "__main__":
    register()