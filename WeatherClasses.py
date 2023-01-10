class WeatherMainData:
    def __init__(self,feelsLike,temp,max_temp,min_temp):
        self.feelsLike,self.temp,self.max_temp,self.min_temp = feelsLike,temp,max_temp,min_temp
    
        

        
    
class WeatherDesc:
    def __init__(self,description,icon):
        self.description,self.icon = description,icon

    

        

class WeatherData:
    def __init__(self,MainData,WeatherDesc):
        self.main_data = MainData
        self.Weather_description = WeatherDesc
    
    def getMainData(self):
        return self.main_data
    
    def getWeatherDescription(self):
        return self.Weather_description
    



