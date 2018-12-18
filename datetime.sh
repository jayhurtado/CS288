#!/bin/sh
while true; do
dateNY=$(date +%Y-%m-%d-%H-%M-%S-NY)
dateCA=$(date +%Y-%m-%d-%H-%M-%S-CA)
dateIL=$(date +%Y-%m-%d-%H-%M-%S-IL)
dateTX=$(date +%Y-%m-%d-%H-%M-%S-TX)
dateAZ=$(date +%Y-%m-%d-%H-%M-%S-AZ)
datePA=$(date +%Y-%m-%d-%H-%M-%S-PA)
dateFL=$(date +%Y-%m-%d-%H-%M-%S-FL)

curl -o $dateNY.html https://forecast-v3.weather.gov/point/40.78,-73.97?view=plain
java -jar tagsoup-1.2.1.jar --files $dateNY.html

curl -o $dateCA.html https://forecast-v3.weather.gov/point/34.02,-118.45?view=plain
java -jar tagsoup-1.2.1.jar --files $dateCA.html

curl -o $dateIL.html https://forecast-v3.weather.gov/point/41.78,-87.76?view=plain
java -jar tagsoup-1.2.1.jar --files $dateIL.html

curl -o $dateTX.html https://forecast-v3.weather.gov/point/29.64,-95.28?view=plain
java -jar tagsoup-1.2.1.jar --files $dateTX.html

curl -o $dateAZ.html https://forecast-v3.weather.gov/point/33.69,-112.07?view=plain
java -jar tagsoup-1.2.1.jar --files $dateAZ.html

curl -o $datePA.html https://forecast-v3.weather.gov/point/40.08,-75.01?view=plain
java -jar tagsoup-1.2.1.jar --files $datePA.html

curl -o $dateFL.html https://forecast-v3.weather.gov/point/30.23,-81.67?view=plain
java -jar tagsoup-1.2.1.jar --files $dateFL.html

ColumnTitle="state,city,weather,temperature,humidity,pressure"
echo $ColumnTitle>new_Csv.csv

python3 parsexhtml.py $dateNY.xhtml
python3 parsexhtml.py $dateCA.xhtml
python3 parsexhtml.py $dateIL.xhtml
python3 parsexhtml.py $dateTX.xhtml
python3 parsexhtml.py $dateAZ.xhtml
python3 parsexhtml.py $datePA.xhtml
python3 parsexhtml.py $dateFL.xhtml


  sleep $[60 * 60]
done

