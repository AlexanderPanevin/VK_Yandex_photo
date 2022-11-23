import time
import requests
from pprint import pprint
import pandas as pd

with open('token_vk.txt', 'r') as file_token_VK:
    token_vk = file_token_VK.read().strip()

class Vk_User:
    url = 'https://api.vk.com/method/'

    def __init__(self, token_vk, version):
        self.params = {
            'access_token': token_vk,
            'v': version }

    def save_photo(self, owner_id):
        url_photo = 'https://api.vk.com/method/photos.get'
        params = {
            'owner_id': '1...9',
            'album_id': 'profile',
            'rev': False,
            'extended': True,
            'photo_sizes': False,
            'access_token': token_vk,
            'count': 1,
            'v': '5.131' }
        res = requests.get(url_photo, params=params)
        res_str = res.json()
        # pprint(res_str)
        res_str_response = res_str['response']['items']
        pprint(res_str_response)
        list = []
        for item in res_str_response:
            list.append(item['sizes'][-1]['url'])
            # print(','.join(list))
            link = list[0]
            # print(link)
            global filename
            filename = ','.join(list).split('/', )[-1]
            foto_download = requests.get(link)
            print(','.join(list))
            with open(filename, 'wb') as file:
                file.write(foto_download.content)
        return res_str

if __name__ == '__main__':
    vk = Vk_User(token_vk, '5.131')
    vk.save_photo(1....9)

with open('token_ya.txt', 'r') as file_token_Ya:
    token_ya = file_token_Ya.read().strip()

class YandexDisk:
    def __init__(self, token_ya):
        self.token = token_ya

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)}

    def _get_upload_link(self, disk_file_path):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        # filename = disk_file_path.split('/', )[-1]
        print(filename)
        params = {'path':f"Загрузки Netology/{filename}", 'overwrite': 'true'}
        response = requests.get(upload_url, headers=headers, params=params)
        pprint(response.json())
        return response.json()

    def upload_file_to_disk(self, disk_file_path, filename):
        # href_json = self._get_upload_link(disk_file_path=disk_file_path)
        # href = href_json['href']
        href_json = self._get_upload_link(disk_file_path=disk_file_path)
        href = href_json.get('href','')
        response = requests.put(href, data=open(filename, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print('Загружено')
        else:
            return f"Ошибка: {response.status_code}"

if __name__ == '__main__':
    uploader = YandexDisk(token_ya)
    result = uploader.upload_file_to_disk("','.join(list)", filename)
    print(result)
