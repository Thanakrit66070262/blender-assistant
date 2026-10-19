# bpy.types.ShaderNodeBsdfPrincipled.subsurface_method

## Signature
```python
subsurface_methodÂ
Description
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
