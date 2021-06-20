from datetime import datetime


class DollarModel:
    def __init__(self, dollar, bolivar):
        self.dollar_quantity = dollar
        self.bolivar_quantity = bolivar
        self.date_asked = datetime.utcnow()

