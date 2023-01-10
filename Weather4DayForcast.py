
from typing import List
from collections import namedtuple
from datetime import datetime



class Daily_MinMax_Condition:
    dayName: str
    dailyMin : str
    dailyMax : str
    weather_icon_max : str
    weather_icon_min : str

    def __init__(self,date,obj) -> None:
        self.dayName =datetime.strptime(date, '%Y-%m-%d').strftime('%a')
        self.dailyMax = obj[0][1]
        self.weather_icon_max = obj[0][2]
        self.dailyMin = obj[1][1]
        self.weather_icon_min= obj[1][2]
        #print(obj)




        

class City:
    def __init__(self,name):
        self.CityName = name


class Weather_main:
     
    # def getDataToTuple(weatherData):
    #     return namedtuple("wtrDt1",weatherData.keys())(*weatherData.values())

     #def __init__(self,feelsLike,temp,max_temp,min_temp):
    def __init__(self,weatherData):
        data = namedtuple("wtrDt1",weatherData.keys())(*weatherData.values())
        self.feelsLike,self.temp,self.max_temp,self.min_temp = data.feels_like,data.temp,data.temp_max,data.temp_min
        #data.feelsLike,data.temp,data.max_temp,data.min_temp

class Weather_description:
    def __init__(self,data):
        data = namedtuple("wtrDt1",data.keys())(*data.values())
        self.description,self.icon = data.description,data.icon

        
class ForcastListItem:
    dt : int
    dt_txt : str
    Weather_main : Weather_main
    Weather_description : Weather_description

    def __init__(self,listObj):
        self.dt=listObj.get('dt')
        self.dt_txt=listObj.get('dt_txt')
        self.weather_main= Weather_main(listObj.get('main'))
        self.weather_description = Weather_description(listObj.get('weather')[0])  # weather is a list with 1 item

    # def __init__(self,dt,dt_txt,Weather_main,Weather_description):
    #     self.dt,self.dt_txt,self.weather_main,self.weather_description = dt,dt_txt,Weather_main,Weather_description



class Weather4DayForcast:
    ForcastList : List[ForcastListItem]
    City : City
    
    def __init__(self,input):
        self.City = City(input.get('city'))
        aa = [ForcastListItem(Item) for Item in input.get('list')]
        self.ForcastList = aa
        #self.ForcastList = ForcastListItem(input.get('list'))
    # def __init__(self,City : City, cnt :int , cod : str, list : List[ForcastList]):
    #     self.City,self.ForcastList = City,list
    # def __init__(self,City,ForcastList : List[ForcastList]):
    #     self.City,self.ForcastList = City,ForcastList





               