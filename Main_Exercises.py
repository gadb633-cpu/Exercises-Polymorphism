# # 1. Device Activation
# class Device:
#     def __init__(self,name):
#         self.name =name
#     def activate(self):
#         return f"Device {self.name} is now on."
# class SmartTV(Device):
#     def __init__(self, name):
#         super().__init__(name)     
#     def activate(self):
#         return f"TV {self.name} is playing the home screen."
# class SmartSpeaker(Device):
#     def __init__(self, name):
#         super().__init__(name)
#     def activate(self):
#         return f"Speaker {self.name} is ready to play music."            
# samsung = SmartTV("Samsung")    
# echo = SmartSpeaker("Echo")
# print(samsung.activate())
# print(echo.activate())

# # 2. Deactivate with Override
# class Device:
#     def __init__(self,name):
#         self.name = name
#     def deactivate(self):
#         return f"Device {self.name} is now off."
# class SmartLamp(Device):
#     def __init__(self, name):
#         super().__init__(name)
#     def deactivate(self):
#         return f"Lamp {self.name} is dimming and turning off."
# class SmartAC(Device):
#     def __init__(self, name):
#         super().__init__(name)
#     def deactivate(self):
#         return f"AC {self.name} is cooling down and switching off."     
# Bedroom_Lamp=SmartLamp("Bedroom Lamp")
# Living_Room_AC=SmartAC("Living Room AC")
# print(Bedroom_Lamp.deactivate())
# print(Living_Room_AC.deactivate())

# # 3. Status Reports
# class Device:
#     def __init__(self,name, is_on):
#         self.is_on = is_on
#         self.name =name
#     def status(self):
#         return f"{self.name}: on or {self.name}: off"
# class SmartTV(Device):
#     def __init__(self, name, is_on,channel):
#         super().__init__(name, is_on)
#         self.channel=channel
#     def status(self):
#         return f"{self.name}: on, watching channel {self.channel} or {self.name}: off"
# class SmartSpeaker(Device):
#     def __init__(self, name, is_on,song):
#         super().__init__(name, is_on)
#         self.song=song
#     def status(self):
#         return f"{self.name}: on, playing {self.song}"
    
# lg = SmartTV("LG", True, 8)
# alexa = SmartSpeaker("Alexa", True, "Bohemian Rhapsody")         
# print(lg.status())
# print(alexa.status())

# # 4. Mixed List Activation
# class Device:
#     def __init__(self,name):
#         self.name =name
#     def activate(self):
#         return f"Device {self.name} is now on."
# class SmartTV(Device):
#     def __init__(self, name):
#         super().__init__(name)
#     def activate(self):
#         return f"{self.name} is playing the home screen."
# class SmartLamp(Device):
#     def __init__(self, name):
#         super().__init__(name)
#     def activate(self):
#         return f"{self.name} is glowing warmly."
# class SmartSpeaker(Device):
#     def __init__(self, name):
#         super().__init__(name)
#     def activate(self):
#         return f"Speaker {self.name} is ready to play musi."
# list_instance = []
# lg = SmartTV("LG")
# desk_Lamp = SmartLamp("Desk Lamp")    
# echo = SmartSpeaker("Echo")
# list_instance.append(lg)
# list_instance.append(desk_Lamp)
# list_instance.append(echo)
# for list1 in list_instance:
#     print(list1.activate())

# # 5. Volume Control Override
# class Device:
#     def __init__(self,name):
#         self.name =name
#     def set_volume(self,level):
#         return f"Device {self.name} volume set to {level}."
# class SmartSpeaker(Device):
#     def __init__(self, name):
#         super().__init__(name)
#     def set_volume(self,level):
#         return f"Speaker {self.name} is now at volume {level}/10. {'Loud!' if level > 7 else ''}"        
# class SmartTV(Device):
#     def __init__(self, name):
#         super().__init__(name)
#     def set_volume(self,level):
#         return f"TV {self.name} volume: {level}. {'Muted!' if level == 0 else ''}"    
# bose= SmartSpeaker("Bose")
# lg = SmartTV("LG")
# print(bose.set_volume(9))
# print(bose.set_volume(3))
# print(lg.set_volume(8))
# print(lg.set_volume(0))

# # 6. Uniform Command Execution
# class Device:
#     def __init__(self,name):
#         self.name = name
#     def run_command(self,cmd):
#         return f"Device {self.name} received command: {cmd}."
#     def send_command(self,device, cmd):
#         return device.run_command(cmd)
# class SmartTv(Device):
#     def __init__(self, name):
#         super().__init__(name)
#     def run_command(self,cmd):
#         return f"Device {self.name} is: {cmd}."    
# class SmartSpeaker(Device):
#     def __init__(self, name):
#         super().__init__(name)
#     def run_command(self,cmd):
#         return f"Device {self.name} Low battery: {cmd}."
# class SmartLamp(Device):
#     def __init__(self, name):
#         super().__init__(name)
#     def run_command(self,cmd):
#         return f"Device {self.name} Low light: {cmd}."          
# class SmartAC(Device):
#     def __init__(self, name):
#         super().__init__(name)
#     def run_command(self,cmd):
#         return f"Device {self.name} is No refrigerator: {cmd}."  
# list_instance =[]
# lg = SmartTv("LG")
# desk_Lamp = SmartLamp("Desk Lamp")    
# echo = SmartSpeaker("Echo")
# samsung = SmartAC("samsung")
# list_instance.append(lg)
# list_instance.append(desk_Lamp)                      
# list_instance.append(echo)                      
# list_instance.append(samsung)
# for list1 in list_instance:
#     print(list1.send_command(list1,"start"))

# # 7. Smart Home Schedule
# class Device:
#     def __init__(self,name):
#         self.name =name
#     def run_schedule(self,hour):
#         return f"{self.name} is idle."
# class SmartLamp(Device):
#     def __init__(self, name):
#         super().__init__(name)
#     def run_schedule(self,hour):
#         return f"{self.name}: turning on." if 18 <= hour <= 23 else f"{self.name}: turning off."
# class SmartAC(Device):
#     def __init__(self, name):
#         super().__init__(name)
#     def run_schedule(self,hour):
#         return f"{self.name}: turning on." if 12 <= hour <= 20 else f"{self.name}: turning off."
# class SmartTV(Device):
#     def __init__(self, name):
#         super().__init__(name)
#     def run_schedule(self,hour):
#         return f"{self.name}: turning on." if 20 <= hour <= 23 else f"{self.name}: turning off." 
# desk_Lamp = SmartLamp("Desk Lamp")                                
# samsung = SmartAC("samsung")
# lg = SmartTV("LG")
# print(desk_Lamp.run_schedule(21))
# print(samsung.run_schedule(21))
# print(lg.run_schedule(21))

# 8. Energy Usage Override
class Device:
    def __init__(self,name,watts):
        self.name = name
        self.watts=watts
    def energy_usage(self):
        return self.watts
class SmartTv(Device):
    def __init__(self, name,watts):
        super().__init__(name,watts)
    def energy_usage(self):
        return f"{self.name}:{self.watts}w"    
class SmartSpeaker(Device):
    def __init__(self, name,watts):
        super().__init__(name,watts)
    def energy_usage(self):
        return f"{self.name}:{self.watts}w"
class SmartLamp(Device):
    def __init__(self, name,watts):
        super().__init__(name,watts)
    def energy_usage(self):
        return f"{self.name}:{self.watts}w"        
class SmartAC(Device):
    def __init__(self, name,watts):
        super().__init__(name,watts)
    def energy_usage(self):
        return f"{self.name}:{self.watts}w" 
list_instance =[]
lg = SmartTv("LG",150)
desk_Lamp = SmartLamp("Desk Lamp",8)    
echo = SmartSpeaker("Echo",30)
samsung = SmartAC("samsung",900)
list_instance.append(lg)
list_instance.append(desk_Lamp)                      
list_instance.append(echo)                      
list_instance.append(samsung)
total = 0
for instance in list_instance:
    total += instance.watts
    print(instance.energy_usage())
print(f"total is: {total}")







