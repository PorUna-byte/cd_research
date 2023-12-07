import os
import json
import subprocess
import shutil

# for split in ["train", "val", "test"]:
#     if os.path.exists(os.path.join(split, "A")):
#         shutil.rmtree(os.path.join(split, "A"))
#     if os.path.exists(os.path.join(split, "B")):
#         shutil.rmtree(os.path.join(split, "B"))
#     if os.path.exists(os.path.join(split, "label")):
#         shutil.rmtree(os.path.join(split, "label"))

#     os.mkdir(os.path.join(split, "A"))
#     os.mkdir(os.path.join(split, "B"))
#     os.mkdir(os.path.join(split, "label"))

#     fr_json = open(os.path.join(split, f"{split}.json"))
#     file_json = json.load(fr_json)
#     for i, image in enumerate(file_json['images'], start=1):
#         if os.path.exists(os.path.join(split, 'mask', image['file_name'].split('.')[0]+'_mask.jpg')):

#             command = f"cp {os.path.join(split, 'sample', image['file_name'])} {os.path.join(split, 'B', f'{split}_{i:04d}.jpg')}"
#             result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

#             command = f"cp {os.path.join(split, 'template', image['template_name'])} {os.path.join(split, 'A', f'{split}_{i:04d}.jpg')}"
#             result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            
#             command = f"cp {os.path.join(split, 'mask', image['file_name'].split('.')[0]+'_mask.jpg')} {os.path.join(split, 'label', f'{split}_{i:04d}.jpg')}"
#             result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

for split in ["train", "val", "test"]:
    for element in ["A", "B", "label"]:
        for i in range(5500):
            if os.path.exists(os.path.join(split, element, split+f"_{i:04d}.jpg")):                
                command = f"convert -resize 1024x1024! {os.path.join(split, element, split+f'_{i:04d}.jpg')} {os.path.join(split, element, split+f'_{i:04d}.jpg')} "
                result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)