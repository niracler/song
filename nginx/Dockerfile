FROM nginx
#对外暴露端口
RUN rm /etc/nginx/conf.d/default.conf
ADD nginx.conf  /etc/nginx/conf.d/
ADD ./cert/ /etc/nginx/cert/
RUN mkdir -p /usr/share/nginx/html/static
RUN mkdir -p /usr/share/nginx/html/media
RUN chmod -R 777 /usr/share/nginx/html/static
RUN chmod -R 777 /usr/share/nginx/html/media