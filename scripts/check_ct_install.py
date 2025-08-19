import ctranslate2
print("CT2 CUDA devices:", ctranslate2.get_cuda_device_count())
print("Supported compute types:", ctranslate2.get_supported_compute_types("cuda"))
