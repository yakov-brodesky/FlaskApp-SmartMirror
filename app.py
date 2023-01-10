from flask import Flask , render_template, url_for
import requests
import json
from datetime import datetime
from collections import namedtuple
from itertools import groupby
from typing import List
from WeatherClasses import WeatherData,WeatherDesc,WeatherMainData
from ZemanimDict import zemanimDictHeb,zemaninDictEn,zmnToShow
from Weather4DayForcast import * # Weather4DayForcast,Weather_main,Weather_description,City,ForcastList
#from  .WeatherClasses import WeatherData, WeatherDesc, WeatherMainData
#from WeatherData import WeatherData




app= Flask(__name__)

def UnixTimeToStr(unixTime):
    return datetime.utcfromtimestamp(int(unixTime)).strftime('%Y-%m-%d %H:%M')
    
def getWeatherDataToTuple(weatherData):
    weatherDataFull = namedtuple("wtrDt",weatherData.keys())(*weatherData.values())
    return weatherDataFull

def getWeatherDataToTuple_1(weatherData):
    return namedtuple("wtrDt1",weatherData.keys())(*weatherData.values())
    # weatherDataFull = namedtuple("wtrDt1",weatherData.keys())(*weatherData.values())
    # return weatherDataFull
#return namedtuple('WeatherData', studentDict.keys())(*studentDict.values())
def get_weather_data() -> WeatherData:
    apiKey="c1f826dfb25ec6405ccfc5b443e34133"
    CityId =281184 # Jerusalem


    

    

    

        
    urlForCall =f'https://api.openweathermap.org/data/2.5/weather?id={CityId}&appid={apiKey}&units=metric'

    icon_url_base='https://openweathermap.org/img/wn/[icon_url]@2x.png'

    # response=''
    # if not IsDev:
        
    #data = json.load(response.content)
    response = requests.get(urlForCall)
    print(response.content)
    result = response.json()
    print(response.json())
    weather = response.json()['weather']
    maindata= response.json()['main']
    #datetime.utcfromtimestamp(timeAsUnix).strftime('%Y-%m-%d %H:%M')
    timeOfMeasure =  datetime.utcfromtimestamp(int(response.json()['dt'])).strftime('%Y-%m-%d %H:%M')

    icon= str(weather[0]['icon'])

    icon_url =icon_url_base.replace('[icon_url]',icon)

    description =str(weather[0]['description'])

    sunRise = UnixTimeToStr(result['sys']['sunrise'])
    sunSet = UnixTimeToStr(result['sys']['sunset'])

    print(f'Sunrize: {sunRise}, Sunset : {sunSet}')

    # print(f'Temperature is: {temperature[0]:.2f}')
    temp = f'{maindata["temp"]:.1f}'
    temp_max = f'{maindata["temp_max"]:.1f}'
    temp_min = f'{maindata["temp_min"]:.1f}'
    feels_like = f'{maindata["feels_like"]:.1f}'

    weatherNamedTuple =json.loads(response.content, object_hook= getWeatherDataToTuple)

    #weather_main_data = WeatherMainData(feels_like,temp,temp_max,temp_min)
    weather_main_data = WeatherMainData(weatherNamedTuple.main.feels_like,weatherNamedTuple.main.temp,weatherNamedTuple.main.temp_max,weatherNamedTuple.main.temp_min)

    weather_desc= WeatherDesc(description,icon_url)

    WeatherFullData = WeatherData(weather_main_data,weather_desc)


    print(f'Temp: {temp} (feels like {feels_like}). Max Temp: {temp_max}, Min_temp :{temp_min}')

    print(f'IconUrl: {icon_url}')

    #dd ={}


    res =[{k, maindata[k]} for k in maindata]


    print(f'Time of measurment: {timeOfMeasure}')
    # for pr in res:
    #     print(type(pr))
    #     print(pr)

    return WeatherFullData

def get_4_day_weather_data():
    apiKey="c1f826dfb25ec6405ccfc5b443e34133"
    CityId =281184 # Jerusalem
    cityName ='jerusalem'
        
    urlForCall =f'https://api.openweathermap.org/data/2.5/forecast?q={cityName}&appid={apiKey}&units=metric'

    icon_url_base='https://openweathermap.org/img/wn/[icon_url]@2x.png'

    # response=''
    # if not IsDev:
        
    #data = json.load(response.content)
    response = requests.get(urlForCall)
    result = response.json()
    # print(result)

    

    # res = response.content

    

    # print(type(res))

    #weatherNamedTuple =json.loads(response.content, object_hook= getWeatherDataToTuple_1)
    #weatherNamedTuple =json.loads(response.content)

    # with open('4DayForCast_To_file.txt','w', encoding='utf-8') as f:
    #     json.dump(result, f, ensure_ascii=False, indent=4)

    # with open('data.json', 'w', encoding='utf-8') as f:
    #     json.dump(data, f, ensure_ascii=False, indent=4)
        

    #weatherJsonDesc = json.loads(response.content, object_hook=Weather4DayForcast)

    #w1 = Weather4DayForcast(**json.loads(response.content))
    w1 = Weather4DayForcast(json.loads(response.content))

    #AllTempsAndDates_v2 = [(datetime.utcfromtimestamp(int(x.dt)).strftime('%Y-%m-%d'),  x.main.temp) for x in weatherNamedTuple.list]
    AllTempsAndDates_v2 = [(datetime.utcfromtimestamp(int(x.dt)).strftime('%Y-%m-%d'),  x.weather_main.temp) for x in w1.ForcastList]
    #AllTempsAndDates_v2 =[(datetime.utcfromtimestamp(int(x['dt'])).strftime('%Y-%m-%d'),x['main']['temp']) for x in result['list']]
    MidDayWeather_Description =[(datetime.utcfromtimestamp(int(x.dt)).strftime('%Y-%m-%d'),datetime.utcfromtimestamp(int(x.dt)).strftime("%H:%M")
        ,x.weather_description.description,x.weather_description.icon) for x in w1.ForcastList 
        if datetime.utcfromtimestamp(int(x.dt)).strftime("%H:%M") =='12:00' 
        or datetime.utcfromtimestamp(int(x.dt)).strftime("%H:%M") =='00:00']
    


#print(AllTempsAndDates_v2)

    for tmp in AllTempsAndDates_v2:
        print(tmp)

    print('**** Now all Maxs and Mins')
    r1 = []
    for date, temp in groupby(AllTempsAndDates_v2, key= lambda k : k[0]):
        #maxDt = max(tmp[1] for tmp in temp)
        # Get weather condition in middle of day - For Max temp
        cond_desc = next((x for x in MidDayWeather_Description if x[0] == date and x[1]=='12:00'), None)
        w_icon=''
        if cond_desc is not None:
            w_icon = cond_desc[3]
        r1.append((date,max(tmp[1] for tmp in temp),w_icon))
        print(cond_desc)
        print(date)

    for date, temp in groupby(AllTempsAndDates_v2, key= lambda k : k[0]):
        # Get weather condition in middle of day - For Min temp
        cond_desc = next((x for x in MidDayWeather_Description if x[0] == date and x[1]=='00:00'), None)
        w_icon=''
        if cond_desc is not None:
            w_icon = cond_desc[3]
        r1.append((date,min(tmp[1] for tmp in temp),w_icon))

    r1.sort(key=lambda k: k[0])

    # rMins =[]
    # for date, temp in groupby(AllTempsAndDates_v2, key= lambda k : k[0]):
    #     rMins.append((date,min(tmp[1] for tmp in temp)))

    # for sky condition ******************
    #[(x.weather[0].description,x.dt_txt,datetime.utcfromtimestamp(int(x.dt)).strftime('%h-%m')) for x in allWeather.list]
    #print(r1)
    # for r in r1:
    #     print(r)

#    list_of_conds = [] # List[Daily_MinMax_Condition]
    group_list =[]
    for date, MinMaxTemps in groupby(r1, key=lambda x : x[0]):
        print(MinMaxTemps)
        #list_of_conds.append(Daily_MinMax_Condition(date,list(MinMaxTemps)))
        group_list.append(list(MinMaxTemps))
    
    daysToAddCounter = 1 # only add 4 days and not including today
    list_of_conds = [] # List[Daily_MinMax_Condition]
    for date, MinMaxTemps in groupby(r1, key=lambda x : x[0]):
        #print(MinMaxTemps)
        if datetime.strptime(date, '%Y-%m-%d') > datetime.today() and daysToAddCounter <= 4:
            list_of_conds.append(Daily_MinMax_Condition(date,list(MinMaxTemps)))
            daysToAddCounter+=1
        #group_list.append(list(MinMaxTemps))


    
    #new_list =[(x[0][0], x[0][1], [y[-1] for y in x]) for x in group_list]
    #daily_Min_Max =[(x[0][0], [y[-1] for y in x]) for x in group_list]
    #daily_Min_Max =[(datetime.strptime(x[0][0], '%Y-%m-%d').strftime('%a'), [y[-1] for y in x]) for x in group_list]
    
    daily_Min_Max = [(datetime.strptime(x[0][0], '%Y-%m-%d').strftime('%a'), [y for y in x]) #[y[-1] for y in x]) 
        for x in group_list if datetime.strptime(x[0][0], '%Y-%m-%d') > datetime.today()]
    
    # daily_Min_Max = [(datetime.strptime(x[0][0], '%Y-%m-%d').strftime('%a'), [y for y in x]) #[y[-1] for y in x]) 
    #     for x in list_of_conds if datetime.strptime(x[0][0], '%Y-%m-%d') > datetime.today()]

    #return daily_Min_Max
    return tuple((list_of_conds,daily_Min_Max))



def get_hebrew_date():
    
    dt_today = datetime.now().strftime("%Y-%m-%d")
    url =f'https://www.hebcal.com/converter?cfg=json&date={dt_today}&g2h=1&strict=1&gs=off'

    result = requests.get(url).json()

    hebrew_date = result['hebrew']
    hebrew_date_eng = f'{result["hd"]} of {result["hm"]}, {result["hy"]}'

    return (hebrew_date,hebrew_date_eng)


def get_zemanim(areaId):
    #datetime.strptime(chatzotNight, '%Y-%m-%dT%H:%M:%S%z')
    localAreaId=areaId
    if localAreaId is None:
        localAreaId=281184

    urlForZemanim =f'https://www.hebcal.com/zmanim?cfg=json&geonameid={localAreaId}'


    response = requests.get(urlForZemanim)
    #print(response.content)
    result = response.json()

    res = [{zemanimDictHeb[zemanKey]:zemanVal} for (zemanKey,zemanVal) in result['times'].items() if zemanKey in zmnToShow]
    res2 ={zemanimDictHeb[zemanKey]: zemanVal for zemanKey,zemanVal in result['times'].items() if zemanKey in zmnToShow}
    res3 ={zemanimDictHeb[zemanKey]: datetime.strptime(zemanVal, '%Y-%m-%dT%H:%M:%S%z').strftime("%H:%M")  for zemanKey,zemanVal in result['times'].items() if zemanKey in zmnToShow}
    return res3



def get_Inn_Rss():
    url_rss_heb ='https://rotter.net/rss/rotternews.xml' #'HTTPS://RSS.WALLA.CO.IL/FEED/22' # r'https://www.inn.co.il/Rss.aspx?act=.1'
    response = requests.get(url_rss_heb)

    with open('Rss_To_file.txt','w') as f:
        f.writelines(str(response.content))

    #result = response.json()

# class MainData:
#     def __init__(self,feelsLike,temp,max_temp,min_temp):
#         self.feelsLike,self.temp,self.max_temp,self.min_temp = feelsLike,temp,max_temp,min_temp
    
    
# class WeatherDesc:
#     def __init__(self,description,icon):
#         self.description,self.icon = description,icon

    

        

# class WeatherData:
#     def __init__(self,MainData,WeatherDesc):
#         self.main_data = MainData
#         self.Weather_description = WeatherDesc
    
#     def getMainData(self):
#         return self.main_data
    
#     def getWeatherDescription(self):
#         return self.Weather_description
    



@app.route('/')
def index():
    weather_data = get_weather_data()
    zemanim = get_zemanim(281184)
    _4DayForcast = get_4_day_weather_data()
    hebrew_dates = get_hebrew_date()
    #rss= get_Inn_Rss()
    #return render_template('index.html',data = weather_data, Zemanim = zemanim,_4DayForCast = _4DayForcast[0],_4day_type2 =_4DayForcast[1])
    return render_template('index.html',data = weather_data, Zemanim = zemanim,_4day_type2 =_4DayForcast[0], hebrew_dates = hebrew_dates)

if __name__ =="__main__":
    app.run(debug=True)