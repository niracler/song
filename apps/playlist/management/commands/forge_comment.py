import os
import click
import django
import datetime
from django.core.management.base import BaseCommand

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'display.settings')
django.setup()


class Command(BaseCommand):
    help = '用于生成假评论数据的命令'

    def add_arguments(self, parser):
        parser.add_argument('--command_num', default=50, type=int, help='Quantity of command, default is 50')

    def handle(self, *args, **options):
        from playlist.fakes import fake_comment

        start_time = datetime.datetime.now()  # 放在程序开始处
        click.echo('Generating the command...')
        fake_comment(options['command_num'])

        end_time = datetime.datetime.now()  # 放在程序结尾处
        interval = (end_time - start_time).seconds  # 以秒的形式
        final_time = interval / 60.0  # 转换成分钟
        click.echo('final_name:\t' + str(final_time))