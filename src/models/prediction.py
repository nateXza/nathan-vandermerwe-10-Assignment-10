class Prediction:
    def __init__(self, prediction_id, disease_name):
        self._prediction_id = prediction_id
        self._disease_name = disease_name

    def generate_report(self):
        return f"Report for disease: {self._disease_name}"