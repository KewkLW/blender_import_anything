import bpy
import os

bl_info = {
    "name": "Import Anything",
    "author": "Kewk @kewkd",
    "version": (1, 0),
    "blender": (4, 0, 0),
    "location": "File > Import > Import Anything",
    "description": "Import any supported file format using the correct importer",
    "warning": "",
    "doc_url": "",
    "category": "Import-Export",
}

def import_file(file_path):
    file_extension = os.path.splitext(file_path)[-1].lower()
    
    if file_extension == ".fbx":
        bpy.ops.import_scene.fbx(filepath=file_path)
    elif file_extension == ".obj":
        bpy.ops.wm.obj_import(filepath=file_path)
    elif file_extension == ".gltf" or file_extension == ".glb":
        bpy.ops.import_scene.gltf(filepath=file_path)
    elif file_extension == ".blend":
        # Open the file browser for object selection
        bpy.ops.wm.append('INVOKE_DEFAULT', filepath=file_path)
    # Add more file extensions and their corresponding import operators
    else:
        print(f"Unsupported file format: {file_extension}")

class ImportAnything(bpy.types.Operator):
    bl_idname = "import_scene.import_anything"
    bl_label = "Import Anything"
    bl_options = {'REGISTER', 'UNDO'}

    filepath: bpy.props.StringProperty(subtype="FILE_PATH")

    def execute(self, context):
        import_file(self.filepath)
        return {'FINISHED'}

    def invoke(self, context, event):
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}

def menu_func_import(self, context):
    self.layout.operator(ImportAnything.bl_idname, text="Import Anything")

def register():
    bpy.utils.register_class(ImportAnything)
    bpy.types.TOPBAR_MT_file_import.append(menu_func_import)

def unregister():
    bpy.utils.unregister_class(ImportAnything)
    bpy.types.TOPBAR_MT_file_import.remove(menu_func_import)

if __name__ == "__main__":
    register()
