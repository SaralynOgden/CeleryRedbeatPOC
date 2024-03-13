from signal_type import SignalType

class Order():
    symbol_name: str
    signal: SignalType
    price: float
    deviation: int

    def __init__(self, symbol_name, signal, price, deviation):
        self.symbol_name = symbol_name
        self.signal = signal
        self.price = price
        self.deviation = deviation
    
    def __str__(self) -> str:
        return f'SymbolName: {self.symbol_name}, Price: {self.price}, Signal: {self.signal}'
    
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
        sort_keys=True, indent=4)
