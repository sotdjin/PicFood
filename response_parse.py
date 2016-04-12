import json


def main():
    s = ""
    data = []
    with open('response_file.json') as f:
        for line in f:
            s += str(line)
    data.append(json.loads(s))

if __name__ == '__main__':
    main()
