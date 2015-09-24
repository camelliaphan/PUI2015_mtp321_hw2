import json
import sys
import csv
import urllib2

#Local test 
#jsonFile = open(sys.argv[1], 'r')
#metadata = json.load(jsonFile)
#buses = metadata['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

#with open(sys.argv[2], 'wb') as csvfile:
#	writer = csv.writer(csvfile)
#	writer.writerow(['Latitude', 'Longitude', 'StopName', 'StopStatus'])
	
#	for bus in buses: 
#		lat = bus['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
#		lon = bus['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
#		name = bus['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName']
#		status = bus['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']
#		row = [lat, lon, name, status]
#		writer.writerow(row)
				
#		print '%s, %s, %s, %s' % (lat, lon, name, status)

url = 'http://api.prod.obanyc.com/api/siri/vehicle-%%20monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s' % (sys.argv[1], sys.argv[2])
request = urllib2.urlopen(url) 
metadata = json.load(request)
buses = metadata['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

with open(sys.argv[3], 'wb') as csvfile:
	writer = csv.writer(csvfile)
	writer.writerow(['Latitude', 'Longitude', 'StopName', 'StopStatus'])
	
	for bus in buses: 
		lat = bus['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
		lon = bus['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
		if bus['MonitoredVehicleJourney']['OnwardCalls']=={}:
			name = 'N/A'
			status = 'N/A'
		else:
			name = bus['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName']
			status = bus['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']
		row = [lat, lon, name, status]
		writer.writerow(row)
				
		print 'Latitude, Longitude, Stop Name, Stop Status \n %s, %s, %s, %s' % (lat, lon, name, status)

