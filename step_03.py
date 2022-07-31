"""
    step_03:
            通过输入 app_id 和 entry_id ，读取出简道云里的数据
"""
import step_00
from read_data.read_jdy_data import Jdy_Read


jdy = Jdy_Read(step_00.appid, step_00.entryid)
# print(jdy.__dict__)
json = jdy.read()
models = list()
for i in json['data']:
    models.append(step_00.form_name(i))
