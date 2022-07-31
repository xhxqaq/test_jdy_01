"""
step_01:
          1、把表单数据结构里面标签中文的值全部自动转换成英文，并存储在translate.txt中;
"""

import translators as ts
import time
import step_00


translate = True


if translate:
    word_dict = {
      '编号': 'part_num',
      '模具编号': 'part_num',
      '图片': 'image',
      '主管': 'director',
      '工单号': 'project_id',
      '附件': 'attachment',

    }

    """
     两种方法取出表单结构里的标签
     第一种：
 
    list_of_name = [i['label'] if 'items' not in i else [i['label']] + [j['label'] 
    for j in i['items']] 
    for i in form_structure['widgets']]
    result = list()
    for i in list_of_name:
        if type(i) is list:
            result.extend(i)
        else:
            result.append(i)
    print(result)
    """

    """
        第二种：
    """
    list_name = []
    for i in step_00.form_structure['widgets']:
        list_name.append(i['label'])
        if 'items' in i:
            for j in i['items']:
                list_name.append(j['label'])
    # print(list_name)

    for i in range(len(list_name)):
        print(i)
        if list_name[i] in word_dict:
            list_name[i] += ' ' + '= ' + word_dict[list_name[i]]    # +=  的意思是把右边的值与左边相加，并把值赋给左边
        else:
            list_name[i] += ' ' + '= ' + ts.baidu(list_name[i]).lower().replace(' ', '_')
            time.sleep(.1)

    def write(content: list):
        with open("./" + "translate.txt", "w", encoding='utf-8') as file:
            file.write('\n'.join(content))
    write(list_name)

