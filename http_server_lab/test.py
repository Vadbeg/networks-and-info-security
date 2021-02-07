import requests


if __name__ == '__main__':
    url = "http://localhost:8888/data/hello.html"

    payload = {}
    files = [
        ('image', ('image.jpeg', open('data/grapefruit.jpg', 'rb'), 'image/jpeg'))
    ]
    headers = {}

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    print(response)
