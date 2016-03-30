import json
import sys
def main():
    data = []
    with open('yelp_academic_dataset_business.json') as f:
        for line in f:
            data.append(json.loads(line))
    print len(data)
    restuarant_data=[]
    for x in range(len(data)):
        if "Restaurants" in data[x]["categories"] and "NV" in data[x]["state"]:
            restuarant_data.append(data[x])
    print len(restuarant_data)
    
    photo_data = []
    with open('photo_id_to_business_id.json') as f:
        photo_data = json.load(f)
    kept_photos=[]
    print len(photo_data)
    restuarant_data_indexed={}
    for item in restuarant_data:
            restuarant_data_indexed[item["business_id"]]=item
    for item in photo_data:
        if (item["business_id"])in restuarant_data_indexed:
            kept_photos.append(item)
    print len(kept_photos)
    
if __name__ == '__main__':
  main()