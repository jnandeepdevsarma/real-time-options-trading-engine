# execution_layer_example.py
"""
Illustrative example of the Execution Layer.
This code does NOT contain real broker logic.
It demonstrates the structure only.
"""

class ExecutionLayer:
    def __init__(self, broker):
        self.broker = broker

    def verify_order(self, trade):
        if trade["qty"] <= 0:
            return False, "Invalid quantity"
        if trade["sl"] is None or trade["tp"] is None:
            return False, "Invalid SL/TP"
        return True, "OK"

    def execute(self, trade):
        ok, msg = self.verify_order(trade)
        if not ok:
            return {"status": "rejected", "reason": msg}

        # Mock broker response
        response = {
            "status": "filled",
            "avg_price": trade["price"],
            "order_id": "MOCK12345"
        }

        return response


# Example usage
if __name__ == "__main__":
    broker = object()   # placeholder
    engine = ExecutionLayer(broker)

    trade = {
        "strike": 24650,
        "price": 101.20,
        "qty": 75,
        "sl": 14.0,
        "tp": 28.0
    }

    print(engine.execute(trade))
