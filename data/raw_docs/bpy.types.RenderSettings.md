# bpy.types.RenderSettings

## Signature
```python
class bpy.types.RenderSettings(bpy_struct)Â
Description
Rendering settings for a Scene data-block
anisotropic_filterÂ
Quality of anisotropic filtering in materials (default 'FILTER_2')
FILTER_0
Off â Turn off anisotropic filtering.
FILTER_2
2Ã â Use 2 samples for anisotropic filtering.
FILTER_4
4Ã â Use 4 samples for anisotropic filtering.
FILTER_8
8Ã â Use 8 samples for anisotropic filtering.
FILTER_16
16Ã â Use 16 samples for anisotropic filtering.
Type:
Literal[âFILTER_0â, âFILTER_2â, âFILTER_4â, âFILTER_8â, âFILTER_16â]
bakeÂ
(readonly, never None)
Type:
BakeSettings
border_max_xÂ
Maximum X value for the render region (in [0, 1], default 1.0)
Type:
float
border_max_yÂ
Maximum Y value for the render region (in [0, 1], default 1.0)
Type:
float
border_min_xÂ
Minimum X value for the render region (in [0, 1], default 0.0)
Type:
float
border_min_yÂ
Minimum Y value for the render region (in [0, 1], default 0.0)
Type:
float
compositor_denoise_deviceÂ
The device to use to process the denoise nodes in the compositor (default 'AUTO')
AUTO
Auto â Use the same device used by the compositor to process the denoise node.
CPU
CPU â Use the CPU to process the denoise node.
GPU
GPU â Use the GPU to process the denoise node if available, otherwise fallback to CPU.
Type:
Literal[âAUTOâ, âCPUâ, âGPUâ]
compositor_denoise_final_qualityÂ
The quality used by denoise nodes during the compositing of final renders if the nodesâ quality option is set to Follow Scene (default 'HIGH')
HIGH
High â High quality.
BALANCED
Balanced â Balanced between performance and quality.
FAST
Fast â High performance.
Type:
Literal[âHIGHâ, âBALANCEDâ, âFASTâ]
compositor_denoise_preview_qualityÂ
The quality used by denoise nodes during viewport and interactive compositing if the nodesâ quality option is set to Follow Scene (default 'BALANCED')
HIGH
High â High quality.
BALANCED
Balanced â Balanced between performance and quality.
FAST
Fast â High performance.
Type:
Literal[âHIGHâ, âBALANCEDâ, âFASTâ]
compositor_deviceÂ
Set how compositing is executed (default 'GPU')
Type:
Literal[âCPUâ, âGPUâ]
compositor_precisionÂ
The precision of compositor intermediate result (default 'AUTO')
AUTO
Auto â Full precision for final renders, half precision otherwise.
FULL
Full â Full precision.
Type:
Literal[âAUTOâ, âFULLâ]
dither_intensityÂ
Amount of dithering noise added to the rendered image to break up banding (in [0, inf], default 1.0)
Type:
float
engineÂ
Engine to use for rendering (default 'BLENDER_EEVEE')
Type:
Literal[âBLENDER_EEVEEâ]
ffmpegÂ
FFmpeg related settings for the scene (readonly)
Type:
FFmpegSettings | None
file_extensionÂ
The file extension used for saving renders (default ââ, readonly, never None)
Type:
str
filepathÂ
Directory/name to save animations, # characters define the position and padding of frame numbers (default â//â, never None, blend relative // prefix supported, Supports template expressions)
Type:
str
film_transparentÂ
World background is transparent, for compositing the render over another background (default False)
Type:
bool
filter_sizeÂ
Width over which the reconstruction filter combines samples (in [0, 500], default 1.5)
Type:
float
fpsÂ
Framerate, expressed in frames per second (in [1, 32767], default 24)
Type:
int
fps_baseÂ
Framerate base (in [1e-05, 1e+06], default 1.0)
Type:
float
frame_map_newÂ
How many frames the Map Old will last (in [1, 900], default 100)
Type:
int
frame_map_oldÂ
Old mapping value in frames (in [1, 900], default 100)
Type:
int
hair_subdivÂ
Additional subdivision along the curves (in [0, 3], default 0)
Type:
int
hair_typeÂ
Curves shape type (default 'STRAND')
Type:
Literal[âSTRANDâ, âSTRIPâ, âCYLINDERâ]
has_multiple_enginesÂ
More than one rendering engine is available (default False, readonly)
Type:
bool
image_settingsÂ
(readonly, never None)
Type:
ImageFormatSettings
is_movie_formatÂ
When true the format is a movie (default False, readonly)
Type:
bool
line_thicknessÂ
Line thickness in pixels (in [0, 10000], default 1.0)
Type:
float
line_thickness_modeÂ
Line thickness mode for Freestyle line drawing (default 'ABSOLUTE')
ABSOLUTE
Absolute â Specify unit line thickness in pixels.
RELATIVE
Relative â Unit line thickness is scaled by the proportion of the present vertical image resolution to 480 pixels.
Type:
Literal[âABSOLUTEâ, âRELATIVEâ]
metadata_inputÂ
Where to take the metadata from (default 'SCENE')
SCENE
Scene â Use metadata from the current scene.
STRIPS
Sequencer Strips â Use metadata from the strips in the sequencer.
Type:
Literal[âSCENEâ, âSTRIPSâ]
motion_blur_positionÂ
Offset for the shutterâs time interval, allows to change the motion blur trails (default 'CENTER')
START
Start on Frame â The shutter opens at the current frame.
CENTER
Center on Frame â The shutter is open during the current frame.
END
End on Frame â The shutter closes at the current frame.
Type:
Literal[âSTARTâ, âCENTERâ, âENDâ]
motion_blur_shutterÂ
Time taken in frames between shutter open and close (in [0, inf], default 0.5)
Type:
float
motion_blur_shutter_curveÂ
Curve defining the shutterâs openness over time (readonly)
Type:
CurveMapping | None
pixel_aspect_xÂ
Horizontal aspect ratio - for anamorphic or non-square pixel output (in [1, 200], default 1.0)
Type:
float
pixel_aspect_yÂ
Vertical aspect ratio - for anamorphic or non-square pixel output (in [1, 200], default 1.0)
Type:
float
ppm_baseÂ
The base unit for pixels per meter. (in [1e-05, 1e+06], default 0.0254)
Type:
float
ppm_factorÂ
The pixel density meta-data written to supported image formats. This value is multiplied by the PPM-base which defines the unit (typically inches or meters) (in [1e-05, 1e+06], default 72.0)
Type:
float
preview_pixel_sizeÂ
Pixel size for viewport rendering (default 'AUTO')
AUTO
Automatic â Automatic pixel size, depends on the user interface scale.
1
1Ã â Render at full resolution.
2
2Ã â Render at 50% resolution.
4
4Ã â Render at 25% resolution.
8
8Ã â Render at 12.5% resolution.
Type:
Literal[âAUTOâ, â1â, â2â, â4â, â8â]
resolution_percentageÂ
Percentage scale for render resolution (in [1, 32767], default 100)
Type:
int
resolution_xÂ
Number of horizontal pixels in the rendered image (in [4, 65536], default 1920)
Type:
int
resolution_yÂ
Number of vertical pixels in the rendered image (in [4, 65536], default 1080)
Type:
int
save_outputÂ
Write frames to disk for animation renders (default True)
Type:
bool
sequencer_gl_previewÂ
Display method used in the sequencer view (default 'SOLID')
Type:
Literal[Shading Type Items]
simplify_child_particlesÂ
Global child particles percentage (in [0, 1], default 1.0)
Type:
float
simplify_child_particles_renderÂ
Global child particles percentage during rendering (in [0, 1], default 0.0)
Type:
float
simplify_gpencilÂ
Simplify Grease Pencil drawing (default False)
Type:
bool
simplify_gpencil_antialiasingÂ
Use Antialiasing to smooth stroke edges (default True)
Type:
bool
simplify_gpencil_modifierÂ
Display modifiers (default True)
Type:
bool
simplify_gpencil_onplayÂ
Simplify Grease Pencil only during animation playback (default False)
Type:
bool
simplify_gpencil_shader_fxÂ
Display Shader Effects (default True)
Type:
bool
simplify_gpencil_tintÂ
Display layer tint (default True)
Type:
bool
simplify_gpencil_view_fillÂ
Display fill strokes in the viewport (default True)
Type:
bool
simplify_subdivisionÂ
Global maximum subdivision level (in [0, 32767], default 6)
Type:
int
simplify_subdivision_renderÂ
Global maximum subdivision level during rendering (in [0, 32767], default 0)
Type:
int
simplify_volumesÂ
Resolution percentage of volume objects in viewport (in [0, 1], default 1.0)
Type:
float
stamp_backgroundÂ
Color to use behind stamp text (array of 4 items, in [0, 1], default (0.0, 0.0, 0.0, 0.25))
Type:
bpy_prop_array[float]
stamp_font_sizeÂ
Size of the font used when rendering stamp text (in [8, 64], default 12)
Type:
int
stamp_foregroundÂ
Color to use for stamp text (array of 4 items, in [0, 1], default (0.8, 0.8, 0.8, 1.0))
Type:
bpy_prop_array[float]
stamp_note_textÂ
Custom text to appear in the stamp note (default ââ, never None)
Type:
str
stereo_viewsÂ
(default None, readonly)
Type:
bpy_prop_collection[SceneRenderView]
threadsÂ
Maximum number of CPU cores to use simultaneously while rendering (for multi-core/CPU systems) (in [1, 1024], default 1)
Type:
int
threads_modeÂ
Determine the amount of render threads used (default 'AUTO')
AUTO
Auto-Detect â Automatically determine the number of threads, based on CPUs.
FIXED
Fixed â Manually determine the number of threads.
Type:
Literal[âAUTOâ, âFIXEDâ]
use_auto_generate_texture_cacheÂ
Automatically create tx files from image files when rendering, if the files do not exist or are outdated. The path to store the texture cache files is configured in the preferences (default False)
Type:
bool
use_borderÂ
Render a user-defined render region, within the frame size (default False)
Type:
bool
use_compositingÂ
Process the render result through the compositing pipeline, if a compositing node group is assigned to the scene (default True)
Type:
bool
use_crop_to_borderÂ
Crop the rendered frame to the defined render region size (default False)
Type:
bool
use_file_extensionÂ
Add the file format extensions to the rendered file name (eg: filename + .jpg) (default True)
Type:
bool
use_freestyleÂ
Draw stylized strokes using Freestyle (default False)
Type:
bool
use_high_quality_normalsÂ
Use high quality tangent space at the cost of lower performance (default False)
Type:
bool
use_lock_interfaceÂ
Lock interface during rendering in favor of giving more memory to the renderer (default False)
Type:
bool
use_motion_blurÂ
Use multi-sampled 3D scene motion blur (default False)
Type:
bool
use_multiviewÂ
Use multiple views in the scene (default False)
Type:
bool
use_overwriteÂ
Overwrite existing files while rendering (default True)
Type:
bool
use_persistent_dataÂ
Keep render data around for faster re-renders and animation renders, at the cost of increased memory usage (default False)
Type:
bool
use_placeholderÂ
Create empty placeholder files while rendering frames (similar to Unix âtouchâ) (default False)
Type:
bool
use_render_cacheÂ
Save render cache to EXR files (useful for heavy compositing, Note: affects indirectly rendered scenes) (default False)
Type:
bool
use_sequencerÂ
Process the render (and composited) result through the video sequence editor pipeline, if sequencer strips exist (default True)
Type:
bool
use_sequencer_override_scene_stripÂ
Use Workbench render and world settings from the sequencer scene, instead of each stripâs scene (default False)
Type:
bool
use_simplifyÂ
Enable simplification of scene for quicker preview renders (default False)
Type:
bool
use_simplify_normalsÂ
Skip computing custom normals and face corner normals for displaying meshes in the viewport (default False)
Type:
bool
use_single_layerÂ
Only render the active layer. Only affects rendering from the interface, ignored for rendering from command line. (default False)
Type:
bool
use_spherical_stereoÂ
Active render engine supports spherical stereo rendering (default False, readonly)
Type:
bool
use_stampÂ
Render the stamp info text in the rendered image (default False)
Type:
bool
use_stamp_cameraÂ
Include the name of the active camera in image metadata (default True)
Type:
bool
use_stamp_dateÂ
Include the current date in image/video metadata (default True)
Type:
bool
use_stamp_filenameÂ
Include the .blend filename in image/video metadata (default True)
Type:
bool
use_stamp_frameÂ
Include the frame number in image metadata (default True)
Type:
bool
use_stamp_frame_rangeÂ
Include the rendered frame range in image/video metadata (default False)
Type:
bool
use_stamp_hostnameÂ
Include the hostname of the machine that rendered the frame (default False)
Type:
bool
use_stamp_labelsÂ
Display stamp labels (âCameraâ in front of camera name, etc.) (default True)
Type:
bool
use_stamp_lensÂ
Include the active cameraâs lens in image metadata (default False)
Type:
bool
use_stamp_markerÂ
Include the name of the last marker in image metadata (default False)
Type:
bool
use_stamp_memoryÂ
Include the peak memory usage in image metadata (default True)
Type:
bool
use_stamp_noteÂ
Include a custom note in image/video metadata (default False)
Type:
bool
use_stamp_render_timeÂ
Include the render time in image metadata (default True)
Type:
bool
use_stamp_sceneÂ
Include the name of the active scene in image/video metadata (default True)
Type:
bool
use_stamp_sequencer_stripÂ
Include the name of the foreground sequence strip in image metadata (default False)
Type:
bool
use_stamp_timeÂ
Include the rendered frame timecode as HH:MM:SS.FF in image metadata (default True)
Type:
bool
use_texture_cacheÂ
Load texture tiles at appropriate resolution on demand to reduce memory usage. This avoids loading all textures into memory, at the cost of extra disk space and some performance (default True)
Type:
bool
viewsÂ
(default None, readonly)
Type:
RenderViews[SceneRenderView]
views_formatÂ
(default 'STEREO_3D')
STEREO_3D
Stereo 3D â Single stereo camera system, adjust the stereo settings in the camera panel.
MULTIVIEW
Multi-View â Multi camera system, adjust the cameras individually.
Type:
Literal[âSTEREO_3Dâ, âMULTIVIEWâ]
frame_path(*, frame=-2147483648, preview=False, view='')Â
Return the absolute path to the filename to be written for a given frame
Parameters:
frame (int) â Frame number to use, if unset the current frame will be used (in [-inf, inf], optional)
preview (bool) â Preview, Use preview range (optional)
view (str) â View, The name of the view to use to replace the â%â chars (optional, never None)
Returns:
File Path, The resulting filepath from the scenes render settings (never None)
Return type:
str
classmethod bl_rna_get_subclass(id, default=None, /)Â
Parameters:
id (str) â The RNA type identifier.
default (bpy.types.Struct | None) â The value to return when not found.
Returns:
The RNA type or default when not found.
Return type:
bpy.types.Struct
classmethod bl_rna_get_subclass_py(id, default=None, /)Â
Parameters:
id (str) â The RNA type identifier.
default (type | None) â The value to return when not found.
Returns:
The class or default when not found.
Return type:
type
