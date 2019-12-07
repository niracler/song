from __future__ import absolute_import, unicode_literals
from celery import shared_task
import datetime
import redis
from django.conf import settings
from song.models import Song, PlayList


@shared_task
def update_click():
    res_type = ['click_song', 'click_playlist']
    item_class = [get_song, get_playlist]
    for i in range(2):
        add_item_click(res_type[i], item_class[i])


def get_song(id):
    return Song.objects.get(sid=id)


def get_playlist(id):
    return PlayList.objects.get(lid=id)


def add_item_click(res_type, get_item):
    client = redis.from_url(settings.REDIS_HOST)

    # 拿出点击数
    keys = client.zrange(res_type, 1, -1)
    print('{}:拿出点击数条数: {}'.format(res_type, str(len(keys))))

    for key in keys:
        key = key.decode("utf-8")
        key = str(key)
        click = client.zscore(res_type, key)
        client.zrem(res_type, key)

        # 拿出对象,保存点击数
        try:
            item = get_item(int(key))
            item.click = item.click + int(click)
            item.save()
        except Exception as e:
            print("{}:{}的资源不存在, {},{}".format(res_type, key, click, str(e)))
    print('{}:添加点击数结束'.format(res_type))
