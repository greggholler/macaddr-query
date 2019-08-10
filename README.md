# macaddr-query
Queries macaddress.io, and returns the Company Name associated with the OUI

# To build
```
docker build -t <somename> .
```

# To run
```
docker run -e API_KEY="<apikey>" <somename> <mac address>
```

Note: mac addresses must be of the form 00:11:22:33:44:55