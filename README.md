# Import Anything Addon for Blender

The "Import Anything" addon is a Blender extension that simplifies the process of importing various file formats into Blender. With this addon, you can import FBX, OBJ, glTF (`.gltf` and `.glb`), and .blend files using a single unified interface.

## Features

- Import FBX files using the `bpy.ops.import_scene.fbx` operator
- Import OBJ files using the `bpy.ops.wm.obj_import` operator
- Import glTF files (`.gltf` and `.glb`) using the `bpy.ops.import_scene.gltf` operator
- Append objects from .blend files using the `bpy.ops.wm.append` operator
- Automatically detects the file format based on the file extension
- Provides a convenient "Import Anything" option in the "File > Import" menu

## Installation

1. Download the `import_anything_addon.py` file from this repository.
2. Open Blender and go to "Edit > Preferences".
3. In the "Add-ons" tab, click on the "Install" button.
4. Navigate to the directory where you downloaded the `import_anything_addon.py` file and select it.
5. Click on the "Install Add-on" button to install the addon.
6. Enable the addon by checking the checkbox next to "Import-Export: Import Anything".
7. Save the preferences by clicking on the "Save Preferences" button.

## Usage

1. Go to "File > Import > Import Anything".
2. In the file browser, navigate to the directory containing the file you want to import.
3. Select the file and click on the "Import" button.
4. If you selected a .blend file, the file browser will open again, allowing you to select the objects or data you want to append from the file.
5. The selected file will be imported into your current Blender scene.

## Supported File Formats (will add more later)

- FBX (`.fbx`)
- OBJ (`.obj`)
- glTF (`.gltf` and `.glb`)
- Blender (`.blend`) - Append functionality

## Extending the Addon

You can easily extend the "Import Anything" addon to support additional file formats by adding the corresponding import operators to the `import_file` function in the `import_anything_addon.py` file.

To add support for a new file format:

1. Identify the appropriate import operator for the file format.
2. Add a new condition in the `import_file` function to check for the file extension.
3. Use the corresponding import operator to import the file.

## License

This addon is released under the [MIT License](LICENSE).

## Acknowledgements

The "Import Anything" addon was created using the Blender Python API and is based on the default import operators provided by Blender.

## Contributing

If you encounter any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request on the GitHub repository.
