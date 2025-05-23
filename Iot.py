import json
import cv2
import os
import matplotlib.pyplot as plt
from collections import defaultdict

annotations_path = '_annotations.coco.json'
images_dir = 'valid'


with open(os.path.join(images_dir, annotations_path)) as f:
    data = json.load(f)


images = {img["id"]: img["file_name"] for img in data["images"]}


annotations_per_image = defaultdict(list)
for ann in data["annotations"]:
    annotations_per_image[ann["image_id"]].append(ann)


for image_idx, (image_id, anns) in enumerate(annotations_per_image.items()):
    image_name = images[image_id]
    image_path = os.path.join(images_dir, image_name)

    img = cv2.imread(image_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    for idx, ann in enumerate(anns):
        x, y, w, h = map(int, ann["bbox"])
        label = f"moto_{idx+1}"

        
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

       
        if image_idx == 0:  
            text_y = y - 10 if idx % 2 == 0 else y + h + 20
        else: 
            text_y = y - 10

        text_x = x
        (text_w, text_h), baseline = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 2)
        cv2.rectangle(img, (text_x - 2, text_y - text_h - 2), (text_x + text_w + 2, text_y + baseline), (0, 0, 0), cv2.FILLED)
        cv2.putText(img, label, (text_x, text_y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 0), 2)

    
    plt.figure(figsize=(16, 9))
    plt.imshow(img)
    plt.axis("off")
    plt.title(f"Motos numeradas - {image_name}")
    plt.show()
