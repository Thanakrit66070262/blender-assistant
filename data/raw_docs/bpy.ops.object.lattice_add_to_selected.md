# bpy.ops.object.lattice_add_to_selected

## Signature
```python
bpy.ops.object.lattice_add_to_selected(*, fit_to_selected=True, radius=1.0, margin=0.0, add_modifiers=True, resolution_u=2, resolution_v=2, resolution_w=2, enter_editmode=False, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0))Â
Description
Add a lattice and use it to deform selected objects
Parameters:
fit_to_selected (bool) â Fit to Selected, Resize lattice to fit selected deformable objects (optional)
radius (float) â Radius, (in [0, inf], optional)
margin (float) â Margin, Add margin to lattice dimensions (in [0, inf], optional)
add_modifiers (bool) â Add Modifiers, Automatically add lattice modifiers to selected objects (optional)
resolution_u (int) â Resolution U, Lattice resolution in U direction (in [1, 64], optional)
resolution_v (int) â V, Lattice resolution in V direction (in [1, 64], optional)
resolution_w (int) â W, Lattice resolution in W direction (in [1, 64], optional)
enter_editmode (bool) â Enter Edit Mode, Enter edit mode when adding this object (optional)
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
