#import required libraries
import sys
import requests

#define the key and busline arguments for the url
key = sys.argv[1]
busline = sys.argv[2]
url ='http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s' %(key, busline)
request = requests.get(url)
data = request.json()

#create variable for each data define the columns in json
eachbus = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]["VehicleActivity"]
number = len(eachbus)

#print bosline and active buses

print "Bus Line:", busline
print "Number of Active Buses", number

#count the each bus in the file and iterate, get the location of the buses as latitute and longigtute
buscount = 0
for i in range(number):
    buscount +=1
    location = eachbus[i]["MonitoredVehicleJourney"]["VehicleLocation"]
    la = location[u"Latitude"]
    lo = location[u"Longitude"]
    
#print the number of buses and their locations    
    print "Bus{} is at latitude{} and longitute {}" .format(buscount, la, lo)
