# bpy.types.Object.users_collection

## Signature
```python
users_collectionÂ
Description
The collections this object is in.
Type:
tuple[Collection, â¦]
Note
Takes O(len(bpy.data.collections) + len(bpy.data.scenes)) time.
(readonly)
