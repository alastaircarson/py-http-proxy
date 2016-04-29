# py-http-proxy
Fixing an issue when using the basic python http service to serve a local directory to the browser
An issue was found with using OpenLayers in that CORS was stopping requests to a remote GeoServer WFS service
By replacing the basic python http service with the code here, a basic http proxy was created (based on the target url), 
forwarding requests to the remote service

The url to the WFS was set up as wfs?http://service details
The proxy detected the wfs prefix and made a request to the remote service
Other requests were handled in the default manner
