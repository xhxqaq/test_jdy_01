"""
    step_04:
            1、连接数据库
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import json
db_url = 'localhost'
db_name = 'health'
db_user = 'root'
db_password = '123456'
engine = create_engine(f'mysql+pymysql://{db_user}:{db_password}@{db_url}/{db_name}?charset=utf8mb4',
                       echo=False, convert_unicode=True,
                       json_serializer=lambda obj: json.dumps(obj, ensure_ascii=False))

Session = sessionmaker(bind=engine)

Base = declarative_base()
engine = create_engine