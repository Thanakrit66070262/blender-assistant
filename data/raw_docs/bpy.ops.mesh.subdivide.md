# bpy.ops.mesh.subdivide

## Signature
```python
bpy.ops.mesh.subdivide(*, number_cuts=1, smoothness=0.0, ngon=True, quadcorner='STRAIGHT_CUT', fractal=0.0, fractal_along_normal=0.0, seed=0)Â
Description
Subdivide selected edges
Parameters:
number_cuts (int) â Number of Cuts, (in [1, 100], optional)
smoothness (float) â Smoothness, Smoothness factor (in [0, 1000], optional)
ngon (bool) â Create N-Gons, When disabled, newly created faces are limited to 3 and 4 sided faces (optional)
quadcorner (Literal['INNERVERT', 'PATH', 'STRAIGHT_CUT', 'FAN']) â Quad Corner Type, How to subdivide quad corners (anything other than Straight Cut will prevent n-gons) (optional)
fractal (float) â Fractal, Fractal randomness factor (in [0, 1e+06], optional)
fractal_along_normal (float) â Along Normal, Apply fractal displacement along normal only (in [0, 1], optional)
seed (int) â Random Seed, Seed for the random number generator (in [0, inf], optional)
Returns:
Result of the operator call.
Return type:
set[Literal[Operator Return Items]]
