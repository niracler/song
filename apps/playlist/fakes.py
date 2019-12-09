import random
import requests
from faker import Faker
from song.models import PlayList

fake = Faker("zh_CN")


def fake_comment(count=50):
    """生成假文章"""

    max_id = 87000
    for i in range(count):
        try:
            list_lid = PlayList.objects.all().values_list('lid', flat=True)
            list_token = [
                'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOjI1LCJ3ZWIiOiJncm91cHRlbiIsIm5hbWUiOiJyb290IiwiaXNBZG1pbiI6ZmFsc2UsImV4cCI6MTU3NjQ2MzA5NiwiaWF0IjoxNTc1ODU4Mjk2fQ.mCHX-qINZBns4eW_wOoUPrCMlVX4t8Sxay42TfWeMqw',
                'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOjEsIndlYiI6Imdyb3VwdGVuIiwibmFtZSI6Im5pcmFjbGVyNCIsImlzQWRtaW4iOmZhbHNlLCJleHAiOjE1NzY0NjM4MDIsImlhdCI6MTU3NTg1OTAwMn0.f7O498v6PVbSBEsjHxIVlKXv5cclfJklzvbzhM_t1OY',
                'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOjI3LCJ3ZWIiOiJncm91cHRlbiIsIm5hbWUiOiJyb290MTIzIiwiaXNBZG1pbiI6ZmFsc2UsImV4cCI6MTU3NjQ2Mzg5MiwiaWF0IjoxNTc1ODU5MDkyfQ.pdslkhn3tNTMgs8yhjOWadD-deedKoBY1R0X3DBb5hQ',
                'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOjI4LCJ3ZWIiOiJncm91cHRlbiIsIm5hbWUiOiIxMTExIiwiaXNBZG1pbiI6ZmFsc2UsImV4cCI6MTU3NjQ2MzkxOSwiaWF0IjoxNTc1ODU5MTE5fQ.964lrvQBYjYq2MVXbDufDAcA74g2qjziT46d6VfHg3M',
                'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOjI5LCJ3ZWIiOiJncm91cHRlbiIsIm5hbWUiOiIxMSIsImlzQWRtaW4iOmZhbHNlLCJleHAiOjE1NzY0NjM5NTMsImlhdCI6MTU3NTg1OTE1M30.OUvBTm8TUM2jl8fPrzVeBL9Trff02Zxji6l5vMdxTBE',
                'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOjMxLCJ3ZWIiOiJncm91cHRlbiIsIm5hbWUiOiIxMTExMiIsImlzQWRtaW4iOmZhbHNlLCJleHAiOjE1NzY0NjM5NzIsImlhdCI6MTU3NTg1OTE3Mn0.Ns_15ARbv3mtbAr9F6e-tBjEXHqsk-oCqAtiC7EDPrc',
                'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOjM0LCJ3ZWIiOiJncm91cHRlbiIsIm5hbWUiOiJhYWJiIiwiaXNBZG1pbiI6ZmFsc2UsImV4cCI6MTU3NjQ2Mzk5MywiaWF0IjoxNTc1ODU5MTkzfQ.xTcM2fFoUgdMo1LeWMNV6yrCGaAiqAhWz_ZodqcAfM4',
                'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOjM1LCJ3ZWIiOiJncm91cHRlbiIsIm5hbWUiOiJhYWJiY2MiLCJpc0FkbWluIjpmYWxzZSwiZXhwIjoxNTc2NDY0MDEyLCJpYXQiOjE1NzU4NTkyMTJ9.nDUApnGvqh_CIY7JxMQhPX8jEcN46srsehXCps8nH98',
                'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOjM2LCJ3ZWIiOiJncm91cHRlbiIsIm5hbWUiOiJjYyIsImlzQWRtaW4iOmZhbHNlLCJleHAiOjE1NzY0NjQwMjksImlhdCI6MTU3NTg1OTIyOX0.4VA3bcQ5q5eT4wEvh5XCoXnNRhFuUW1auc-mSXCJ0QU',
            ]

            headers = {
                'token': random.choice(list_token)
            }

            data = {
                'content': fake.text(random.randint(7, 140)),
                'type': 1,
                'resourceId': random.choice(list_lid),
                'repliedCommentId': random.choice(
                    [random.randint(7, max_id), random.randint(7, max_id//2), None, None]),
            }
            # print(data['repliedCommentId'])

            url = 'https://music-01.niracler.com:8001/comment'

            r = requests.post(url, headers=headers, data=data)
            if r.status_code != 201:
                print(r.text)
            max_id += 1

        except Exception as e:
            print(e)
