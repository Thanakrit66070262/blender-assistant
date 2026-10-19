# bpy.types.Scene.audio_distance_model

## Signature
```python
audio_distance_modelÂ
Description
Distance model for distance attenuation calculation (default 'INVERSE_CLAMPED')
NONE
None â No distance attenuation.
INVERSE
Inverse â Inverse distance model.
INVERSE_CLAMPED
Inverse Clamped â Inverse distance model with clamping.
LINEAR
Linear â Linear distance model.
LINEAR_CLAMPED
Linear Clamped â Linear distance model with clamping.
EXPONENT
Exponential â Exponential distance model.
EXPONENT_CLAMPED
Exponential Clamped â Exponential distance model with clamping.
Type:
Literal[âNONEâ, âINVERSEâ, âINVERSE_CLAMPEDâ, âLINEARâ, âLINEAR_CLAMPEDâ, âEXPONENTâ, âEXPONENT_CLAMPEDâ]
