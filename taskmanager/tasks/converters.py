from datetime import datetime

class DateConverter:
    regex = r"[0-9]{4}-[0-9]{2}-[0-9]{2}"

    def to_python(self, value):
        # Convert the string to a Python date object
        return datetime.strptime(value, "%Y-%m-%d").date()

    def to_url(self, value):
        # Convert a Python date object back to string for URL
        return value.strftime("%Y-%m-%d")
