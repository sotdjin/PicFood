import requests
import json
import sys
def main():
    data = open('test_photos.json', 'rb').read()
    response = requests.post(url='https://vision.googleapis.com/v1/images:annotate?key=<API-key>',
    data=data,
    headers={'Content-Type': 'application/json'})
    response_file=open("response_file.json","w")
    response_file.write(response.text)
    response_file.close()
if __name__ == '__main__':
  main()