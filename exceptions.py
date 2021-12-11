
class WrongSignException(Exception):
    def __init__(self, message = 'invalid sign'):
        super().__init__(message)
    def __str__(self):
        return '{} is invalid input, can only accept ' \
               '+, -, *, /, 0  as its values'.format(self.value)

 