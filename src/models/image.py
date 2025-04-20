class Image:
    def __init__(self, image_id, url):
        self._image_id = image_id
        self._url = url
        self._status = "Pending"

    def validate(self):
        self._status = "Valid" if self._url.endswith(('.jpg', '.png')) else "Invalid"
        return self._status

    def process(self):
        if self._status == "Valid":
            print(f"Processing image: {self._url}")
        else:
            print("Cannot process invalid image.")