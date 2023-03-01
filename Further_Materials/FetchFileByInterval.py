import sys
import time
import urllib.request

if len(sys.argv) != 1:
    print("Usage: python FetchFileByInterval "
          "<URL to fetch> <streaming directory> <number of seconds>", file=sys.stderr)
    exit(-1)

urlToFetch = "https://datosabiertos.malaga.eu/recursos/aparcamientos/ocupappublicosmun/ocupappublicosmun.csv"
streamingDirectory = "parking/"
#secondsToSleep = 60

while True:
    time_stamp = str(time.time())

    newFile = streamingDirectory + "/" + time_stamp + ".csv"
    urllib.request.urlretrieve(urlToFetch, newFile)

 #   time.sleep(secondsToSleep)
