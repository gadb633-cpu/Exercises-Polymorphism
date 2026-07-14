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

# 2. Deactivate with Override
class Device:
    def __init__(self,name):
        self.name = name
    def deactivate(self):
        return f"Device {self.name} is now off."
class SmartLamp(Device):
    def __init__(self, name):
        super().__init__(name)
    def deactivate(self):
        return f"Lamp {self.name} is dimming and turning off."
class SmartAC(Device):
    def __init__(self, name):
        super().__init__(name)
    def deactivate(self):
        return f"AC {self.name} is cooling down and switching off."     
Bedroom_Lamp=SmartLamp("Bedroom Lamp")
Living_Room_AC=SmartAC("Living Room AC")
print(Bedroom_Lamp.deactivate())
print(Living_Room_AC.deactivate())
    
