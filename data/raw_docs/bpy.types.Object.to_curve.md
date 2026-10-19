# bpy.types.Object.to_curve

## Signature
```python
to_curve(depsgraph, *, apply_modifiers=False)Â
Description
Create a Curve data-block from the current state of the object. This only works for curve and text objects. The object owns the data-block. To force free it, use to_curve_clear(). The result is temporary and cannot be used by objects from the main database.
Parameters:
depsgraph (Depsgraph | None) â Dependency Graph, Evaluated dependency graph
apply_modifiers (bool) â Apply the deform modifiers on the control points of the curve. This is only supported for curve objects. (optional)
Returns:
Curve created from object
Return type:
Curve
