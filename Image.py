import requests
from PySide6.QtGui import QImageWriter


def save_image_from_url(url, file_path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(file_path, 'wb') as file:
            file.write(response.content)
            file.close()
            print(url)
            print(file_path)
            print(f"Image saved successfully at {file_path}")
    else:
        print(f"Failed to download image. Error code: {response.status_code}")

