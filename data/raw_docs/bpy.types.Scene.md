# bpy.types.Scene

## Signature
```python
class bpy.types.Scene(ID)Â
Description
Scene data-block, consisting in objects and defining time and render related settings
active_clipÂ
Active Movie Clip that can be used by motion tracking constraints or as a cameraâs background image
Type:
MovieClip | None
allow_prerollÂ
Allows playing back frames before the playback start frame (default False)
Type:
bool
animation_dataÂ
Animation data for this data-block (readonly)
Type:
AnimData | None
annotationÂ
Data-block used for annotations in the 3D view
Type:
Annotation | None
audio_distance_modelÂ
Distance model for distance attenuation calculation (default 'INVERSE_CLAMPED')
NONE
None â No distance attenuation.
INVERSE
Inverse â Inverse distance model.
INVERSE_CLAMPED
Inverse Clamped â Inverse distance model with clamping.
LINEAR
Linear â Linear distance model.
LINEAR_CLAMPED
Linear Clamped â Linear distance model with clamping.
EXPONENT
Exponential â Exponential distance model.
EXPONENT_CLAMPED
Exponential Clamped â Exponential distance model with clamping.
Type:
Literal[âNONEâ, âINVERSEâ, âINVERSE_CLAMPEDâ, âLINEARâ, âLINEAR_CLAMPEDâ, âEXPONENTâ, âEXPONENT_CLAMPEDâ]
audio_doppler_factorÂ
Pitch factor for Doppler effect calculation (in [0, inf], default 1.0)
Type:
float
audio_doppler_speedÂ
Speed of sound for Doppler effect calculation (in [0.01, inf], default 343.3)
Type:
float
audio_volumeÂ
Audio volume (in [0, 100], default 1.0)
Type:
float
background_setÂ
Background set scene
Type:
Scene | None
cameraÂ
Active camera, used for rendering the scene
Type:
Object | None
collectionÂ
Scene root collection that owns all the objects and other collections instantiated in the scene (readonly, never None)
Type:
Collection
compositing_node_groupÂ
Compositor Nodes
Type:
NodeTree | None
cursorÂ
(readonly, never None)
Type:
View3DCursor
cyclesÂ
Cycles render settings (readonly)
Type:
CyclesRenderSettings | None
cycles_curvesÂ
Cycles curves rendering settings (readonly)
Type:
CyclesCurveRenderSettings | None
displayÂ
Scene display settings for 3D viewport (readonly)
Type:
SceneDisplay | None
display_settingsÂ
Settings of device saved image would be displayed on (readonly)
Type:
ColorManagedDisplaySettings | None
eeveeÂ
EEVEE settings for the scene (readonly)
Type:
SceneEEVEE | None
frame_currentÂ
Current frame, to update animation data from Python frame_set() instead (in [-1048574, 1048574], default 1)
Type:
int
frame_current_finalÂ
Current frame with subframe and time remapping applied (in [-1.04857e+06, 1.04857e+06], default 0.0, readonly)
Type:
float
frame_endÂ
Final frame of the playback/rendering range (in [0, 1048574], default 250)
Type:
int
frame_floatÂ
(in [-1.04857e+06, 1.04857e+06], default 0.0)
Type:
float
frame_preview_endÂ
Alternative end frame for UI playback (in [-inf, inf], default 0)
Type:
int
frame_preview_startÂ
Alternative start frame for UI playback (in [-inf, inf], default 0)
Type:
int
frame_startÂ
First frame of the playback/rendering range (in [0, 1048574], default 1)
Type:
int
frame_stepÂ
Number of frames to skip forward while rendering/playing back each frame (in [0, 1048574], default 1)
Type:
int
frame_subframeÂ
(in [0, 1], default 0.0)
Type:
float
gravityÂ
Constant acceleration in a given direction (array of 3 items, in [-inf, inf], default (0.0, 0.0, -9.81))
Type:
mathutils.Vector
grease_pencil_settingsÂ
Grease Pencil settings for the scene (readonly)
Type:
SceneGpencil | None
hydraÂ
Hydra settings for the scene (readonly)
Type:
SceneHydra | None
is_nla_tweakmodeÂ
Whether there is any action referenced by NLA being edited (strictly read-only) (default False, readonly)
Type:
bool
keying_setsÂ
Absolute Keying Sets for this Scene (default None, readonly)
Type:
KeyingSets[KeyingSet]
keying_sets_allÂ
All Keying Sets available for use (Builtins and Absolute Keying Sets for this Scene) (default None, readonly)
Type:
KeyingSetsAll[KeyingSet]
lock_frame_selection_to_rangeÂ
Donât allow frame to be selected with mouse outside of frame range (default False)
Type:
bool
objectsÂ
(default None, readonly)
Type:
SceneObjects[Object]
playback_loop_modeÂ
What to do when playback reaches the last frame (default 'INFINITE')
INFINITE
Infinite â After the last frame, jump back to the first and keep playing, infinitely.
STOP_END_FRAME
Stop at End Frame â Stop playback at the last frame, without looping.
STOP_START_FRAME
Stop at Start Frame â After the last frame, jump back to the first and stop playback.
RESTORE
Restore Frame â After the last frame, stop at the frame the playback started from.
BOUNCE
Bounce â At the last frame, reverse playback.
Type:
Literal[âINFINITEâ, âSTOP_END_FRAMEâ, âSTOP_START_FRAMEâ, âRESTOREâ, âBOUNCEâ]
renderÂ
(readonly, never None)
Type:
RenderSettings
rigidbody_worldÂ
(readonly)
Type:
RigidBodyWorld | None
safe_areasÂ
(readonly, never None)
Type:
DisplaySafeAreas
sequence_editorÂ
(readonly)
Type:
SequenceEditor | None
sequencer_colorspace_settingsÂ
Settings of color space sequencer is working in (readonly)
Type:
ColorManagedSequencerColorspaceSettings | None
show_keys_from_selected_onlyÂ
Only include channels relating to selected objects and data (default True)
Type:
bool
show_subframeÂ
Display and allow setting fractional frame values for the current frame (default False)
Type:
bool
simulation_frame_endÂ
Frame at which simulations end (in [-inf, inf], default 250)
Type:
int
simulation_frame_startÂ
Frame at which simulations start (in [-inf, inf], default 1)
Type:
int
sync_modeÂ
How to sync playback (default 'AUDIO_SYNC')
NONE
Play Every Frame â Do not sync, play every frame.
FRAME_DROP
Frame Dropping â Drop frames if playback is too slow.
AUDIO_SYNC
Sync to Audio â Sync to audio playback, dropping frames.
Type:
Literal[âNONEâ, âFRAME_DROPâ, âAUDIO_SYNCâ]
time_jump_deltaÂ
Number of frames or seconds to jump forward or backward (in [0.1, inf], default 1.0)
Type:
float
time_jump_unitÂ
Which unit to use for time jumps in the timeline (default 'SECOND')
FRAME
Frame â Jump by frames.
SECOND
Second â Jump by seconds.
Type:
Literal[âFRAMEâ, âSECONDâ]
timeline_markersÂ
Markers used in all timelines for the current scene (default None, readonly)
Type:
TimelineMarkers[TimelineMarker]
tool_settingsÂ
(readonly, never None)
Type:
ToolSettings
transform_orientation_slotsÂ
(default None, readonly)
Type:
bpy_prop_collection[TransformOrientationSlot]
unit_settingsÂ
Unit editing settings (readonly, never None)
Type:
UnitSettings
use_audioÂ
Play back of audio from Sequence Editor, otherwise mute audio (default False)
Type:
bool
use_audio_scrubÂ
Play audio from Sequence Editor while scrubbing (default False)
Type:
bool
use_custom_simulation_rangeÂ
Use a simulation range that is different from the scene range for simulation nodes that donât override the frame range themselves (default False)
Type:
bool
use_gravityÂ
Use global gravity for all dynamics (default True)
Type:
bool
use_nodesÂ
Enable the compositing node group. (default False)
Deprecated since version 5.0: removal planned in version 6.0
Unused but kept for compatibility reasons. Setting the property has no effect, and getting it always returns True. Use #scene.render.use_compositing to turn compositing to enable or disable compositing.
Type:
bool
use_preview_rangeÂ
Use an alternative start/end frame range for animation playback and view renders (default False)
Type:
bool
use_stamp_noteÂ
User defined note for the render stamping (default ââ, never None)
Type:
str
view_layersÂ
(default None, readonly)
Type:
ViewLayers[ViewLayer]
view_settingsÂ
Color management settings applied on image before saving (readonly)
Type:
ColorManagedViewSettings | None
worldÂ
World used for rendering the scene
Type:
World | None
classmethod update_render_engine()Â
Trigger a render engine update
statistics(view_layer)Â
statistics
Parameters:
view_layer (ViewLayer | None) â View Layer, (never None)
Returns:
Statistics, (never None)
Return type:
str
frame_set(frame, *, subframe=0.0)Â
Set scene frame updating all objects and view layers immediately
Parameters:
frame (int) â Frame number to set (in [-1048574, 1048574])
subframe (float) â Subframe time, between 0.0 and 1.0 (in [0, 1], optional)
uvedit_aspect(object)Â
Get uv aspect for current object
Parameters:
object (Object | None) â Object (never None)
Returns:
aspect (array of 2 items, in [0, inf])
Return type:
mathutils.Vector
ray_cast(depsgraph, origin, direction, *, distance=1.70141e+38)Â
Cast a ray onto evaluated geometry in world-space
Parameters:
depsgraph (Depsgraph | None) â The current dependency graph (never None)
origin (mathutils.Vector | Sequence[float]) â (array of 3 items, in [-inf, inf])
direction (mathutils.Vector | Sequence[float]) â (array of 3 items, in [-inf, inf])
distance (float) â Maximum distance (in [0, inf], optional)
Returns:
result, bool
location, The hit location of this ray cast, mathutils.Vector
normal, The face normal at the ray cast hit location, mathutils.Vector
index, The face index, -1 when original data isnât available, int
object, The original (un-evaluated) object that was hit. Note that location, normal, and index correspond to the evaluated objectâs mesh., Object
matrix, Matrix, mathutils.Matrix
Return type:
tuple[bool, mathutils.Vector, mathutils.Vector, int, Object, mathutils.Matrix]
sequence_editor_create()Â
Ensure sequence editor is valid in this scene
Returns:
New sequence editor data or None
Return type:
SequenceEditor
sequence_editor_clear()Â
Clear sequence editor in this scene
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
