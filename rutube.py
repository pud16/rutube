import requests
import json
import csv
import datetime
def parsing_rutube(fname):
    avtor=fname
    link_author= f"https://rutube.ru/api/video/person/{avtor}"
    json_data = requests.get(link_author).json()
    result=json_data['results']
    result_list=result[2]
    list_autor=result_list['author']
    autor_name=list_autor['name']
    autor_id=list_autor['id']
    video=result[0]
    link_video=video['id']
    link2=f"https://rutube.ru/api/video/{link_video}"
    json_feed_sub = requests.get(link2).json()
    autor_sub=json_feed_sub['feed_subscribers_count']
    today_date = datetime.date.today().isoformat() # дата
    with open(autor_name, "a", newline="") as file:
        writer = csv.writer(file)
        autor_xml_data=[today_date ,autor_name, autor_id ,autor_sub]
        writer.writerow(autor_xml_data)
rutube_autor_id=[26772571,24517039] # список ID
for item in rutube_autor_id:
    parsing_rutube(item)