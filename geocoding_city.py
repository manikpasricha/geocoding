# import relevant lib
import pandas as pd    
import math

R = 6378.1 #Radius of the Earth

def my_grid(lat, lon, step_dis = 10.0, step_count=10):
    # DEFINING AN EMPTY DF
    df_append = pd.DataFrame([[lat, lon]])
    for bearing in [0, 180, 90, -90]:
    # bearing guidance -  # 90 = move right; -90 = move left;  0 = move up; 180 = move down
        for i in range(step_count):
    # loop through lat and long to create new lat and long at specified distances + store them in a data frame
            brng = math.radians(bearing)
            lat1 = math.radians(lat)
            lon1 = math.radians(lon)
            lat2 = math.asin( math.sin(lat1)*math.cos((i+1)*step_dis/R) + math.cos(lat1)*math.sin((i+1)*step_dis/R)*math.cos(brng))
            lon2 = lon1 + math.atan2(math.sin(brng)*math.sin((i+1)*step_dis/R)*math.cos(lat1), math.cos((i+1)*step_dis/R)-math.sin(lat1)*math.sin(lat2))
            lat2 = math.degrees(lat2)
            lon2 = math.degrees(lon2)
            df_append = df_append.append([[lat2, lon2]])
    df_append.columns = ["lat", "long"]
    return(df_append)

x = my_grid(lat = 28.579789,lon = 77.196710,step_dis = 4.0, step_count = 10)
print(x)



