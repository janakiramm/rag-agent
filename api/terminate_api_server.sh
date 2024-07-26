docker-compose down
docker-compose stop
docker volume rm $(docker volume ls -q)
