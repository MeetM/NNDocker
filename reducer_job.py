import os
import pymysql
from utils import store_best_params
from utils import incr_completed_job_count

mysql_url = os.environ['RDS_URL']
mysql_user = os.environ['RDS_USERNAME']
mysql_passwd = os.environ['RDS_PASSWORD']
mysql_db = os.environ['RDS_DBNAME']
model_id = os.environ['MODEL_ID']

conn = pymysql.connect(host=mysql_url, port=3306, user=mysql_user, passwd=mysql_passwd, db=mysql_db)
cur = conn.cursor(pymysql.cursors.DictCursor)
sql = 'SELECT * FROM model_params WHERE id = '+str(model_id)+';'
cur.execute(sql)
rows = cur.fetchall()
best_params = {
        "i" : None,
        "j" : None,
        "k" : None,
        "acc" : -1
    }
for row in rows:
    if best_params["acc"] < float(row["acc"]):
        best_params["acc"] = float(row["acc"])
        best_params["i"] = float(row["i"])
        best_params["j"] = float(row["j"])
        best_params["k"] = float(row["k"])

store_best_params(model_id, best_params)
incr_completed_job_count(model_id)