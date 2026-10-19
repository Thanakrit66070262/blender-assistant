# bpy.ops.object.volume_import

## Signature
```python
bpy.ops.object.volume_import(*, filepath='', directory='', files=None, hide_props_region=True, check_existing=False, filter_blender=False, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_archive=False, filter_btx=False, filter_alembic=False, filter_usd=False, filter_obj=False, filter_volume=True, filter_folder=True, filter_blenlib=False, filemode=9, relative_path=True, display_type='DEFAULT', sort_method='', use_sequence_detection=True, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0))Â
Description
Import OpenVDB volume file
Parameters:
filepath (str) â File Path, Path to file (optional, never None)
directory (str) â Directory, Directory of the file (optional, never None)
files (bpy_prop_collection[OperatorFileListElement] | None) â Files, (optional)
hide_props_region (bool) â Hide Operator Properties, Collapse the region displaying the operator settings (optional)
check_existing (bool) â Check Existing, Check and warn on overwriting existing files (optional)
filter_blender (bool) â Filter .blend files, (optional)
filter_backup (bool) â Filter backup .blend files, (optional)
filter_image (bool) â Filter image files, (optional)
filter_movie (bool) â Filter movie files, (optional)
filter_python (bool) â Filter Python files, (optional)
filter_font (bool) â Filter font files, (optional)
filter_sound (bool) â Filter sound files, (optional)
filter_text (bool) â Filter text files, (optional)
filter_archive (bool) â Filter archive files, (optional)
filter_btx (bool) â Filter btx files, (optional)
filter_alembic (bool) â Filter Alembic files, (optional)
filter_usd (bool) â Filter USD files, (optional)
filter_obj (bool) â Filter OBJ files, (optional)
filter_volume (bool) â Filter OpenVDB volume files, (optional)
filter_folder (bool) â Filter folders, (optional)
filter_blenlib (bool) â Filter Blender IDs, (optional)
filemode (int) â File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file (in [1, 9], optional)
relative_path (bool) â Relative Path, Select the file relative to the blend file (optional)
display_type (Literal['DEFAULT', 'LIST_VERTICAL', 'LIST_HORIZONTAL', 'THUMBNAIL']) â Display Type, (optional)
DEFAULT
Default â Automatically determine display type for files.
LIST_VERTICAL
Short List â Display files as short list.
LIST_HORIZONTAL
Long List â Display files as a detailed list.
THUMBNAIL
Thumbnails â Display files as thumbnails.
sort_method (str) â File sorting mode, (optional)
use_sequence_detection (bool) â Detect Sequences, Automatically detect animated sequences in selected volume files (based on file names) (optional)
align (Literal['WORLD', 'VIEW', 'CURSOR']) â Align, The alignment of the new object (optional)
WORLD
World â Align the new object to the world.
VIEW
View â Align the new object to the view.
CURSOR
3D Cursor â Use the 3D cursor orientation for the new object.
location (mathutils.Vector | Sequence[float]) â Location, Location for the newly added object (array of 3 items, in [-inf, inf], optional)
rotation (mathutils.Euler | Sequence[float]) â Rotation, Rotation for the newly added object (array of 3 items, in [-inf, inf], optional)
scale (mathutils.Vector | Sequence[float]) â Scale, Scale for the newly added object (array of 3 items, in [-inf, inf], optional)
Returns:
Result of the operator call.
Return type:
set[Literal[Operator Return Items]]
