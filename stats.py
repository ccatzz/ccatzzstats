import psutil
import requests, json
url = "http://192.168.0.101/zabpy/index.php"
agent = 5
###########################################

############################################
psutil.disk_usage('/')
disk = psutil.disk_usage('/')
disk_tot = ((disk.total) / 1024**3)
disk_free = ((disk.free) / 1024**3)
disk_use = ((disk.used) / 1024**3)
disk_perc = disk.percent
disk_perc = (int(disk_perc))

disk_tot = round(disk_tot, 2)
disk_free = round(disk_free, 2)
disk_use = round(disk_use, 2)


disk_tot = ("{} Gb".format(disk_tot))
disk_use = ("{} Gb".format(disk_use))
disk_free = ("{} Gb".format(disk_free))

#############################################
psutil.virtual_memory()
mem = psutil.virtual_memory()
ram_tot = ((mem.total) / 1024**3)
ram_used = ((mem.used) / 1024**3)
ram_free = ((mem.free) / 1024**3)

ram_tot = round(ram_tot, 2)
ram_used = round(ram_used, 2)
ram_free = round(ram_free, 2)

ram_tot = ("{} Gb".format(ram_tot))
ram_used = ("{} Gb".format(ram_used))
ram_free = ("{} Gb".format(ram_free))



#############################################
if disk_perc < 80:
	disk_status = 'OK'
elif disk_perc == 50:
	disk_status = 'WARNING'
else:
	disk_status = 'ALLERT'
	
#############################################
data = {'disk_tot': disk_tot, 'disk_free': disk_free, 'disk_use': disk_use, 'disk_perc': disk_perc, 'disk_status': disk_status, 'ram_tot': ram_tot, 'ram_used': ram_used, 'ram_free': ram_free}
params = {'id_agent': agent, 'log': json.dumps(data) }

r = requests.post(url = url, params = params)

print(r.text)



