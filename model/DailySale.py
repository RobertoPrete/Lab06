from dataclasses import dataclass
from datetime import datetime


@dataclass
class DailySale:
    Retailer_code: int
    Product_number: int
    Order_method_code: int
    Date: datetime
    Quantity: int
    Unit_price: float
    Unit_sale_price: float

    def __hash__(self):
        return hash(self._id)

    def __str__(self):
        return self.Retailer_code
