# bpy.types.Object.crazyspace_eval

## Signature
```python
crazyspace_eval(depsgraph, scene)Â
Description
Compute orientation mapping between vertices of an original object and object with shape keys and deforming modifiers applied.The evaluation is to be freed with the crazyspace_eval_free function
Parameters:
depsgraph (Depsgraph | None) â Dependency Graph, Evaluated dependency graph
scene (Scene | None) â Scene, Scene of the object
