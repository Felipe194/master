class Product:
    def __init__(self, tittle:str,value:float,currency: str):
        self.tittle=tittle
        self.value=value
        self.currency=currency
        
    def to_dict(self) -> dict:
        return {
                    "title": self.tittle,
                    "value":self.value,
                    "currency":self.currency            
                }