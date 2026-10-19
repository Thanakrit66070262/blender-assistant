# bpy.ops.object.empty_image_add

## Signature
```python
bpy.ops.object.empty_image_add(*, filepath='', hide_props_region=True, check_existing=False, filter_blender=False, filter_backup=False, filter_image=True, filter_movie=True, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_archive=False, filter_btx=False, filter_alembic=False, filter_usd=False, filter_obj=False, filter_volume=False, filter_folder=True, filter_blenlib=False, filemode=9, relative_path=True, show_multiview=False, use_multiview=False, display_type='DEFAULT', sort_method='', name='', session_uid=0, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0), background=False)Â
Description
Add an empty image type to scene with data
Parameters:
filepath (str) â File Path, Path to file (optional, never None)
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
show_multiview (bool) â Enable Multi-View, (optional)
use_multiview (bool) â Use Multi-View, (optional)
display_type (Literal['DEFAULT', 'LIST_VERTICAL', 'LIST_HORIZONTAL', 'THUMBNAIL']) â Display Type, (optional)
DEFAULT
Default â Automatically determine display type for files.
LIST_VERTICAL
Short List â Display files as short list.
LIST_HORIZONTAL
Long List â Display files as a detailed list.
THUMBNAIL
Thumbnails â Display files as thumbnails.
sort_method (Literal['', 'DEFAULT', 'FILE_SORT_ALPHA', 'FILE_SORT_EXTENSION', 'FILE_SORT_TIME', 'FILE_SORT_SIZE', 'ASSET_CATALOG']) â File sorting mode, (optional)
DEFAULT
Default â Automatically determine sort method for files.
FILE_SORT_ALPHA
Name â Sort the file list alphabetically.
FILE_SORT_EXTENSION
Extension â Sort the file list by extension/type.
FILE_SORT_TIME
Modified Date â Sort files by modification time.
FILE_SORT_SIZE
Size â Sort files by size.
ASSET_CATALOG
Asset Catalog â Sort the asset list so that assets in the same catalog are kept together. Within a single catalog, assets are ordered by name. The catalogs are in order of the flattened catalog hierarchy..
name (str) â Name, Name of the data-block to use by the operator (optional, never None)
session_uid (int) â Session UID, Session UID of the data-block to use by the operator (in [-inf, inf], optional)
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
background (bool) â Put in Background, Make the image render behind all objects (optional)
Returns:
Result of the operator call.
Return type:
set[Literal[Operator Return Items]]
