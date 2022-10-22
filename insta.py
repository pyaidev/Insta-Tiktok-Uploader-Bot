import requests
import json

def instadownloader(link):
    url = "https://instagram-downloader-download-instagram-videos-stories.p.rapidapi.com/index"

    querystring = {"url": link}

    headers = {
        "X-RapidAPI-Key": "d179273d7emsh34fe0f35151a7a3p12379ejsnf9a526d26356",
        "X-RapidAPI-Host": "instagram-downloader-download-instagram-videos-stories.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    rest = json.loads(response.text)
    if 'error' in rest:
        return "error"
    else:
        dict = {}
        if rest['Type'] == 'Post-image':
            dict['type'] = 'image'
            dict['media'] = rest['media']
            return dict

        elif rest['Type'] == 'Post-Video':
            dict['type'] = 'video'
            dict['media'] = rest['media']
            return dict

        elif rest['Type'] == 'Carousel':
            dict['type'] = 'carousel'
            dict['media'] = rest['media']
            return dict
        else:
            return "Error"

