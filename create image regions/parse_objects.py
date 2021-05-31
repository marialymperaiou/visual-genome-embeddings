import json
from visual_genome import api as vg
import pandas as pd

with open("objects.json") as file:    # objects.json locally
    data=json.load(file)
    
regions = []
images = []
for i in range(len(data)):
    region_sentences = []      # descriptions for areas of the chosen image
    image_id=data[i]['image_id']
    try:
        region = vg.get_region_descriptions_of_image(id=image_id)
        for j in region:
            region_sentences.append(j.phrase.lower())
        if region_sentences:
            images.append(image_id)
            regions.append(region_sentences) 
    except IndexError:
        continue
        
images_regions = pd.DataFrame(list(zip(images, regions)), columns =['Image_id', 'region_sentences'])
images_regions.to_csv('image_regions.csv', index=False)