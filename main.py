import typer, requests, json
app=typer.Typer()
def generate(place:str):
    url=f"https://geocode.maps.co/search?q={place}"
    response=requests.get(url)
    data=response.json()
    lat=data[0]["lat"]
    lon=data[0]["lon"]
    #Replace the below string with your API key.
    api="Your API key"
    url=f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api}"
    response=requests.get(url)
    data=response.json()
    description=data['weather'][0]['description']
    tempk=(data['main']['temp'])
    tempc=(tempk-273.15)
    tempf=str(tempc*9/5+32)[0:5]+' °F'
    tempk=str(tempk)[0:5]+" K"
    tempc=str(tempc)[0:5]+' °C'
    pressure=str(data['main']['pressure'])+" hPa"
    humidity=str(data['main']['humidity'])+" %"
    return [description,tempc,tempf,tempk,pressure,humidity]
@app.command()
def all(place:str):
    try:
        l=generate(place)
        print(f"Place       : {place}\nDescription : {l[0]}\nTemperature : {l[1]}\n              {l[2]}\n              {l[3]}\nPressure    : {l[4]}\nHumidity    : {l[5]}")
    except:
        print("Check the spelling of the place")
@app.command()
def description(place:str):
    try:
        print(f"Place       : {place}\nDescription : {generate(place)[0]}")
    except:
        print("Check the spelling of the place")
@app.command()
def temperature(place:str):
    try:
        l=generate(place)
        print(f"Place       : {place}\nTemperature : {l[1]}\n              {l[2]}\n              {l[3]}")
    except:
        print("Check the spelling of the place")
@app.command()
def pressure(place:str):
    try:
        print(f"Place    : {place}\nPressure : {generate(place)[4]}")
    except:
        print("Check the spelling of the place")
@app.command()
def humidity(place:str):
    try:
        print(f"Place    : {place}\nHumidity : {generate(place)[5]}")
    except:
        print("Check the spelling of the place")
if __name__=="__main__":
    app()
