# bpy.types.RenderSettings.compositor_denoise_device

## Signature
```python
compositor_denoise_deviceÂ
Description
The device to use to process the denoise nodes in the compositor (default 'AUTO')
AUTO
Auto â Use the same device used by the compositor to process the denoise node.
CPU
CPU â Use the CPU to process the denoise node.
GPU
GPU â Use the GPU to process the denoise node if available, otherwise fallback to CPU.
Type:
Literal[âAUTOâ, âCPUâ, âGPUâ]
