from celery import Celery

app = Celery('tasks', broker="amqp://guest@localhost//")

@app.task
def calc_rgb_avg(pic_url):
    # return calculated luminance value based by weighted average of
    # RGB of every pixel
    return 0
