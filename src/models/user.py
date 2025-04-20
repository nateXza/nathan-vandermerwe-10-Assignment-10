class User:
    def __init__(self, user_id, name):
        self._user_id = user_id  # Private attribute
        self._name = name

    def upload_image(self, image_url):
        print(f"{self._name} uploaded an image: {image_url}")

    def view_report(self, report):
        print(f"{self._name} viewed report: {report}")