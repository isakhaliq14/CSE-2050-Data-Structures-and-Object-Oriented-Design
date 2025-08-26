class SmartDevice():
    def __init__(self, name):
        '''Initializes the device with a given name and sets the status to False (off) by default.'''
        self.name = name
        self.status = False
    
    def turn_on(self):
        '''Turns the device on by setting the status attribute to True.'''
        self.status = True

    def turn_off(self):
        '''Turns the device off by setting the status attribute to False.'''
        self.status = False
    
    def __str__(self):
        '''Returns a string representation of the device, showing the name and its current on/off status.'''
        if self.status == True:
            return f'{self.name}: ON'
        else:
            return f'{self.name}: OFF'
        
class Light(SmartDevice):
    def __init__(self, name):
        super().__init__(name)
        self.brightness = 100

    def adjust_brightness(self, level):
        '''Adjusts the brightness of the light. The brightness is only changed if the level is between 1 and 100 (inclusive). If the level is outside this range, the brightness remains unchanged.'''
        if level >= 1 and level <= 100:
            self.brightness = level
        else:
            pass
    
    def __str__(self):
        '''Returns a string representation of the light, showing the name, its current on/off status, and its brightness level.'''
        if self.status == True:
            return f'{self.name}: ON, Brightness: {self.brightness}'
        else:
            return f'{self.name}: OFF, Brightness: {self.brightness}'
        
class Thermostat(SmartDevice):
    def __init__(self, name):
        super().__init__(name)
        self.temperature = 65.0

    def adjust_temperature(self, temp):
        '''Adjusts the temperature of the thermostat. If the temperature is within this range, it updates the temperature attribute. If not, it leaves the temperature unchanged.'''
        if self._check_temperature_limits(temp):
            self.temperature = temp

    def __str__(self):
        '''Returns a string representation of the thermostat, showing the name, its current on/off status, and the current temperature.'''
        if self.status == True:
            return f'{self.name}: ON, Temperature: {self.temperature}'
        else:
            return f'{self.name}: OFF, Temperature: {self.temperature}'
        
    def _check_temperature_limits(self, temp):
        '''Checks if the given temperature is within the acceptable range. This is a private method used internally to validate temperature adjustments.'''
        if temp >= 55.0 and temp <= 80.0:
            return True
        else: 
            return False
        
class Speaker(SmartDevice):
    def __init__(self, name):
        super().__init__(name)
        self.volume = 3

    def increase_volume(self):
        '''Increases the volume by 1, with a maximum volume of 10.'''
        if self.volume < 10:
            self.volume += 1
        else: 
            pass

    def decrease_volume(self):
        '''Decreases the volume by 1, with a minimum volume of 1.'''
        if self.volume > 1:
            self.volume -= 1
        else: 
            pass

    def __str__(self):
        '''Returns a string representation of the speaker, showing the name, its current on/off status, and its volume setting.'''
        if self.status == True:
            return f'{self.name}: ON, Volume: {self.volume}'
        else:
            return f'{self.name}: OFF, Volume: {self.volume}'
        
class SmartHome():
    def __init__(self):
        self.devices = []

    def __add__(self, other):
        '''Overloads the + operator to allow devices to be added to the SmartHome instance. This method appends the device to the devices list in the SmartHome.'''
        self.devices.append(other)

    def turn_off_all(self):
        '''Turns off all devices listed for the smart home instance.'''
        for device in self.devices:
            device.turn_off()

    def __str__(self):
        '''Returns a string listing the name and status of each device in the SmartHome instance.'''
