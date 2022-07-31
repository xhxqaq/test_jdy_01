import step_00
import requests
jdy_api_key = 'E0qrsk1u33qo4sfedZIa2tZAJK2ufTp4'
headers = {"Authorization": "Bearer " + jdy_api_key}
url = "https://api.jiandaoyun.com/api/v4/app/{app_id}/entry/{entry_id}/data".format(app_id=step_00.appid, entry_id=step_00.entryid)
# print(url)
parameter = {'limit': 100}


class Jdy_Read:

    def __init__(self, app_id, entry_id) -> None:
        self.url = "https://api.jiandaoyun.com/api/v4/app/{app_id}/entry/{entry_id}/data"\
            .format(app_id=app_id, entry_id=entry_id)
        self.para = {'limit': 100}

    def read(self):
        response = requests.post(self.url, headers=headers)
        return response.json()

    def read_next(self, data_id):
        self.para['data_id'] = data_id
        response = requests.post(self.url, headers=headers, json=self.para)
        return response.json()


