class Report:
    def __init__(self, report_id, content):
        self._report_id = report_id
        self._content = content

    def generate_pdf(self):
        print(f"Generating PDF for report ID: {self._report_id}")