import math

def sta_epi_angle(station):
    #計算震央及測站間的角度
    angle = math.atan2(epicenter[1] - station[1], epicenter[0] - station[0])
    angle = math.degrees(angle)
    if angle < 0:
        angle += 360
    return(angle)

#測站數量
num_stations = int(input("測站數量: "))

#震央座標
epicenter_longitude = float(input("震央經度: "))
epicenter_latitude = float(input("震央緯度: "))
epicenter = (epicenter_longitude, epicenter_latitude)

#各測站座標
stations = []
for i in range(num_stations):
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

if num_stations == 2:
    #GAP明顯地震可只輸入2站資料
    print("\nGAP1:", round(max_angle,2))
    print("GAP2:", 360-round(max_angle,2))
else:
    print("\nGAP:", round(max_angle,2))