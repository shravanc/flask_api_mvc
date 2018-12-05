from app import celery

@celery.task
def new_task():
    print('---Task-Called---')
