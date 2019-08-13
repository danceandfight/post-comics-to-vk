import os
import requests
import random
from dotenv import load_dotenv
from urllib.parse import urlparse

def get_random_comics_params():
    current_comics_url = 'http://xkcd.com/info.0.json'
    response = requests.get(current_comics_url)
    comics_total_number = response.json()['num']
    random_comics_number = random.randrange(1, comics_total_number + 1)
    random_comics_url = 'http://xkcd.com/{}/info.0.json'.format(random_comics_number)
    response = requests.get(random_comics_url)
    if not response.ok or 'error' in response:
        raise requests.exceptions.HTTPError(response['error'])
    response_data = response.json()
    comics_url = response_data['img']
    comment = response_data['alt']
    url_path = urlparse(comics_url)
    filename = os.path.basename(url_path.path)
    return comics_url, comment, filename
  
def download_comics(url, filename):
    response = requests.get(url)
    #response.raise_for_status()
    if not response.ok or 'error' in response:
        raise requests.exceptions.HTTPError(response['error'])
    #os.makedirs(os.path.abspath('.'), exist_ok = True)
    os.makedirs(os.path.abspath('temp_pics'), exist_ok = True)
    file_with_path = 'temp_pics/{}'.format(filename)
    with open(file_with_path, 'wb') as file:
        file.write(response.content)

def upload_comics(url, comment, filename):
    XKCD_CLIENT_ID = os.getenv('XKCD_CLIENT_ID')
    VK_IMPLICIT_FLOW_TOKEN = os.getenv('VK_IMPLICIT_FLOW_TOKEN')
    XKCD_GROUP_ID = os.getenv('XKCD_GROUP_ID')
    api_version = '5.101'
    payload = {'access_token': VK_IMPLICIT_FLOW_TOKEN, 'v': api_version, 'group_id': XKCD_CLIENT_ID}
    wall_upload_server_url = 'https://api.vk.com/method/photos.getWallUploadServer'
    response = requests.get(wall_upload_server_url, params=payload)
    if not response.ok or 'error' in response:
        raise requests.exceptions.HTTPError(response['error'])
    response_data = response.json()
    upload_url = response_data['response']['upload_url']
    album_id = response_data['response']['album_id']
    user_id = response_data['response']['user_id']
    photo_with_path = 'temp_pics/{}'.format(filename)
    with open(photo_with_path, 'rb') as photo:
    #photo = open(photo_with_path, 'rb')
        response = requests.post(upload_url, files={'photo': photo})
        if not response.ok or 'error' in response:
            raise requests.exceptions.HTTPError(response['error'])
        response_data = response.json()
        #photo.close()

    data = {'server': response_data['server'], 
          'photo': response_data['photo'], 
          'hash': response_data['hash'],
          'group_id': XKCD_CLIENT_ID,
          'access_token': VK_IMPLICIT_FLOW_TOKEN,
          'v': api_version}
    album_url = 'https://api.vk.com/method/photos.saveWallPhoto'
    response = requests.post(album_url, data=data)
    if not response.ok or 'error' in response:
        raise requests.exceptions.HTTPError(response['error'])
    response_album_url = response.json()['response'][0]
    media_id = response_album_url['id']
    owner_id = response_album_url['owner_id']
    post_by_group = 1               # post in vk will be created with group account
    type_of_media = 'photo'
    attachments = '{}{}_{}'.format(type_of_media, owner_id, media_id)
    params = {'owner_id': XKCD_GROUP_ID, 
            'from_group': post_by_group, 
            'attachments': attachments, 
            'message': comment, 
            'access_token': VK_IMPLICIT_FLOW_TOKEN, 
            'v': api_version}
    wall_post_url = 'https://api.vk.com/method/wall.post'
    response = requests.post(wall_post_url, data=params)
    if not response.ok or 'error' in response:
        raise requests.exceptions.HTTPError(response['error'])
    #os.remove(photo_with_path)

def main():
    load_dotenv()
    url, comment, filename = get_random_comics_params()
    download_comics(url, filename)
    upload_comics(url, comment, filename)
    photo_with_path = 'temp_pics/{}'.format(filename)
    os.remove(photo_with_path)

if __name__ == '__main__':
    main()