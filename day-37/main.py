import requests
from datetime import datetime

USERNAME="rithishgouda"
TOKEN="ywg37grwurff"
NAME_OF_GRAPH="graph1"

pixela_endpoint="https://pixe.la/v1/users"

user_params={
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}

# response=requests.post(url=pixela_endpoint,json=user_params)
# print(response.text)
graph_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs"
graph_params={
    "id":NAME_OF_GRAPH,
    "name":"number of hours",
    "unit":"Hours",
    "type":"int",
    "color":"ichou"
}
headers={
    "X-USER-TOKEN":TOKEN
}
# response=requests.post(url=graph_endpoint,json=graph_params,headers=headers)
# print(response.text)
pixel_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/{NAME_OF_GRAPH}"

today=datetime.now()
DATE=today.strftime("%Y%m%d")
pixel_params={
    "date":DATE,
    "quantity":input("How many hours did you study"),
}
response=requests.post(url=pixel_endpoint,json=pixel_params,headers=headers)
print(response.text)
update_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/{NAME_OF_GRAPH}/{DATE}"
update_params={
    "quantity":"5",
}
# response=requests.put(url=update_endpoint,json=update_params,headers=headers)
# print(response.text)
delete_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/{NAME_OF_GRAPH}/{DATE}"
# response=requests.delete(url=delete_endpoint,headers=headers)
# print(response.text)