# bpy.types.Object

## Signature
```python
class bpy.types.Object(ID)Â
Description
Object data-block defining an object in a scene
active_materialÂ
Active material being displayed
Type:
Material | None
active_material_indexÂ
Index of active material slot (in [0, inf], default 0)
Type:
int
active_selection_setÂ
Index of the currently active selection set (in [-inf, inf], default 0)
Type:
int
active_shape_keyÂ
Current shape key (readonly)
Type:
ShapeKey | None
active_shape_key_indexÂ
Current shape key index (in [-32768, 32767], default 0)
Type:
int
add_rest_position_attributeÂ
Add a ârest_positionâ attribute that is a copy of the position attribute before shape keys and modifiers are evaluated (default False)
Type:
bool
animation_dataÂ
Animation data for this data-block (readonly)
Type:
AnimData | None
animation_visualizationÂ
Animation data for this data-block (readonly, never None)
Type:
AnimViz
bound_boxÂ
Objectâs bounding box in object-space coordinates, all values are -1.0 when not available (multi-dimensional array of 8 * 3 items, in [-inf, inf], default ((0.0, 0.0, 0.0), (0.0, 0.0, 0.0), (0.0, 0.0, 0.0), (0.0, 0.0, 0.0), (0.0, 0.0, 0.0), (0.0, 0.0, 0.0), (0.0, 0.0, 0.0), (0.0, 0.0, 0.0)), readonly)
Type:
bpy_prop_array[bpy_prop_array[float]]
collisionÂ
Settings for using the object as a collider in physics simulation (readonly)
Type:
CollisionSettings | None
colorÂ
Object color and alpha, used when the Object Color mode is enabled (array of 4 items, in [0, inf], default (1.0, 1.0, 1.0, 1.0))
Type:
bpy_prop_array[float]
constraintsÂ
Constraints affecting the transformation of the object (default None, readonly)
Type:
ObjectConstraints[Constraint]
cyclesÂ
Cycles object settings (readonly)
Type:
CyclesObjectSettings | None
dataÂ
Object data
Type:
ID | None
delta_locationÂ
Extra translation added to the location of the object (array of 3 items, in [-inf, inf], default (0.0, 0.0, 0.0))
Type:
mathutils.Vector
delta_rotation_eulerÂ
Extra rotation added to the rotation of the object (when using Euler rotations) (array of 3 items, in [-inf, inf], default (0.0, 0.0, 0.0))
Type:
mathutils.Euler
delta_rotation_quaternionÂ
Extra rotation added to the rotation of the object (when using Quaternion rotations) (array of 4 items, in [-inf, inf], default (1.0, 0.0, 0.0, 0.0))
Type:
mathutils.Quaternion
delta_scaleÂ
Extra scaling added to the scale of the object (array of 3 items, in [-inf, inf], default (1.0, 1.0, 1.0))
Type:
mathutils.Vector
dimensionsÂ
Absolute bounding box dimensions of the object.
Warning: Assigning to it or its members multiple consecutive times will not work correctly, as this needs up-to-date evaluated data
(array of 3 items, in [-inf, inf], default (0.0, 0.0, 0.0))
Type:
mathutils.Vector
displayÂ
Object display settings for 3D viewport (readonly, never None)
Type:
ObjectDisplay
display_bounds_typeÂ
Object boundary display type (default 'BOX')
BOX
Box â Display bounds as box.
SPHERE
Sphere â Display bounds as sphere.
CYLINDER
Cylinder â Display bounds as cylinder.
CONE
Cone â Display bounds as cone.
CAPSULE
Capsule â Display bounds as capsule.
Type:
Literal[âBOXâ, âSPHEREâ, âCYLINDERâ, âCONEâ, âCAPSULEâ]
display_typeÂ
How to display object in viewport (default 'TEXTURED')
BOUNDS
Bounds â Display the bounds of the object.
WIRE
Wire â Display the object as a wireframe.
SOLID
Solid â Display the object as a solid (if solid drawing is enabled in the viewport).
TEXTURED
Textured â Display the object with textures (if textures are enabled in the viewport).
Type:
Literal[âBOUNDSâ, âWIREâ, âSOLIDâ, âTEXTUREDâ]
empty_display_sizeÂ
Size of display for empties in the viewport (in [0.0001, 1000], default 1.0)
Type:
float
empty_display_typeÂ
Viewport display style for empties (default 'PLAIN_AXES')
Type:
Literal[Object Empty Drawtype Items]
empty_image_depthÂ
Determine which other objects will occlude the image (default 'DEFAULT')
Type:
Literal[âDEFAULTâ, âFRONTâ, âBACKâ]
empty_image_offsetÂ
Origin offset distance (array of 2 items, in [-inf, inf], default (-0.5, -0.5))
Type:
bpy_prop_array[float]
empty_image_sideÂ
Show front/back side (default 'DOUBLE_SIDED')
Type:
Literal[âDOUBLE_SIDEDâ, âFRONTâ, âBACKâ]
fieldÂ
Settings for using the object as a field in physics simulation (readonly)
Type:
FieldSettings | None
hide_probe_planeÂ
Globally disable in planar light probes (default False)
Type:
bool
hide_probe_sphereÂ
Globally disable in spherical light probes (default False)
Type:
bool
hide_probe_volumeÂ
Globally disable in volume probes (default False)
Type:
bool
hide_renderÂ
Globally disable in renders (default False)
Type:
bool
hide_selectÂ
Disable selection in viewport (default False)
Type:
bool
hide_surface_pickÂ
Disable surface influence during selection, snapping and depth-picking operators. Usually used to avoid semi-transparent objects to affect scene navigation (default False)
Type:
bool
hide_viewportÂ
Globally disable in viewports (default False)
Type:
bool
image_userÂ
Parameters defining which layer, pass and frame of the image is displayed (readonly, never None)
Type:
ImageUser
instance_collectionÂ
Instance an existing collection
Type:
Collection | None
instance_faces_scaleÂ
Scale the face instance objects (in [0.001, 10000], default 1.0)
Type:
float
instance_typeÂ
If not None, object instancing method to use (default 'NONE')
NONE
None.
VERTS
Vertices â Instantiate child objects on all vertices.
FACES
Faces â Instantiate child objects on all faces.
COLLECTION
Collection â Enable collection instancing.
Type:
Literal[âNONEâ, âVERTSâ, âFACESâ, âCOLLECTIONâ]
is_from_instancerÂ
Object comes from a instancer (default False, readonly)
Type:
bool
is_from_setÂ
Object comes from a background set (default False, readonly)
Type:
bool
is_holdoutÂ
Render objects as a holdout or matte, creating a hole in the image with zero alpha, to fill out in compositing with real footage or another render (default False)
Type:
bool
is_instancerÂ
(default False, readonly)
Type:
bool
is_shadow_catcherÂ
Only render shadows and reflections on this object, for compositing renders into real footage. Objects with this setting are considered to already exist in the footage, objects without it are synthetic objects being composited into it. (default False)
Type:
bool
light_linkingÂ
Light linking settings (readonly, never None)
Type:
ObjectLightLinking
lightgroupÂ
Lightgroup that the object belongs to (default ââ, never None)
Type:
str
lineartÂ
Line Art settings for the object (readonly)
Type:
ObjectLineArt | None
locationÂ
Location of the object (array of 3 items, in [-inf, inf], default (0.0, 0.0, 0.0))
Type:
mathutils.Vector
lock_locationÂ
Lock editing of location when transforming (array of 3 items, default (False, False, False))
Type:
bpy_prop_array[bool]
lock_rotationÂ
Lock editing of rotation when transforming (array of 3 items, default (False, False, False))
Type:
bpy_prop_array[bool]
lock_rotation_wÂ
Lock editing of âangleâ component of four-component rotations when transforming (default False)
Type:
bool
lock_rotations_4dÂ
Lock editing of four component rotations by components (instead of as Eulers) (default True)
Type:
bool
lock_scaleÂ
Lock editing of scale when transforming (array of 3 items, default (False, False, False))
Type:
bpy_prop_array[bool]
material_slotsÂ
Material slots in the object (default None, readonly)
Type:
bpy_prop_collection[MaterialSlot]
matrix_basisÂ
Matrix access to location, rotation and scale (including deltas), before constraints and parenting are applied (multi-dimensional array of 4 * 4 items, in [-inf, inf], default ((0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0)))
Type:
mathutils.Matrix
matrix_localÂ
Parent relative transformation matrix.
Warning: Only takes into account object parenting, so e.g. in case of bone parenting you get a matrix relative to the Armature object, not to the actual parent bone
(multi-dimensional array of 4 * 4 items, in [-inf, inf], default ((0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0)))
Type:
mathutils.Matrix
matrix_parent_inverseÂ
Inverse of objectâs parent matrix at time of parenting (multi-dimensional array of 4 * 4 items, in [-inf, inf], default ((1.0, 0.0, 0.0, 0.0), (0.0, 1.0, 0.0, 0.0), (0.0, 0.0, 1.0, 0.0), (0.0, 0.0, 0.0, 1.0)))
Type:
mathutils.Matrix
matrix_worldÂ
Worldspace transformation matrix (multi-dimensional array of 4 * 4 items, in [-inf, inf], default ((0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0)))
Type:
mathutils.Matrix
modeÂ
Object interaction mode (default 'OBJECT', readonly)
Type:
Literal[Object Mode Items]
modifiersÂ
Modifiers affecting the geometric data of the object (default None, readonly)
Type:
ObjectModifiers[Modifier]
motion_pathÂ
Motion Path for this element (readonly)
Type:
MotionPath | None
parentÂ
Parent object
Type:
Object | None
parent_boneÂ
Name of parent bone in case of a bone parenting relation (default ââ, never None)
Type:
str
parent_bone_head_tail_factorÂ
Position along the length of bone (in [0, 1], default 1.0)
Type:
float
parent_typeÂ
Type of parent relation (default 'OBJECT')
OBJECT
Object â The object is parented to an object.
ARMATURE
Armature.
LATTICE
Lattice â The object is parented to a lattice.
VERTEX
Vertex â The object is parented to a vertex.
VERTEX_3
3 Vertices.
BONE
Bone â The object is parented to a bone.
Type:
Literal[âOBJECTâ, âARMATUREâ, âLATTICEâ, âVERTEXâ, âVERTEX_3â, âBONEâ]
parent_verticesÂ
Indices of vertices in case of a vertex parenting relation (array of 3 items, in [0, inf], default (0, 0, 0))
Type:
bpy_prop_array[int]
particle_systemsÂ
Particle systems emitted from the object (default None, readonly)
Type:
ParticleSystems[ParticleSystem]
pass_indexÂ
Index number for the âObject Indexâ render pass (in [0, 32767], default 0)
Type:
int
poseÂ
Current pose for armatures (readonly)
Type:
Pose | None
rigid_bodyÂ
Settings for rigid body simulation (readonly)
Type:
RigidBodyObject | None
rigid_body_constraintÂ
Constraint constraining rigid bodies (readonly)
Type:
RigidBodyConstraint | None
rotation_axis_angleÂ
Angle of Rotation for Axis-Angle rotation representation (array of 4 items, in [-inf, inf], default (0.0, 0.0, 1.0, 0.0))
Type:
bpy_prop_array[float]
rotation_eulerÂ
Rotation in Eulers (array of 3 items, in [-inf, inf], default (0.0, 0.0, 0.0))
Type:
mathutils.Euler
rotation_modeÂ
The kind of rotation to apply, values from other rotation modes are not used (default 'XYZ')
Type:
Literal[Object Rotation Mode Items]
rotation_quaternionÂ
Rotation in Quaternions (array of 4 items, in [-inf, inf], default (1.0, 0.0, 0.0, 0.0))
Type:
mathutils.Quaternion
scaleÂ
Scaling of the object (array of 3 items, in [-inf, inf], default (1.0, 1.0, 1.0))
Type:
mathutils.Vector
selection_setsÂ
List of groups of bones for easy selection (default None, readonly)
Type:
bpy_prop_collection[SelectionSet]
shader_effectsÂ
Effects affecting display of object (default None, readonly)
Type:
ObjectShaderFx[ShaderFx]
shadow_terminator_geometry_offsetÂ
Offset rays from the surface to reduce shadow terminator artifact on low poly geometry. Only affects triangles at grazing angles to light (in [0, inf], default 0.1)
Type:
float
shadow_terminator_normal_offsetÂ
Offset rays from the surface to reduce shadow terminator artifact on low poly geometry. Only affect triangles that are affected by the geometry offset (in [0, inf], default 0.0)
Type:
float
shadow_terminator_shading_offsetÂ
Push the shadow terminator towards the light to hide artifacts on low poly geometry (in [0, inf], default 0.0)
Type:
float
show_all_edgesÂ
Display all edges for mesh objects (default False)
Type:
bool
show_axisÂ
Display the objectâs origin and axes (default False)
Type:
bool
show_boundsÂ
Display the objectâs bounds (default False)
Type:
bool
show_empty_image_only_axis_alignedÂ
Only display the image when it is aligned with the view axis (default False)
Type:
bool
show_empty_image_orthographicÂ
Display image in orthographic mode (default True)
Type:
bool
show_empty_image_perspectiveÂ
Display image in perspective mode (default True)
Type:
bool
show_in_frontÂ
Make the object display in front of others (default False)
Type:
bool
show_instancer_for_renderÂ
Make instancer visible when rendering (default True)
Type:
bool
show_instancer_for_viewportÂ
Make instancer visible in the viewport (default True)
Type:
bool
show_nameÂ
Display the objectâs name (default False)
Type:
bool
show_only_shape_keyÂ
Only show the active shape key at full value (default False)
Type:
bool
show_texture_spaceÂ
Display the objectâs texture space (default False)
Type:
bool
show_transparentÂ
Display material transparency in the object (default False)
Type:
bool
show_wireÂ
Display the objectâs wireframe over solid shading (default False)
Type:
bool
soft_bodyÂ
Settings for soft body simulation (readonly)
Type:
SoftBodySettings | None
track_axisÂ
Axis that points in the âforwardâ direction (applies to Instance Vertices when Align to Vertex Normal is enabled) (default 'POS_X')
Type:
Literal[Object Axis Items]
typeÂ
Type of object (default 'EMPTY', readonly)
Type:
Literal[Object Type Items]
up_axisÂ
Axis that points in the upward direction (applies to Instance Vertices when Align to Vertex Normal is enabled) (default 'Y')
Type:
Literal[âXâ, âYâ, âZâ]
use_camera_lock_parentÂ
View Lock 3D viewport camera transformation affects the objectâs parent instead (default False)
Type:
bool
use_dynamic_topology_sculptingÂ
(default False, readonly)
Type:
bool
use_empty_image_alphaÂ
Use alpha blending instead of alpha test (can produce sorting artifacts) (default False)
Type:
bool
use_grease_pencil_lightsÂ
Lights affect Grease Pencil object (default True)
Type:
bool
use_instance_faces_scaleÂ
Scale instance based on face size (default False)
Type:
bool
use_instance_vertices_rotationÂ
Rotate instance according to vertex normal (default False)
Type:
bool
use_mesh_mirror_xÂ
Enable mesh symmetry in the X axis (default False)
Type:
bool
use_mesh_mirror_yÂ
Enable mesh symmetry in the Y axis (default False)
Type:
bool
use_mesh_mirror_zÂ
Enable mesh symmetry in the Z axis (default False)
Type:
bool
use_parent_final_indicesÂ
Use the final evaluated indices rather than the original mesh indices (default False)
Type:
bool
use_shape_key_edit_modeÂ
Display shape keys in edit mode (for meshes only) (default False)
Type:
bool
use_simulation_cacheÂ
Cache frames during simulation nodes playback (default True)
Type:
bool
vertex_groupsÂ
Vertex groups of the object (default None, readonly)
Type:
VertexGroups[VertexGroup]
visible_cameraÂ
Object visibility to camera rays (default True)
Type:
bool
visible_diffuseÂ
Object visibility to diffuse rays (default True)
Type:
bool
visible_glossyÂ
Object visibility to glossy rays (default True)
Type:
bool
visible_raycastÂ
Object visibility to raycast rays. Implicitly false for Blended materials. (default True)
Type:
bool
visible_shadowÂ
Object visibility to shadow rays (default True)
Type:
bool
visible_transmissionÂ
Object visibility to transmission rays (default True)
Type:
bool
visible_volume_scatterÂ
Object visibility to volume scattering rays (default True)
Type:
bool
childrenÂ
All the children of this object.
Type:
tuple[Object, â¦]
Note
Takes O(len(bpy.data.objects)) time.
(readonly)
children_recursiveÂ
A list of all children from this object.
Type:
list[Object]
Note
Takes O(len(bpy.data.objects)) time.
(readonly)
users_collectionÂ
The collections this object is in.
Type:
tuple[Collection, â¦]
Note
Takes O(len(bpy.data.collections) + len(bpy.data.scenes)) time.
(readonly)
users_sceneÂ
The scenes this object is in.
Type:
tuple[Scene, â¦]
Note
Takes O(len(bpy.data.scenes) * len(bpy.data.objects)) time.
(readonly)
select_get(*, view_layer=None)Â
Test if the object is selected. The selection state is per view layer.
Parameters:
view_layer (ViewLayer | None) â Use this instead of the active view layer (optional)
Returns:
Object selected
Return type:
bool
select_set(state, *, view_layer=None)Â
Select or deselect the object. The selection state is per view layer.
Parameters:
state (bool) â Selection state to define
view_layer (ViewLayer | None) â Use this instead of the active view layer (optional)
hide_get(*, view_layer=None)Â
Test if the object is hidden for viewport editing. This hiding state is per view layer.
Parameters:
view_layer (ViewLayer | None) â Use this instead of the active view layer (optional)
Returns:
Object hidden
Return type:
bool
hide_set(state, *, view_layer=None)Â
Hide the object for viewport editing. This hiding state is per view layer.
Parameters:
state (bool) â Hide state to define
view_layer (ViewLayer | None) â Use this instead of the active view layer (optional)
visible_get(*, view_layer=None, viewport=None)Â
Test if the object is visible in the 3D viewport, taking into account all visibility settings
Parameters:
view_layer (ViewLayer | None) â Use this instead of the active view layer (optional)
viewport (SpaceView3D | None) â Use this instead of the active 3D viewport (optional)
Returns:
Object visible
Return type:
bool
holdout_get(*, view_layer=None)Â
Test if object is masked in the view layer
Parameters:
view_layer (ViewLayer | None) â Use this instead of the active view layer (optional)
Returns:
Object holdout
Return type:
bool
indirect_only_get(*, view_layer=None)Â
Test if object is set to contribute only indirectly (through shadows and reflections) in the view layer
Parameters:
view_layer (ViewLayer | None) â Use this instead of the active view layer (optional)
Returns:
Object indirect only
Return type:
bool
local_view_get(viewport)Â
Get the local view state for this object
Parameters:
viewport (SpaceView3D | None) â Viewport in local view (never None)
Returns:
Object local view state
Return type:
bool
local_view_set(viewport, state)Â
Set the local view state for this object
Parameters:
viewport (SpaceView3D | None) â Viewport in local view (never None)
state (bool) â Local view state to define
visible_in_viewport_get(viewport)Â
Check for local view and local collections for this viewport and object
Parameters:
viewport (SpaceView3D | None) â Viewport in local collections (never None)
Returns:
Object viewport visibility
Return type:
bool
convert_space(*, pose_bone=None, matrix=((0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0)), from_space='WORLD', to_space='WORLD')Â
Convert (transform) the given matrix from one space to another
Parameters:
pose_bone (PoseBone | None) â Bone to use to define spaces (may be None, in which case only the two âWORLDâ and âLOCALâ spaces are usable) (optional)
matrix (mathutils.Matrix | Sequence[Sequence[float]]) â The matrix to transform (multi-dimensional array of 4 * 4 items, in [-inf, inf], optional)
from_space (Literal['WORLD', 'POSE', 'LOCAL_WITH_PARENT', 'LOCAL']) â The space in which âmatrixâ is currently (optional)
WORLD
World Space â The most global space in Blender.
POSE
Pose Space â The pose space of a bone (its armatureâs object space).
LOCAL_WITH_PARENT
Local With Parent â The rest pose local space of a bone (this matrix includes parent transforms).
LOCAL
Local Space â The local space of an object/bone.
to_space (Literal['WORLD', 'POSE', 'LOCAL_WITH_PARENT', 'LOCAL']) â The space to which you want to transform âmatrixâ (optional)
WORLD
World Space â The most global space in Blender.
POSE
Pose Space â The pose space of a bone (its armatureâs object space).
LOCAL_WITH_PARENT
Local With Parent â The rest pose local space of a bone (this matrix includes parent transforms).
LOCAL
Local Space â The local space of an object/bone.
Returns:
The transformed matrix (multi-dimensional array of 4 * 4 items, in [-inf, inf])
Return type:
mathutils.Matrix
calc_matrix_camera(depsgraph, *, x=1, y=1, scale_x=1.0, scale_y=1.0)Â
Generate the camera projection matrix of this object (mostly useful for Camera and Light types)
Parameters:
depsgraph (Depsgraph | None) â Depsgraph to get evaluated data from
x (int) â Width of the render area (in [0, inf], optional)
y (int) â Height of the render area (in [0, inf], optional)
scale_x (float) â Width scaling factor (in [1e-06, inf], optional)
scale_y (float) â Height scaling factor (in [1e-06, inf], optional)
Returns:
The camera projection matrix (multi-dimensional array of 4 * 4 items, in [-inf, inf])
Return type:
mathutils.Matrix
camera_fit_coords(depsgraph, coordinates)Â
Compute the coordinate (and scale for ortho cameras) given object should be to âseeâ all given coordinates
Parameters:
depsgraph (Depsgraph | None) â Depsgraph to get evaluated data from
coordinates (Sequence[float]) â Coordinates to fit in (array of 1 items, in [-inf, inf], never None)
Returns:
co_return, The location to aim to be able to see all given points, mathutils.Vector
scale_return, The ortho scale to aim to be able to see all given points (if relevant), float
Return type:
tuple[mathutils.Vector, float]
crazyspace_eval(depsgraph, scene)Â
Compute orientation mapping between vertices of an original object and object with shape keys and deforming modifiers applied.The evaluation is to be freed with the crazyspace_eval_free function
Parameters:
depsgraph (Depsgraph | None) â Dependency Graph, Evaluated dependency graph
scene (Scene | None) â Scene, Scene of the object
crazyspace_displacement_to_deformed(*, vertex_index=0, displacement=(0.0, 0.0, 0.0))Â
Convert displacement vector from non-deformed object space to deformed object space
Parameters:
vertex_index (int) â vertex_index, (in [-inf, inf], optional)
displacement (mathutils.Vector | Sequence[float]) â displacement, (array of 3 items, in [-inf, inf], optional)
Returns:
displacement_deformed, (array of 3 items, in [-inf, inf])
Return type:
mathutils.Vector
crazyspace_displacement_to_original(*, vertex_index=0, displacement=(0.0, 0.0, 0.0))Â
Free evaluated state of crazyspace
Parameters:
vertex_index (int) â vertex_index, (in [-inf, inf], optional)
displacement (mathutils.Vector | Sequence[float]) â displacement, (array of 3 items, in [-inf, inf], optional)
Returns:
displacement_original, (array of 3 items, in [-inf, inf])
Return type:
mathutils.Vector
crazyspace_eval_clear()Â
crazyspace_eval_clear
to_mesh(*, preserve_all_data_layers=False, depsgraph=None)Â
Create a Mesh data-block from the current state of the object. The object owns the data-block. To force free it use to_mesh_clear(). The result is temporary and cannot be used by objects from the main database.
Parameters:
preserve_all_data_layers (bool) â Preserve all data layers in the mesh, like UV maps and vertex groups. By default Blender only computes the subset of data layers needed for viewport display and rendering, for better performance. (optional)
depsgraph (Depsgraph | None) â Dependency Graph, Evaluated dependency graph which is required when preserve_all_data_layers is true (optional)
Returns:
Mesh created from object
Return type:
Mesh
to_mesh_clear()Â
Clears mesh data-block created by to_mesh()
to_curve(depsgraph, *, apply_modifiers=False)Â
Create a Curve data-block from the current state of the object. This only works for curve and text objects. The object owns the data-block. To force free it, use to_curve_clear(). The result is temporary and cannot be used by objects from the main database.
Parameters:
depsgraph (Depsgraph | None) â Dependency Graph, Evaluated dependency graph
apply_modifiers (bool) â Apply the deform modifiers on the control points of the curve. This is only supported for curve objects. (optional)
Returns:
Curve created from object
Return type:
Curve
to_curve_clear()Â
Clears curve data-block created by to_curve()
find_armature()Â
Find armature influencing this object as a parent or via a modifier
Returns:
Armature object influencing this object or nullptr
Return type:
Object
shape_key_add(*, name='Key', from_mix=True)Â
Add shape key to this object
Parameters:
name (str) â Unique name for the new key-block (optional, never None)
from_mix (bool) â Create new shape from existing mix of shapes (optional)
Returns:
New shape key-block
Return type:
ShapeKey
shape_key_remove(key)Â
Remove a Shape Key from this object
Parameters:
key (ShapeKey | None) â Key-block to be removed (never None)
shape_key_clear()Â
Remove all Shape Keys from this object
shape_keys_selected()Â
Return selected shape keys
Returns:
keyblocks
Return type:
bpy_prop_collection[ShapeKey]
ray_cast(origin, direction, *, distance=1.70141e+38, depsgraph=None)Â
Cast a ray onto evaluated geometry, in object space (using contextâs or provided depsgraph to get evaluated mesh if needed)
Parameters:
origin (mathutils.Vector | Sequence[float]) â Origin of the ray, in object space (array of 3 items, in [-inf, inf])
direction (mathutils.Vector | Sequence[float]) â Direction of the ray, in object space (array of 3 items, in [-inf, inf])
distance (float) â Maximum distance (in [0, inf], optional)
depsgraph (Depsgraph | None) â Depsgraph to use to get evaluated data, when called from original object (only needed if current Contextâs depsgraph is not suitable) (optional)
Returns:
result, Whether the ray successfully hit the geometry, bool
location, The hit location of this ray cast, mathutils.Vector
normal, The face normal at the ray cast hit location, mathutils.Vector
index, The face index, -1 when original data isnât available, int
Return type:
tuple[bool, mathutils.Vector, mathutils.Vector, int]
closest_point_on_mesh(origin, *, distance=1.84467e+19, depsgraph=None)Â
Find the nearest point on evaluated geometry, in object space (using contextâs or provided depsgraph to get evaluated mesh if needed)
Parameters:
origin (mathutils.Vector | Sequence[float]) â Point to find closest geometry from (in object space) (array of 3 items, in [-inf, inf])
distance (float) â Maximum distance (in [0, inf], optional)
depsgraph (Depsgraph | None) â Depsgraph to use to get evaluated data, when called from original object (only needed if current Contextâs depsgraph is not suitable) (optional)
Returns:
result, Whether closest point on geometry was found, bool
location, The location on the object closest to the point, mathutils.Vector
normal, The face normal at the closest point, mathutils.Vector
index, The face index, -1 when original data isnât available, int
Return type:
tuple[bool, mathutils.Vector, mathutils.Vector, int]
is_modified(scene, settings)Â
Determine if this object is modified from the base mesh data
Parameters:
scene (Scene | None) â Scene in which to check the object (never None)
settings (Literal['PREVIEW', 'RENDER']) â Modifier settings to apply
PREVIEW
Preview â Apply modifier preview settings.
RENDER
Render â Apply modifier render settings.
Returns:
Whether the object is modified
Return type:
bool
is_deform_modified(scene, settings)Â
Determine if this object is modified by a deformation from the base mesh data
Parameters:
scene (Scene | None) â Scene in which to check the object (never None)
settings (Literal['PREVIEW', 'RENDER']) â Modifier settings to apply
PREVIEW
Preview â Apply modifier preview settings.
RENDER
Render â Apply modifier render settings.
Returns:
Whether the object is deform-modified
Return type:
bool
update_from_editmode()Â
Load the objects edit-mode data into the object data
Returns:
Success
Return type:
bool
cache_release()Â
Release memory used by caches associated with this object. Intended to be used by render engines only.
evaluated_geometry()Â
Get the evaluated geometry set of this evaluated object. This only works for
objects that contain geometry data like meshes and curves but not e.g. cameras.
Returns:
The evaluated geometry.
Return type:
GeometrySet
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
