from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
import dotenv

dotenv.read_dotenv('.env')

# 获取当前文件夹名，即为该Django的项目名
project_name = 'core'
project_settings = '%s.settings' % project_name

# 设置环境变量
os.environ.setdefault('DJANGO_SETTINGS_MODULE', project_settings)

# 实例化Celery
app = Celery(project_name)

# 使用Django的settings文件配置celery
app.config_from_object('django.conf:settings', namespace='CELERY')

# Celery加载所有注册的应用
app.autodiscover_tasks(('apps.song',), force=True)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
