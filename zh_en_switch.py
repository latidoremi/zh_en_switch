bl_info = {
    "name": "zh/en switch",
    "author": "Latidoremi",
    "version": (1, 0),
    "blender": (3, 0, 0),
    "location": "F3 menu/tool header",
    "description": "Switch ui language between zh_CN and en_US",
    "category": "Interface",
}

import bpy

class UI_OT_switch(bpy.types.Operator):
    bl_idname = 'view3d.zh_en_switch'
    bl_label = 'zh/en Switch'
    bl_options = {'UNDO'}
    
    def execute(self, context):
        lan = context.preferences.view.language
        if lan == 'en_US':
            context.preferences.view.language = 'zh_CN'
        else:
            context.preferences.view.language = 'en_US'
        
        return {'FINISHED'}


def draw_switch(self,context):
    self.layout.operator('view3d.zh_en_switch', text='zh/en')
    
def register():
    bpy.utils.register_class(UI_OT_switch)
    bpy.types.VIEW3D_HT_tool_header.append(draw_switch)

def unregister():
    bpy.utils.unregister_class(UI_OT_switch)
    bpy.types.VIEW3D_HT_tool_header.remove(draw_switch)

#if __name__ == '__main__':
#    register()
#    unregister()
