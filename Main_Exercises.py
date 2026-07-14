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

# 3. Status Reports
class Device:
    def __init__(self,name, is_on):
        self.is_on = is_on
        self.name =name
    def status(self):
        return f"{self.name}: on or {self.name}: off"
class SmartTV(Device):
    def __init__(self, name, is_on,channel):
        super().__init__(name, is_on)
        self.channel=channel
    def status(self):
        return f"{self.name}: on, watching channel {self.channel} or {self.name}: off"
class SmartSpeaker(Device):
    def __init__(self, name, is_on,song):
        super().__init__(name, is_on)
        self.song=song
    def status(self):
        return f"{self.name}: on, playing {self.song}"
    
lg = SmartTV("LG", True, 8)
alexa = SmartSpeaker("Alexa", True, "Bohemian Rhapsody")         
print(lg.status())
print(alexa.status())

# 4. Mixed List Activation
class Device:
    def __init__(self,name):
        self.name =name
    def activate(self):
        return f"Device {self.name} is now on."
class SmartTV(Device):
    def __init__(self, name):
        super().__init__(name)
    def activate(self):
        return f"{self.name} is playing the home screen."
class SmartLamp(Device):
    def __init__(self, name):
        super().__init__(name)
    def activate(self):
        return f"{self.name} is glowing warmly."
class SmartSpeaker(Device):
    def __init__(self, name):
        super().__init__(name)
    def activate(self):
        return f"Speaker {self.name} is ready to play musi."
list_instance = []
lg = SmartTV("LG")
desk_Lamp = SmartLamp("Desk Lamp")    
echo = SmartSpeaker("Echo")
list_instance.append(lg)
list_instance.append(desk_Lamp)
list_instance.append(echo)
for list1 in list_instance:
    print(list1.activate())





