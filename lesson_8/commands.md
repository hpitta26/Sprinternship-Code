
## Class Commnands
```bash
docker build -t myapi . # build image based on Dockerfile

docker images # list images

docker run -it myapi bash # run a container based on the image and open a bash shell

exit # exit the container

docker run -it myapi

docker run -it -p 8080:80 myapi # map traffic on local port 8080 container port 80
# go to http://localhost:8080/ --> you will see {"message": "Hello, World!"}

docker run -it -d -p 8080:80 myapi # -d --> run detached (in the background)
docker run -it -d -p 8090:80 myapi # run a second instance of the container

docker run -it -d -p 9090:80 -v .:/app myapi # map volume (folder) . to /app inside the container
# this allows
docker restart <container-id> # changes to current folder auto reflects inside the container
```

## Additional Commands
```bash
docker stop <container-id> 

docker rm <container-id>

docker rmi <image-id>
```

