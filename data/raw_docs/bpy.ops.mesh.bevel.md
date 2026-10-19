# bpy.ops.mesh.bevel

## Signature
```python
bpy.ops.mesh.bevel(*, offset_type='OFFSET', offset=0.0, profile_type='SUPERELLIPSE', offset_pct=0.0, segments=1, profile=0.5, affect='EDGES', clamp_overlap=False, loop_slide=True, mark_seam=False, mark_sharp=False, material=-1, harden_normals=False, face_strength_mode='NONE', miter_outer='SHARP', miter_inner='SHARP', spread=0.1, vmesh_method='ADJ', release_confirm=False)Â
Description
Cut into selected items at an angle to create bevel or chamfer
Parameters:
offset_type (Literal['OFFSET', 'WIDTH', 'DEPTH', 'PERCENT', 'ABSOLUTE']) â Width Type, The method for determining the size of the bevel (optional)
OFFSET
Offset â Amount is offset of new edges from original.
WIDTH
Width â Amount is width of new face.
DEPTH
Depth â Amount is perpendicular distance from original edge to bevel face.
PERCENT
Percent â Amount is percent of adjacent edge length.
ABSOLUTE
Absolute â Amount is absolute distance along adjacent edge.
offset (float) â Width, Bevel amount (in [0, 1e+06], optional)
profile_type (Literal['SUPERELLIPSE', 'CUSTOM']) â Profile Type, The type of shape used to rebuild a beveled section (optional)
SUPERELLIPSE
Superellipse â The profile can be a concave or convex curve.
CUSTOM
Custom â The profile can be any arbitrary path between its endpoints.
offset_pct (float) â Width Percent, Bevel amount for percentage method (in [0, 100], optional)
segments (int) â Segments, Segments for curved edge (in [1, 1000], optional)
profile (float) â Profile, Controls profile shape (0.5 = round) (in [0, 1], optional)
affect (Literal['VERTICES', 'EDGES']) â Affect, Affect edges or vertices (optional)
VERTICES
Vertices â Affect only vertices.
EDGES
Edges â Affect only edges.
clamp_overlap (bool) â Clamp Overlap, Do not allow beveled edges/vertices to overlap each other (optional)
loop_slide (bool) â Loop Slide, Prefer sliding along edges to even widths (optional)
mark_seam (bool) â Mark Seams, Preserve seams along beveled edges (optional)
mark_sharp (bool) â Mark Sharp, Preserve sharp edges along beveled edges (optional)
material (int) â Material Index, Material for bevel faces (-1 means use adjacent faces) (in [-1, inf], optional)
harden_normals (bool) â Harden Normals, Match normals of new faces to adjacent faces (optional)
face_strength_mode (Literal['NONE', 'NEW', 'AFFECTED', 'ALL']) â Face Strength Mode, Whether to set face strength, and which faces to set face strength on (optional)
NONE
None â Do not set face strength.
NEW
New â Set face strength on new faces only.
AFFECTED
Affected â Set face strength on new and modified faces only.
ALL
All â Set face strength on all faces.
miter_outer (Literal['SHARP', 'PATCH', 'ARC']) â Outer Miter, Pattern to use for outside of miters (optional)
SHARP
Sharp â Outside of miter is sharp.
PATCH
Patch â Outside of miter is squared-off patch.
ARC
Arc â Outside of miter is arc.
miter_inner (Literal['SHARP', 'ARC']) â Inner Miter, Pattern to use for inside of miters (optional)
SHARP
Sharp â Inside of miter is sharp.
ARC
Arc â Inside of miter is arc.
spread (float) â Spread, Amount to spread arcs for arc inner miters (in [0, 1e+06], optional)
vmesh_method (Literal['ADJ', 'CUTOFF']) â Vertex Mesh Method, The method to use to create meshes at intersections (optional)
ADJ
Grid Fill â Default patterned fill.
CUTOFF
Cutoff â A cutoff at each profileâs end before the intersection.
release_confirm (bool) â Confirm on Release, (optional)
Returns:
Result of the operator call.
Return type:
set[Literal[Operator Return Items]]
