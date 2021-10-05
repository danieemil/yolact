import collections
import json
import numpy


number  = 40
dones   = 0

with open("./data/coco/annotations/instances_train2014.json", "r") as f:
    data = json.load(f)
    images = data.get("images")
    categories = data.get("categories")
    annos = data.get("annotations")
    for anno in annos:
        if (anno.get("image_id")==168806):

            if number < dones:
                break
            dones = dones + 1


            print(anno)
            print()

            category_id = anno.get("category_id")
            image_id = anno.get("image_id")

            for image in images:
                if image.get("id")==image_id:
                    print("Url : " + image.get("coco_url"))
            
            for category in categories:
                if category.get("id")==category_id:
                    print("Categoría : " + category.get("name"))
            
            print()
            print()