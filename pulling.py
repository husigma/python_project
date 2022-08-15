
from urllib.request import urlopen
import json
import pandas as pd
from pandas import json_normalize
import datetime


col = ('OBJECTID', 'TICKET_NUMBER', 'ISSUE_DATE', 'ISSUE_TIME',
       'ISSUING_AGENCY_CODE', 'ISSUING_AGENCY_NAME', 'ISSUING_AGENCY_SHORT',
       'VIOLATION_CODE', 'VIOLATION_PROC_DESC', 'LOCATION', 'PLATE_STATE',
       'VEHICLE_TYPE', 'MULTI_OWNER_NUMBER', 'DISPOSITION_CODE',
       'DISPOSITION_TYPE', 'DISPOSITION_DESC', 'DISPOSITION_DATE',
       'FINE_AMOUNT', 'TOTAL_PAID', 'PENALTY_1', 'PENALTY_2', 'PENALTY_3',
       'PENALTY_4', 'PENALTY_5', 'XCOORD', 'YCOORD', 'LATITUDE', 'LONGITUDE',
       'MAR_ID', 'GIS_LAST_MOD_DTTM')

def downny(year, month):
    url = 'https://maps2.dcgis.dc.gov/dcgis/rest/services/DCGIS_DATA/Violations_Parking_{}/MapServer/{}/query?where=1%3D1&outFields=*&outSR=4326&f=json'.format(year,month)
    response = urlopen(url)
    data_json = json.loads(response.read())
    df2 = json_normalize(data_json['features']) 
    df2.columns = [i.replace("attributes.", "") for i in df2.columns]
    df2["ISSUE_DATE"] = pd.to_datetime(df2["ISSUE_DATE"], unit='ms')
    return(df2)


all_res = []


d = datetime.datetime.now().strftime("%m")
d = int(d)
d = d-2
d

for i in range(2015,2023):
    for j in range(0,12):
        try:
            data = downny(year= i, month= j)
            all_res.append(data)
            
        except Exception:
            pass

df_res = pd.DataFrame(data=None, columns= col)
df_res = pd.concat(all_res)
df_res.head()

df_res.shape

df_res.ISSUE_DATE.unique()

df_res['n'] = 1
df_res['month'] = pd.DatetimeIndex(df_res['ISSUE_DATE']).month
df_res['year'] = pd.DatetimeIndex(df_res['ISSUE_DATE']).year
df_res['combo'] = str(df_res['month'] )+ '-' + str(df_res['year'])



