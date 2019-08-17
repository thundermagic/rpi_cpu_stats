#Prometheus exporter to export raspberry pi cpu stats. 
Exposes CPU temp and CPU max, min and current frequency

It read the stats from files in /sys directory. So this should work without any dependency on vcgencmd command and on 
distros which do not have vcgencmd installed by default

Docker images are available at: https://cloud.docker.com/repository/docker/thundermagic/rpi_cpu_stats

# Docker examples
Docker run <br>
`docker container run --name rpi_cpu_stats -v /sys:/sys:ro -p 9669:9669 -d thundermagic/rpi_cpu_stats:latest`

docker compose 
```
version: "2"
services:
  rpi_cpu_stats:
    image: thundermagic/rpi_cpu_stats:latest
    restart: always
    container_name: rpi_cpu_stats
    ports:
      - "9669:9669"
    environment: # Add the PUID and PGID of the user you want to run the container as
      - PUID=1001
      - PGID=1001
    volumes:
      - /sys:/sys
```
