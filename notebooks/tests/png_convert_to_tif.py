from pathlib import Path
from PIL import Image
import numpy as np
import rasterio


png_dir = Path("") # path to the directory with PNG files
tif_dir = Path("") # the path where TIF files will be saved
tif_dir.mkdir(parents=True, exist_ok=True)

for png_file in png_dir.glob("*.png"):
    arr = np.array(Image.open(png_file))

    r = arr[:, :, 0].astype(np.uint8)
    b = arr[:, :, 2].astype(np.uint8)

    h, w = r.shape
    out_path = tif_dir / f"{png_file.stem}.tif"

    with rasterio.open(
        out_path,
        "w",
        driver="GTiff",
        height=h,
        width=w,
        count=2,
        dtype=np.uint8,
    ) as dst:
        dst.write(r, 1)  
        dst.write(b, 2)  

    print(f"saved: {out_path}")