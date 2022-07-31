"""
    step_00:
        1、在这里插入表的表单数据结构
        2、命名一个表的名字
"""


form_structure = {
  "op": "form_update",
  "data": {
    "appId": "5d0c1bf52966bd4c03cd20b4",
    "entryId": "5fbf3f05651d460006e680e0",
    "name": "质量改进系统",
    "createTime": "2018-01-01T10:10:10.000Z"
  },
  "widgets": [
    {
      "label": "日期",
      "name": "date",
      "type": "datetime"
    },
    {
      "label": "工单号",
      "name": "project_id",
      "type": "sn"
    },
    {
      "label": "编号",
      "name": "part_num",
      "type": "text"
    },
    {
      "label": "模具规格",
      "name": "mould_specification",
      "type": "combo"
    },
    {
      "label": "模头类型",
      "name": "mould_type",
      "type": "combo"
    },
    {
      "label": "工艺难度",
      "name": "technology_difficulty",
      "type": "combo"
    },
    {
      "label": "发现来源",
      "name": "find_source",
      "type": "combo"
    },
    {
      "label": "异常部件",
      "name": "abnormal_component",
      "type": "combo"
    },
    {
      "label": "异常部位",
      "name": "abnormal_part",
      "type": "combocheck"
    },
    {
      "label": "异常类别",
      "name": "abnormal_type",
      "type": "combo"
    },
    {
      "label": "异常项目",
      "name": "abnormal_project",
      "type": "combo"
    },
    {
      "label": "异常描述",
      "name": "abnormal_description",
      "type": "textarea"
    },
    {
      "label": "附件",
      "name": "attachment",
      "type": "upload"
    },
    {
      "label": "备注",
      "name": "remarks",
      "type": "text"
    },
    {
      "label": "质检员",
      "name": "quality_inspector",
      "type": "combo"
    },
    {
      "label": "返工时间确认",
      "name": "confirm_rework_time",
      "type": "datetime"
    },
    {
      "label": "责任部门",
      "name": "responsibility_department",
      "type": "combo"
    },
    {
      "label": "主管",
      "name": "director",
      "type": "user"
    },
    {
      "label": "责任环节",
      "name": "responsibility_link",
      "type": "combo"
    },
    {
      "label": "责任车间",
      "name": "responsibility_workshop",
      "type": "combo"
    },
    {
      "label": "组长",
      "name": "group_leader",
      "type": "text"
    },
    {
      "label": "责任人",
      "name": "duty_person",
      "type": "text"
    },
    {
      "label": "评估日期",
      "name": "valuation_date",
      "type": "datetime"
    },
    {
      "label": "异常等级",
      "name": "abnormal_level",
      "type": "radiogroup"
    },
    {
      "label": "损失情况",
      "name": "damage_situation",
      "type": "subform",
      "items": [
        {
          "label": "直接损失（元）",
          "name": "damage_situation_direct_loss",
          "type": "number"
        },
        {
          "label": "间接损失（元）",
          "name": "damage_situation_indirect_loss",
          "type": "number"
        },
        {
          "label": "损失总额",
          "name": "total_loss",
          "type": "number"
        }
      ]
    },
    {
      "label": "扣款明细",
      "name": "penalty_detail",
      "type": "subform",
      "items": [
        {
          "label": "扣款总额（元）",
          "name": "total_penalty",
          "type": "number"
        },
        {
          "label": "组长扣款（元）",
          "name": "group_leader_penalty",
          "type": "number"
        },
        {
          "label": "主管扣款（元）",
          "name": "director_penalty",
          "type": "number"
        },
        {
          "label": "责任人扣款（元）",
          "name": "duty_person_penalty",
          "type": "number"
        }
      ]
    },
    {
      "label": "直接损失（元）",
      "name": "direct_loss",
      "type": "number"
    },
    {
      "label": "间接损失（元）",
      "name": "indirect_loss",
      "type": "number"
    },
    {
      "label": "根本原因",
      "name": "fundamental_cause",
      "type": "textarea"
    },
    {
      "label": "临时措施",
      "name": "temporary_measures",
      "type": "textarea"
    },
    {
      "label": "预防措施",
      "name": "precaution",
      "type": "textarea"
    },
    {
      "label": "图片",
      "name": "picture1",
      "type": "image"
    },
    {
      "label": "预计实施时间",
      "name": "expected_implement_time",
      "type": "datetime"
    },
    {
      "label": "评审意见",
      "name": "review_opinions",
      "type": "textarea"
    },
    {
      "label": "图片",
      "name": "picture2",
      "type": "image"
    },
    {
      "label": "实际实施时间",
      "name": "practical_implement_time",
      "type": "datetime"
    },
    {
      "label": "验证结果",
      "name": "verify_result",
      "type": "radiogroup"
    },
    {
      "label": "有效性确认",
      "name": "notarize_validation",
      "type": "textarea"
    },
    {
      "label": "图片",
      "name": "picture3",
      "type": "image"
    },
    {
      "label": "验证结果",
      "name": "verify_result1",
      "type": "radiogroup"
    }
  ]
}
form_name = 'quality_improvement'


appid = form_structure['data']['appId']
# print(appid)
entryid = form_structure['data']['entryId']
# print(entryid)
