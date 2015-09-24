import json
import sys
import urllib2

#local test
#jsonFile = open(sys.argv[1], 'r')
#metadata = json.load(jsonFile)
#buses = metadata['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

#print "The number of active buses is: %s " % len(buses)

#count = 0
#for bus in buses:
#	lat = bus['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
#	lon = bus['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
#	count += 1
#	print "Bus %s is at latitude %s and longitude %s." % (count, lat, lon)

url = 'http://api.prod.obanyc.com/api/siri/vehicle-%%20monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s' % (sys.argv[1], sys.argv[2])
request = urllib2.urlopen(url) 
metadata = json.load(request)

buses = metadata['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

print "The number of active buses is: %s " % len(buses)

count = 0
for bus in buses:
	lat = bus['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
	lon = bus['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
	count += 1
	print "Bus %s is at latitude %s and longitude %s." % (count, lat, lon)
