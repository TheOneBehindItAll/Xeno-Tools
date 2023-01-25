bl_info = {
     "name": "Xeno3 Model Cleaner",
    "author": "Mastermind",
    "version": (1, 0),
    "blender": (3, 4, 0),
    "location": "Object",
    "description": "This is an addon for cleaning up the main charecter models from Xenoblace Chronicals 3. It removes their face bits that get in the way and sets their show backface to false",
    "category": "All"
}


import bpy
 
 
 
class ADDONNAME_PT_TemplatePanel(bpy.types.Panel):
    bl_label = "Xeno3 Face Cleaner"
    bl_idname = "ADDONNAME_PT_TemplatePanel"
    bl_space_type = "VIEW_3D"
    bl_region_type = 'UI'
    bl_category = "Xeno3 Face Cleaner"
    
    def draw(self, context):
        layout = self.layout
        
        layout.operator("wm.template_operator")
        
 
 
 
 
 
class ADDONAME_OT_TemplateOperator(bpy.types.Operator):
    bl_label = "Face Clean up"
    bl_idname = "wm.template_operator"
    
    
    preset_enum : bpy.props.EnumProperty(
        name="",
        description = "",
        items = [ 
            ('Noah', "Noah", "Deletes Noah's face bits"),
            ('Mio', "Mio", "Deletes Mio's face bits"),
            ('Lanz', "Lanz", "Deletes Lanz's face bits"),
            ('Sena', "Sena", "Deletes Sena's face bits"),
            ('Euine', "Euine", "Deletes Euine's face bits"),
            ('Taion', "Taion", "Deletes Taion's face bits"),
        
        
        
        
        ]
    
    
    
    
    )
    
    
    
    
    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)
    
    
    def draw(self, context):
        layout = self.layout
        layout.prop(self,"preset_enum")
        
    
    def execute(self, context):
        
        for item in bpy.data.materials:
             item.blend_method = 'OPAQUE'
        
        if self.preset_enum == 'Noah':
               bpy.ops.object.select_all(action='DESELECT')
               bpy.data.objects['eyepatch_toon'].select_set(True)
               bpy.ops.object.delete()
               bpy.ops.object.select_all(action='DESELECT')
               bpy.data.objects['sub_shadow2'].select_set(True)
               bpy.ops.object.delete()
               bpy.ops.object.select_all(action='DESELECT')
               bpy.data.objects['eye_shadow1_9_shape'].select_set(True)
               bpy.ops.object.delete()
               bpy.ops.object.select_all(action='DESELECT')
               bpy.data.objects['eye2_subs2'].select_set(True)
               bpy.ops.object.delete()
               bpy.ops.object.select_all(action='DESELECT')
               bpy.data.objects['add_eye1'].select_set(True)
               bpy.ops.object.delete()
               bpy.ops.object.select_all(action='DESELECT')
               bpy.data.objects['eye_hi2'].select_set(True)
               bpy.ops.object.delete()
               bpy.ops.object.select_all(action='DESELECT')
               bpy.data.objects['matu_alpha2_shape'].select_set(True)
               bpy.ops.object.delete()
               bpy.ops.object.select_all(action='DESELECT')
               bpy.data.objects['0012_kote02_pbr'].select_set(True)
               bpy.ops.object.delete()
               bpy.ops.object.select_all(action='DESELECT')
               bpy.data.objects['0004_sub_shadow3'].select_set(True)
               bpy.ops.object.delete()
                  
     
               
        if self.preset_enum == "Mio":
              bpy.ops.object.select_all(action='DESELECT')
              bpy.data.objects['eyepatch_toon'].select_set(True)
              bpy.ops.object.delete()
              bpy.ops.object.select_all(action='DESELECT')
              bpy.data.objects['hair_shadow'].select_set(True)
              bpy.ops.object.delete()
              bpy.ops.object.select_all(action='DESELECT')
              bpy.data.objects['eye_shadow3_shape'].select_set(True)
              bpy.ops.object.delete()
              bpy.ops.object.select_all(action='DESELECT')
              bpy.data.objects['eye2_subs1'].select_set(True)
              bpy.ops.object.delete()
              bpy.ops.object.select_all(action='DESELECT')
              bpy.data.objects['tooth4_shape'].select_set(True)
              bpy.ops.object.delete()
              bpy.ops.object.select_all(action='DESELECT')
              bpy.data.objects['skin_hi3_shape'].select_set(True)
              bpy.ops.object.delete()
              bpy.ops.object.select_all(action='DESELECT')
              bpy.data.objects['add_eye1'].select_set(True)
              bpy.ops.object.delete()
              bpy.ops.object.select_all(action='DESELECT')
              bpy.data.objects['eye_hi2'].select_set(True)
              bpy.ops.object.delete()
              bpy.ops.object.select_all(action='DESELECT')
              bpy.data.objects['matu_c_alpha2_shape'].select_set(True)
              bpy.ops.object.delete()
              bpy.ops.object.select_all(action='DESELECT')
              bpy.data.objects['0006_hair_shadow'].select_set(True)
              bpy.ops.object.delete()
              
        if self.preset_enum == "Euine":
                 bpy.ops.object.select_all(action='DESELECT')
                 bpy.data.objects['eyepatch_toon'].select_set(True)
                 bpy.ops.object.delete()
                 bpy.ops.object.select_all(action='DESELECT')
                 bpy.data.objects['eye2_subs'].select_set(True)
                 bpy.ops.object.delete()
                 bpy.ops.object.select_all(action='DESELECT')
                 bpy.data.objects['eye_add'].select_set(True)
                 bpy.ops.object.delete()
                 bpy.ops.object.select_all(action='DESELECT')
                 bpy.data.objects['eye_hi'].select_set(True)
                 bpy.ops.object.delete()
                 bpy.ops.object.select_all(action='DESELECT')
                 bpy.data.objects['eye_shadow_shape'].select_set(True)
                 bpy.ops.object.delete()
                 bpy.ops.object.select_all(action='DESELECT')
                 bpy.data.objects['face_C1'].select_set(True)
                 bpy.ops.object.delete()
                 bpy.ops.object.select_all(action='DESELECT')
                 bpy.data.objects['face_C_alpha1_shape'].select_set(True)
                 bpy.ops.object.delete()
                 bpy.ops.object.select_all(action='DESELECT')
                 bpy.data.objects['futae_shadow2_shape'].select_set(True)
                 bpy.ops.object.delete()
                 bpy.ops.object.select_all(action='DESELECT')
                 bpy.data.objects['hair_shadow3'].select_set(True)
                 bpy.ops.object.delete()
                 bpy.ops.object.select_all(action='DESELECT')
                 bpy.data.objects['matu_alpha_shape'].select_set(True)
                 bpy.ops.object.delete()
                 bpy.ops.object.select_all(action='DESELECT')
                 bpy.data.objects['skin_hi_shape'].select_set(True)
                 bpy.ops.object.delete()
                 bpy.ops.object.select_all(action='DESELECT')
                 bpy.data.objects['0001_hair_shadow3'].select_set(True)
                 bpy.ops.object.delete()
                 
        if self.preset_enum == "Taion":
                  bpy.ops.object.select_all(action='DESELECT')
                  bpy.data.objects['_eye_Set_eye2_subs1'].select_set(True)
                  bpy.ops.object.delete()
                  bpy.ops.object.select_all(action='DESELECT')
                  bpy.data.objects['_eye_shadow_shape'].select_set(True)
                  bpy.ops.object.delete()
                  bpy.ops.object.select_all(action='DESELECT')
                  bpy.data.objects['eye_add'].select_set(True)
                  bpy.ops.object.delete()
                  bpy.ops.object.select_all(action='DESELECT')
                  bpy.data.objects['eye_hi'].select_set(True)
                  bpy.ops.object.delete()
                  bpy.ops.object.select_all(action='DESELECT')
                  bpy.data.objects['eye_hiB'].select_set(True)
                  bpy.ops.object.delete()
                  bpy.ops.object.select_all(action='DESELECT')
                  bpy.data.objects['eye_ref'].select_set(True)
                  bpy.ops.object.delete()
                  bpy.ops.object.select_all(action='DESELECT')
                  bpy.data.objects['eyepatch_toon'].select_set(True)
                  bpy.ops.object.delete()
                  bpy.ops.object.select_all(action='DESELECT')
                  bpy.data.objects['lambert1'].select_set(True)
                  bpy.ops.object.delete()
                  bpy.ops.object.select_all(action='DESELECT')
                  bpy.data.objects['sub_shadow2'].select_set(True)
                  bpy.ops.object.delete()
                  
        if self.preset_enum == "Lanz":
         bpy.ops.object.select_all(action='DESELECT')
         bpy.data.objects['eyepatch_toon'].select_set(True)
         bpy.ops.object.delete()
         bpy.ops.object.select_all(action='DESELECT')
         bpy.data.objects['eyepatch_shadow'].select_set(True)
         bpy.ops.object.delete()
         bpy.ops.object.select_all(action='DESELECT')
         bpy.data.objects['eyeshadow_toon_shape'].select_set(True)
         bpy.ops.object.delete()
         bpy.ops.object.select_all(action='DESELECT')
         bpy.data.objects['facealp_toon_shape'].select_set(True)
         bpy.ops.object.delete()
         bpy.ops.object.select_all(action='DESELECT')
         bpy.data.objects['kokuin_shape'].select_set(True)
         bpy.ops.object.delete()
         bpy.ops.object.select_all(action='DESELECT')
         bpy.data.objects['line_toon_shape'].select_set(True)
         bpy.ops.object.delete()
         bpy.ops.object.select_all(action='DESELECT')
         bpy.data.objects['spec_toon_shape'].select_set(True)
         bpy.ops.object.delete()
         bpy.ops.object.select_all(action='DESELECT')
         bpy.data.objects['hilite_toon'].select_set(True)
         bpy.ops.object.delete()
         bpy.ops.object.select_all(action='DESELECT')
         bpy.data.objects['mayu_toon2_shape'].select_set(True)
         bpy.ops.object.delete()
         bpy.ops.object.select_all(action='DESELECT')
         bpy.data.objects['hairshadow_toon'].select_set(True)
         bpy.ops.object.delete()
         
        if self.preset_enum == "Sena": 
         bpy.ops.object.select_all(action='DESELECT')
         bpy.data.objects['eye2_subs'].select_set(True)
         bpy.ops.object.delete()
         bpy.ops.object.select_all(action='DESELECT')
         bpy.data.objects['eye_add'].select_set(True)
         bpy.ops.object.delete()
         bpy.ops.object.select_all(action='DESELECT')
         bpy.data.objects['eye_add1'].select_set(True)
         bpy.ops.object.delete()
         bpy.ops.object.select_all(action='DESELECT')
         bpy.data.objects['eye_hi'].select_set(True)
         bpy.ops.object.delete()
         bpy.ops.object.select_all(action='DESELECT')
         bpy.data.objects['eye_shadow_shape'].select_set(True)
         bpy.ops.object.delete()
         bpy.ops.object.select_all(action='DESELECT')
         bpy.data.objects['face_C'].select_set(True)
         bpy.ops.object.delete()
         bpy.ops.object.select_all(action='DESELECT')
         bpy.data.objects['eyepatch_toon'].select_set(True)
         bpy.ops.object.delete()
         bpy.ops.object.select_all(action='DESELECT')
         bpy.data.objects['face_C_alpha1_shape'].select_set(True)
         bpy.ops.object.delete()
         bpy.ops.object.select_all(action='DESELECT')
         bpy.data.objects['hair_shadow2'].select_set(True)
         bpy.ops.object.delete()
         bpy.ops.object.select_all(action='DESELECT')
         bpy.data.objects['hair_shadow3_shape'].select_set(True)
         bpy.ops.object.delete()
         bpy.ops.object.select_all(action='DESELECT')
         bpy.data.objects['matu_alpha_shape'].select_set(True)
         bpy.ops.object.delete()
         bpy.ops.object.select_all(action='DESELECT')
         bpy.data.objects['skin_hi1_shape'].select_set(True)
         bpy.ops.object.delete()
         bpy.ops.object.select_all(action='DESELECT')
         bpy.data.objects['eff_tl_heir_base1'].select_set(True)
         bpy.ops.object.delete()
         bpy.ops.object.select_all(action='DESELECT')
         bpy.data.objects['eff_tl_heir_base2'].select_set(True)
         bpy.ops.object.delete()
         bpy.ops.object.select_all(action='DESELECT')
         bpy.data.objects['eff_op_heir_base1'].select_set(True)
         bpy.ops.object.delete()
         bpy.ops.object.select_all(action='DESELECT')
         bpy.data.objects['hair_shadow2.001'].select_set(True)
         bpy.ops.object.delete()
         bpy.ops.object.select_all(action='DESELECT')
         bpy.data.objects['phong29'].select_set(True)
         bpy.ops.object.delete()
        return {'FINISHED'}    
 
 
 
 
 
class MATERIALFIX_OT_TemplateOperator(bpy.types.Operator):
    bl_label = "Material Fix"
    bl_idname = "wm.materialFix"

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)
    
    
    def draw(self, context):
        layout = self.layout
        layout.prop(self,"preset_enum")
        
    
    def execute(self, context):
        
        for item in bpy.data.materials:
           item.show_backface = True

 
classes = [ADDONNAME_PT_TemplatePanel, ADDONAME_OT_TemplateOperator]
 
 
 
def register():
    for cls in classes:
        bpy.utils.register_class(cls)
 
def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
 
 
 
if __name__ == "__main__":
    register()