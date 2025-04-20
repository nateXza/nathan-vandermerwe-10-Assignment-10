class ImageFactory:
    @staticmethod
    def create_image(image_type, image_id, url):
        if image_type == "JPG":
            return JPGImage(image_id, url)
        elif image_type == "PNG":
            return PNGImage(image_id, url)
        else:
            raise ValueError("Unsupported image type")

class JPGImage:
    def __init__(self, image_id, url):
        self.image_id = image_id
        self.url = url

class PNGImage:
    def __init__(self, image_id, url):
        self.image_id = image_id
        self.url = url