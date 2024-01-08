# Define the custom exception
class FieldException(Exception):
    def __init__(self, message, field_code = 0):
        self.message = message
        super().__init__(message)
        self.field_code = field_code