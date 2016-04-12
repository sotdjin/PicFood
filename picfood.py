import json
import sys


def main():
    data = []
    with open('yelp_academic_dataset_business.json') as f:
        for line in f:
            data.append(json.loads(line))
    print len(data)
    restaurant_data = []
    for x in range(len(data)):
        if "Restaurants" in data[x]["categories"]:
            restaurant_data.append(data[x])
    print len(restaurant_data)
    
    photo_data = []
    with open('photo_id_to_business_id.json') as f:
        photo_data = json.load(f)
    kept_photos = []
    print len(photo_data)
    restaurant_data_indexed = {}
    for item in restaurant_data:
        restaurant_data_indexed[item["business_id"]] = item
    for item in photo_data:
        if (item["business_id"]) in restaurant_data_indexed:
            kept_photos.append(item)
    print len(kept_photos)
    print "how many photos have labels and or captions"
    count = 0
    test_photos = []
    for item in kept_photos:
        if item["caption"] == "" and (item["label"] == "food" or item["label"] == "drink" or item["label"] == "none"):
            count += 1
            test_photos.append(item["photo_id"])
    print count
    file = open("photo_id_to_restuarant_NV.json", 'w')
    file.write(json.dumps(kept_photos))
    file.close()
    label_word = {}
    for item in kept_photos:
        if item["label"] not in label_word:
            label_word[item["label"]] = 1
    label_file = open("unique labels.txt", 'w')
    label_file.write(json.dumps(label_word))
    label_file.close()
    
    photo_id_file = open("photo_id.txt", 'w')
    for x in range(10):
        uri = "C://2016_yelp_dataset_challenge_photos//" + test_photos[x] + ".jpg 4:10"
        photo_id_file.write(uri + '\n')
    photo_id_file.close()
    
if __name__ == '__main__':
    main()