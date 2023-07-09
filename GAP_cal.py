import math
import requests
import urllib3
urllib3.disable_warnings()

def sta_epi_angle(station):
    #計算震央及測站間的角度
    angle = math.atan2(epicenter[1] - station[1], epicenter[0] - station[0])
    angle = math.degrees(angle)
    if angle < 0:
        angle += 360
    return(angle)

ans = input("輸入測站資訊時使用檢知編號(1)或測站代碼(2)或座標(3)?:")
if ans == "1":
    print("使用編號")
elif ans == "2":
    print("使用代碼")
else:
    print("使用座標")

sta_list = requests.get("https://exptech.com.tw/api/v1/file/resource/station.json",verify=False).json()

alerttime = ""
if ans == "1":
    stations = []
    url = f"https://exptech.com.tw/api/v1/earthquake/trem-info/{input('檢知編號: ')}?key={input('金鑰(可不輸入): ')}"
    data = requests.get(url,verify=False).json()
    eqinfo = data["eq"]
    if eqinfo == {}:
        print("未找到震央資訊，請手動輸入震央座標")
        epicenter_longitude = float(input("震央經度: "))
        epicenter_latitude = float(input("震央緯度: "))
        epicenter = (epicenter_longitude, epicenter_latitude)
    else:
        epicenter = (eqinfo["lon"],eqinfo["lat"])
        alerttime = str(int(data["alert"]) - int(eqinfo["time"]))[:-3]
    for i in data["station"]:
        station = (round(sta_list[i["uuid"]]["Long"],2), round(sta_list[i["uuid"]]["Lat"],2))
        sta_angle = sta_epi_angle(station)
        stations.append((sta_angle))
    num_stations = len(data["station"])

else:
    #震央座標
    epicenter_longitude = float(input("震央經度: "))
    epicenter_latitude = float(input("震央緯度: "))
    epicenter = (epicenter_longitude, epicenter_latitude)

    #測站數量
    num_stations = int(input("測站數量: "))

    #各測站座標
    stations = []
    for i in range(num_stations):
        longitude = ""
        if ans == "2":
            sta_code = input("測站 {} 代碼: ".format(i+1))
            if sta_code not in sta_list:
                print("未找到測站，請輸入測站座標")
            else:
                longitude = round(sta_list[sta_code]["Long"],2)
                latitude = round(sta_list[sta_code]["Lat"],2)
        if longitude == "":
            longitude = float(input("測站 {} 經度: ".format(i+1)))
            latitude = float(input("測站 {} 緯度: ".format(i+1)))
        station = (longitude, latitude)
        sta_angle = sta_epi_angle(station)
        stations.append((sta_angle))

#依測站與震央的角度排序
stations = sorted(stations)
stations.append(stations[0] + 360)

#計算GAP
max_angle = 0
for i in range(num_stations):
    angle = stations[i+1] - stations[i]
    if angle > max_angle:
        max_angle = angle
        
print()
if alerttime != "":print(f"發報速度: 震後 {alerttime} 秒")
if num_stations == 2:
    #GAP明顯地震可只輸入2站資料
    print("GAP1:", round(max_angle,2))
    print("GAP2:", round(360-max_angle,2))
else:
    print("GAP:", round(max_angle,2))