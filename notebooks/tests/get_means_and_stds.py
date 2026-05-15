from pathlib import Path
import numpy as np
import tifffile

images_dir = Path('') # the path where are tif_images were saved 
train_split_path = Path('') # the path where splits files were saved
# the train.txt file was used to compute mean/stds 

train_ids = [line.strip() for line in train_split_path.read_text().splitlines() if line.strip()]

sum_channels = None
sum_sq_channels = None
num_pixels = 0


for sample_id in train_ids:
    tif_path = images_dir / f"{sample_id}.tif"
    
    if not tif_path.exists():
        print(f"file not found: {tif_path}")
        continue
    
    arr = tifffile.imread(tif_path)
    
    if arr.ndim != 3:
        print(f"unepxected shape for {tif_path.name}: {arr.shape}")
        continue

    if arr.shape[0] == 2:      
        arr = np.moveaxis(arr, 0, -1)  

    if arr.shape[2] != 2:
        print(f"unepxected shape for {tif_path.name}: {arr.shape}")
        continue
    
    arr = arr.astype(np.float64)
    
    pixels = arr.reshape(-1, arr.shape[2])
    
    if sum_channels is None:
        sum_channels = np.zeros(pixels.shape[1], dtype=np.float64)
        sum_sq_channels = np.zeros(pixels.shape[1], dtype=np.float64)
        
    sum_channels += pixels.sum(axis=0)
    sum_sq_channels += (pixels ** 2).sum(axis=0)
    num_pixels += pixels.shape[0]
    
means = sum_channels / num_pixels
variances = (sum_sq_channels / num_pixels) - (means ** 2)
stds = np.sqrt(variances)

print("train images used:", len(train_ids))
print("num_pixels:", num_pixels)
print("means:", means.tolist())
print("stds:", stds.tolist())