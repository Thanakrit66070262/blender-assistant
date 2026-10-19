# bpy.ops.object.quadriflow_remesh

## Signature
```python
bpy.ops.object.quadriflow_remesh(*, use_mesh_symmetry=True, use_preserve_sharp=False, use_preserve_boundary=False, preserve_attributes=False, smooth_normals=False, mode='FACES', target_ratio=1.0, target_edge_length=0.1, target_faces=4000, mesh_area=-1.0, seed=0)Â
Description
Create a new quad based mesh using the surface data of the current mesh. All data layers will be lost
Parameters:
use_mesh_symmetry (bool) â Use Mesh Symmetry, Generates a symmetrical mesh using the mesh symmetry configuration (optional)
use_preserve_sharp (bool) â Preserve Sharp, Try to preserve sharp features on the mesh (optional)
use_preserve_boundary (bool) â Preserve Mesh Boundary, Try to preserve mesh boundary on the mesh (optional)
preserve_attributes (bool) â Preserve Attributes, Reproject attributes onto the new mesh (optional)
smooth_normals (bool) â Smooth Normals, Set the output mesh normals to smooth (optional)
mode (Literal['RATIO', 'EDGE', 'FACES']) â Mode, How to specify the amount of detail for the new mesh (optional)
RATIO
Ratio â Specify target number of faces relative to the current mesh.
EDGE
Edge Length â Input target edge length in the new mesh.
FACES
Faces â Input target number of faces in the new mesh.
target_ratio (float) â Ratio, Relative number of faces compared to the current mesh (in [0, inf], optional)
target_edge_length (float) â Edge Length, Target edge length in the new mesh (in [1e-07, inf], optional)
target_faces (int) â Number of Faces, Approximate number of faces (quads) in the new mesh (in [1, inf], optional)
mesh_area (float) â Old Object Face Area, This property is only used to cache the object area for later calculations (in [-inf, inf], optional)
seed (int) â Seed, Random seed to use with the solver. Different seeds will cause the remesher to come up with different quad layouts on the mesh (in [0, inf], optional)
Returns:
Result of the operator call.
Return type:
set[Literal[Operator Return Items]]
