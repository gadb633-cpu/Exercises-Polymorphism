# 1. Device Activation
class Device:
    def __init__(self,name):
        self.name =name
    def activate(self):
        return f"Device {self.name} is now on."
class SmartTV(Device):
    def __init__(self, name):
        super().__init__(name)     
    def activate(self):
        return f"TV {self.name} is playing the home screen."
class SmartSpeaker(Device):
    def __init__(self, name):
        super().__init__(name)
    def activate(self):
        return f"Speaker {self.name} is ready to play music."            
samsung = SmartTV("Samsung")    
echo = SmartSpeaker("Echo")
print(samsung.activate())
print(echo.activate())