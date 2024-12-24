FROM nginx:latest
WORKDIR /usr/share/nginx/html
COPY index.html .

RUN apt-get update
EXPOSE 8080
CMD ["nginx", "-g" "daemon off;"]