# Get ticks in Mountain Project

import requests
import pandas as pd
import json

url_todos = 'https://www.mountainproject.com/data/get-ticks?email=nickyrucker@hotmail.com&key=7069372-b40d69409c81b222cd5d2c61e3a8cdcd'
url_route_info = 'https://www.mountainproject.com/data/get-routes?key=7069372-b40d69409c81b222cd5d2c61e3a8cdcd&routeIds='

def get_dataframe(passed_url, dataframe_element):
    get_active_url = requests.request("GET", passed_url)
    json_details = json.loads(get_active_url.text)[dataframe_element]
    print(json_details)
    df = pd.DataFrame(json_details)
    return df

if __name__ == '__main__':

    mtn_project_ticks = get_dataframe(url_todos, 'ticks')
    mtn_project_tick_ids = mtn_project_ticks['routeId']
    print(list(mtn_project_ticks))

    idx = 0

    for i in mtn_project_tick_ids.iteritems():
        id = str(i[1])
        # id = '110037673'
        url_route_info_w_id = url_route_info + str(id)

        print(url_route_info_w_id)
        try:
            mtn_project_get_route_data = get_dataframe(url_route_info_w_id, 'routes')
            # print(list(mtn_project_get_route_data))
            # print(mtn_project_get_route_data)

            mtn_project_route_df = mtn_project_get_route_data[[
                'id',
                'name',
                'latitude',
                'longitude',
                'location',
                'type',
                'stars',
                'pitches',
                'url'
            ]]

            print(mtn_project_route_df)
            if idx<1:
                mtn_project_route_df.to_csv('mtn_projects_ticks.csv', index=False)
                idx+=1
            else:
                mtn_project_route_df.to_csv('mtn_projects_ticks.csv', mode='a', header=False, index=False)
        except:
            pass
