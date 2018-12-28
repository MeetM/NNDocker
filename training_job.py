import os
import pymysql
import random
from utils import incr_completed_job_count

mysql_url = os.environ['RDS_URL']
user = os.environ['RDS_USERNAME']
passwd = os.environ['RDS_PASSWORD']
db = os.environ['RDS_DBNAME']
model_id = os.environ['MODEL_ID']
i = os.environ['MODEL_I']
j = os.environ['MODEL_J']
k = os.environ['MODEL_K']

conn = pymysql.connect(host=mysql_url, port=3306, user=user, passwd=passwd, db=db)
cur = conn.cursor()
cur.execute(
    'INSERT INTO model_params VALUES ('
    +str(model_id)+', '+str(i)+', '+str(j)+', '
    +str(k)+', '+str(random.random())+')'
)
conn.commit()

incr_completed_job_count(model_id)