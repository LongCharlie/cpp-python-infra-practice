import sys
import torch

print("="*60)
print(f"sys.executable          : {sys.executable}")
print(f"PyTorch version         : {torch.__version__}")
# pytorch编译构建时的CUDA版本
print(f"PyTorch built‑with CUDA : {torch.version.cuda}")
# cudnn版本
print(f"CuDNN version           : {torch.backends.cudnn.version()}")
print(f"CUDA available(runtime) : {torch.cuda.is_available()}")

# CUDA_VISIBLE_DEVICES 环境变量，控制设备可见
import os
cuda_visible = os.environ.get("CUDA_VISIBLE_DEVICES", "<not set>")
print(f"CUDA_VISIBLE_DEVICES    : {cuda_visible}")

if torch.cuda.is_available():
    print(f"GPU count               : {torch.cuda.device_count()}")
    for i in range(torch.cuda.device_count()):
        print(f"  Device {i} name       : {torch.cuda.get_device_name(i)}")
        print(f"  Device {i} properties : {torch.cuda.get_device_properties(i)}")
else:
    print("No CUDA GPU available")
print("="*60)
