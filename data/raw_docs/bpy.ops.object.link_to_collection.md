# bpy.ops.object.link_to_collection

## Signature
```python
bpy.ops.object.link_to_collection(*, collection_uid=-1, is_new=False, new_collection_name='')Â
Description
Link objects to a collection
Parameters:
collection_uid (int) â Collection UID, Session UID of the collection to link to (in [-1, inf], optional)
is_new (bool) â New, Link objects to a new collection (optional)
new_collection_name (str) â Name, Name of the newly added collection (optional, never None)
Returns:
Result of the operator call.
Return type:
set[Literal[Operator Return Items]]
