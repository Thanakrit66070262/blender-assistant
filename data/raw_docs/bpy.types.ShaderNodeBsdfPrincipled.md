# bpy.types.ShaderNodeBsdfPrincipled

## Signature
```python
class bpy.types.ShaderNodeBsdfPrincipled(ShaderNode)Â
Description
Physically-based, easy-to-use shader for rendering surface materials, based on the OpenPBR model
distributionÂ
Light scattering distribution on rough surface (default 'GGX')
GGX
GGX.
MULTI_GGX
Multiscatter GGX â GGX with additional correction to account for multiple scattering, preserve energy and prevent unexpected darkening at high roughness.
Type:
Literal[âGGXâ, âMULTI_GGXâ]
subsurface_methodÂ
Method for rendering subsurface scattering (default 'BURLEY')
BURLEY
Christensen-Burley â Approximation to physically based volume scattering.
RANDOM_WALK
Random Walk â Volumetric approximation to physically based volume scattering, using the scattering radius as specified.
RANDOM_WALK_SKIN
Random Walk (Skin) â Volumetric approximation to physically based volume scattering, with scattering radius automatically adjusted to match color textures. Designed for skin shading..
RANDOM_WALK_LEGACY
Random Walk (Legacy) â Volumetric approximation to physically based volume scattering, using the scattering radius as specified.
Type:
Literal[âBURLEYâ, âRANDOM_WALKâ, âRANDOM_WALK_SKINâ, âRANDOM_WALK_LEGACYâ]
classmethod is_registered_node_type()Â
True if a registered node type
Returns:
Result
Return type:
bool
classmethod input_template(index)Â
Input socket template
Parameters:
index (int) â Index, (in [0, inf])
Returns:
result
Return type:
NodeInternalSocketTemplate
classmethod output_template(index)Â
Output socket template
Parameters:
index (int) â Index, (in [0, inf])
Returns:
result
Return type:
NodeInternalSocketTemplate
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
