import tensorflow as tf

print("Testing for GPU")
if tf.test.is_gpu_available:	
    print("GPU is available")

if tf.test.is_gpu_available(cuda_only=True):
    print("NVidia CUDA GPU is available")

if tf.test.is_gpu_available(cuda_only=False):
    print("No NVidia CUDA GPU available")
