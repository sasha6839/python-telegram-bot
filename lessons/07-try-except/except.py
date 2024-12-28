
class FiveDivisionError(Exception):
    def __init__(self,message, error_code):
        super().__init__(message)
        self.error_code = error_code




def devide_number(a,b):
    if b == 5:
        raise FiveDivisionError('Діленняна 5 неможливо!', 400)
    return a / b

try:
    result = devide_number(4,5)
    print(result)
except FiveDivisionError as e:
    print(e)
    print(f'Код помилки {e.error_code}')