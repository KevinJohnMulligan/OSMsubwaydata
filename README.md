# OSMsubwaydata

Background: Jason Stine, the developer of Lost LaoWai mobile map application (which is aimed at helping foreigners navigate in China) uses Google maps to display the map tiles in his app. Most information including subway stations is shown, however many of the subway lines are not shown on Google Maps in China (data loss has occurred due to Google no longer supporting the region).

This project makes use of Open Street Maps (OSM) data via the Python API to retrieve the station and line names as well as the coordinates of the missing subway lines. The project also corrects for "the China GPS shift" as Google maps already corrects for it but OSM data does not causing a misalignment.
