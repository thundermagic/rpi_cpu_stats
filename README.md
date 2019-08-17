#Prometheus exporter to export raspberry pi cpu stats. 
Exposes CPU temp and CPU max, min and current frequency

It read the stats from files in /sys directory. So this should work without any dependency on vcgencmd command and on 
distros which do not have vcgencmd installed by default

Docker images are available at: https://cloud.docker.com/repository/docker/thundermagic/rpi_cpu_stats

`docker container run --name rpi_cpu_stats -v /sys:/sys -p 9669:9669 -d thundermagic/rpi_cpu_stats:latest`
