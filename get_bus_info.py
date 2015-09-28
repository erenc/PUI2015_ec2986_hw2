#import required libraries
import sys
import requests
import csv

#define the key and busline arguments for the url
key = sys.argv[1]
busline = sys.argv[2]
url ='http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s' %(key, busline)
request = requests.get(url)
data = request.json()

#create 3 arg that calling from the bash
with open(sys.argv[3], 'wb') as csvFile:
    writer = csv.writer(csvFile)
    headers = ['Latitude', 'Longitude', 'StopName', 'StopStatus']
    writer.writerow(headers)
#defie variable for eachbus count
    eachbus = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]["VehicleActivity"]
    number = len(eachbus)
#print the bus line and active buses
    print "Bus Line:", busline
    print "Number of Active Buses", number

#create varaible buscount for each bus and iterate in the for loop, 
#get the location of each active buses and stop 

    buscount = 0

    for i in range(number):
        buscount +=1
        location = eachbus[i]["MonitoredVehicleJourney"]["VehicleLocation"]
        la = location[u"Latitude"]
        lo = location[u"Longitude"]
        onward = eachbus[i]["MonitoredVehicleJourney"]["OnwardCalls"]["OnwardCall"][0]
        status = onward["Extensions"]["Distances"][u"PresentableDistance"]
        stop = onward[u"StopPointName"]
    
#test print the results
        print "Bus{} is at latitude {} and longitute {} {} {}" .format(buscount, la, lo, stop, status)

#print to the csv file   
        print "%s,%s:%s, %s" % (la, lo, stop, status)
        writer.writerow([la, lo, stop, status])
