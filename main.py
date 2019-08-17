from prometheus_client import start_http_server, Gauge
from time import sleep
from subprocess import run as run_command


def read_cpu_temp():
    """ Reads cpu temp from /sys/class/thermal/thermal_zone0/temp """

    cpu_temp = run_command(['cat', '/sys/class/thermal/thermal_zone0/temp'], capture_output=True, text=True).stdout
    return int(cpu_temp)/1000


def read_cpu_freq():
    """
    Reads cpu freq in from /sys/devices/system/cpu/cpufreq/policy0/. Freq are in hertz
    max cpu freq file: /sys/devices/system/cpu/cpufreq/policy0/cpuinfo_max_freq
    min cpu freq file: /sys/devices/system/cpu/cpufreq/policy0/cpuinfo_min_freq
    current cpu freq file: /sys/devices/system/cpu/cpufreq/policy0/scaling_cur_freq
    """

    max_freq = run_command(['cat', '/sys/devices/system/cpu/cpufreq/policy0/cpuinfo_max_freq'],
                           capture_output=True, text=True).stdout
    min_freq = run_command(['cat', '/sys/devices/system/cpu/cpufreq/policy0/cpuinfo_min_freq'],
                           capture_output=True, text=True).stdout
    cur_freq = run_command(['cat', '/sys/devices/system/cpu/cpufreq/policy0/scaling_cur_freq'],
                           capture_output=True, text=True).stdout
    return max_freq, min_freq, cur_freq


if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(9669)
    # Create metrics
    cpu_temp = Gauge('cpu_temp', 'CPU temperate')
    cpu_freq = Gauge('cpu_freq', 'CPU frequencies', labelnames=['freq'])
    while True:
        cpu_temp.set(read_cpu_temp())
        max_freq, min_freq, cur_freq = read_cpu_freq()
        cpu_freq.labels(freq='max').set(max_freq)
        cpu_freq.labels(freq='min').set(min_freq)
        cpu_freq.labels(freq='cur').set(cur_freq)
        sleep(2)