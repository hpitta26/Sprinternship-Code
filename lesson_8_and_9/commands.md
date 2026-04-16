
## Class Commnands - Lesson 8
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

docker compose up --build -d
```

## Lesson 9
```bash
docker run mongo # searches for image locally if DNE then pull image from docker-hub and run it as a container

docker exec -it <container-id> mongosh # open mongodb shell in container
# mongod --> mongodb daemon that runs service in the background

# run 'mongo' image as a container in detached mode with 2 volumes (mapped like host_path:container_path) with port mapping (-p)
docker run -d --name mongodb -p 27017:27017 -v mongodb_data:/data/db -v ./init-db.js:/docker-entrypoint-initdb.d/init-db.js:ro mongo

docker exec -it mongodb mongosh
```

## Additional Commands
```bash
docker stop <container-id> 

docker rm <container-id>

docker rmi <image-id>
```

## MongoSH Commands
```bash
use agentic_db # enter a specific db in mongosh

show tables # list tables in db

db.items.find().pretty()
```

