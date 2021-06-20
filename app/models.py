from datetime import datetime, timedelta


class DollarModel:
    def __init__(self, usd, ves):
        self.usd = usd
        self.ves = ves
        self.date = datetime.utcnow() - timedelta(hours=4)

