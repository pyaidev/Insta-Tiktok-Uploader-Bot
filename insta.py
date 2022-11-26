import requests
import json

def instadownloader(link):
    url = "https://instagram-downloader-download-instagram-videos-stories.p.rapidapi.com/index"

    querystring = {"url": link}

    headers = {
	"content-type": "application/x-www-form-urlencoded",
	"X-RapidAPI-Key": "2507542715msh65a0a76b179a083p15606fjsn211bd5cbad0e",
	"X-RapidAPI-Host": "instagram-video-or-images-downloader.p.rapidapi.com"
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

