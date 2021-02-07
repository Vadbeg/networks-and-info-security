import requests


if __name__ == '__main__':
    url = "http://localhost:8888/data/"
    file_path = '/home/vadbeg/Downloads/wall1.jpg'

    with open(file=file_path, mode='rb') as file:
        payload = file.read()

    headers = {
        'Content-Type': 'image/jpeg'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response)
