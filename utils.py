import redis
import os
import json

def _get_db():
	redis_url = os.environ['REDIS_URL']
	return redis.StrictRedis(host=redis_url, port=6379, db=0)

def store_best_params(model_id, param_dic):
	db = _get_db()
	db.set("BEST_PARAMS_" + str(model_id), json.dumps(param_dic))

def incr_completed_job_count(model_id):
	db = _get_db()
	db.incr("JOB_COMPLETED_COUNT_" + model_id)