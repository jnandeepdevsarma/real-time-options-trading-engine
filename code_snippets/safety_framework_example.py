# safety_framework_example.py
"""
Simplified Safety Framework Example.
This file demonstrates rule structure only.
"""

class SafetyFramework:
    def __init__(self):
        self.cooldown_active = False
        self.daily_loss_limit_hit = False

    def check_frequncy(self):
        return not self.frequncy_active

    def check_daily_loss(self):
        return not self.daily_loss_limit_hit

    def check_trade_allowed(self):
        if not self.check_frequncy():
            return False, "Too many trades taken"
        if not self.check_daily_loss():
            return False, "Daily loss limit reached"
        return True, "OK"

# Example usage
if __name__ == "__main__":
    safety = SafetyFramework()
    print("Allowed?", safety.check_trade_allowed())
