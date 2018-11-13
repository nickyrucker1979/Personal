import requests
import pandas as pd
import json

email = ''
key = ''

url_todos = 'https://www.mountainproject.com/data/get-to-dos?email='+email+'&key='+key
url_route_info = 'https://www.mountainproject.com/data/get-routes?key='+key+'&routeIds='

def get_dataframe(passed_url, dataframe_element):
    get_active_url = requests.request("GET", passed_url)
    json_details = json.loads(get_active_url.text)[dataframe_element]
    print(json_details)
    df = pd.DataFrame(json_details)
    return df

if __name__ == '__main__':

    mtn_project_todos_ids = get_dataframe(url_todos, 'toDos')
    mtn_project_todos_ids = mtn_project_todos_ids

    print(mtn_project_todos_ids)
    idx = 0

    for index, row in mtn_project_todos_ids.iterrows():
        id = str(row[0])
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
                mtn_project_route_df.to_csv('mtn_projects_to_dos.csv', index=False)
                idx+=1
            else:
                mtn_project_route_df.to_csv('mtn_projects_to_dos.csv', mode='a', header=False, index=False)
        except:
            pass
