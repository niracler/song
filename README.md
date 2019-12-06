# song
歌曲接口

- [接口文档](https://documenter.getpostman.com/view/9556968/SW7gTQTL?version=latest)

## 更新数据库

```
python manage.py makemigrations
python manage.py migrate
```

## 如何团队项目保持同步(重要)

([附上IDEA可视化操作](https://blog.csdn.net/autfish/article/details/52513465))

第一次时需要,与团队仓库建立联系

```shell script
git remote add upstream https://github.com/dgut-group-ten/song.git
```

工作前后要运行这几条命令,和团队项目保持同步

```shell script
git fetch upstream
git merge upstream/master
```

## 参考资料

- [django解决跨域请求的问题](https://blog.csdn.net/apple9005/article/details/54427902)
- [Docker安装RabbitMQ（docker-compose.yml）](https://blog.csdn.net/Aria_Miazzy/article/details/89332658)