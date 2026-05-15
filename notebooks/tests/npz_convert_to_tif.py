import numpy as np
from pathlib import Path
import tifffile

npz_dir = Path('') # path to the directory with NPZ files
tif_dir = Path('') # the path where tif_mask files will be saved

tif_dir.mkdir(parents=True, exist_ok=True)

for npz_file in npz_dir.glob('*.npz'):
    data = np.load(npz_file)
    
    mask = data['ice_mask']
    
    mask = np.squeeze(mask)
    
    mask = mask.astype(np.uint8)
    
    out_name = npz_file.stem.replace('ice_mask', '') + '_mask.tif'
    out_path = tif_dir / out_name
    
    tifffile.imwrite(out_path, mask)
    
    print(f"Saved: {out_path.name} | shape={mask.shape} | dtype={mask.dtype} | unique={np.unique(mask)}")