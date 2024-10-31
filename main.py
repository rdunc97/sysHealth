import time
import psutil



#defining metrics
cpuUsage = psutil.cpu_percent(interval=1)
memUsage = psutil.virtual_memory()
disUsage = psutil.disk_usage('/')
netUsage = psutil.net_io_counters()




