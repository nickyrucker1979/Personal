import requests
import pandas as pd
import json

key = ''
email = ''

url_todos = 'https://www.mtbproject.com/data/get-to-dos?email='+email+'&key='+key
url_route_info = 'https://www.mtbproject.com/data/get-trails-by-id?key='+key+'&ids='

def get_dataframe(passed_url, dataframe_element):
    get_active_url = requests.request("GET", passed_url)
    json_details = json.loads(get_active_url.text)[dataframe_element]
    print(json_details)
    df = pd.DataFrame(json_details)
    return df

if __name__ == '__main__':

    mtb_project_todos_ids = get_dataframe(url_todos, 'toDos')
    # mtb_project_todos_ids = mtb_project_todos_ids

    print(mtb_project_todos_ids)
    idx = 0

    for index, row in mtb_project_todos_ids.iterrows():
        id = str(row[0])
        # id = ''
        url_route_info_w_id = url_route_info + str(id)

        print(url_route_info_w_id)
        try:
            mtb_project_get_route_data = get_dataframe(url_route_info_w_id, 'trails')
            # print(list(mtn_project_get_route_data))
            # print(mtn_project_get_route_data)
    #
            mtb_project_route_df = mtb_project_get_route_data[[
                'location',
                'name',
                'difficulty',
                'latitude',
                'longitude',
                'type',
                'length',
                'url'
            ]]

            print(mtb_project_route_df)
            if idx<1:
                mtb_project_route_df.to_csv('mtb_projects_to_dos.csv', index=False)
                idx+=1
            else:
                mtb_project_route_df.to_csv('mtb_projects_to_dos.csv', mode='a', header=False, index=False)
        except:
            pass
