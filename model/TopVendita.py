from dataclasses import dataclass
from datetime import datetime


@dataclass
class TopVendita:
    Date: datetime
    Ricavo: float
    Retailer_code: int
    Product_number: int

    def __str__(self):
        return f"Data: {self.Date}; Ricavo: {self.Ricavo}; Retailer: {self.Retailer_code}; Product: {self.Product_number}"
