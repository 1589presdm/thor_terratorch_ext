from pathlib import Path
import random

random.seed(42)

images_dir = Path('') # path to tif images
splits_dir = Path('') # path where splits data will be saved 
splits_dir.mkdir(parents=True, exist_ok=True)

files = sorted([f.stem for f in images_dir.glob("*.tif")])
random.shuffle(files)

train = files[:95]
val = files[95:115]
test = files[115:135]

(splits_dir/ "train.txt").write_text("\n".join(train) + "\n")
(splits_dir/ "val.txt").write_text("\n".join(val) + "\n")
(splits_dir/ "test.txt").write_text("\n".join(test) + "\n")

print(f"train: {len(train)}")
print(f"val: {len(val)}")
print(f"test: {len(test)}")