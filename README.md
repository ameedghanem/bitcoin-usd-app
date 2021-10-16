# Bitcoin-USD-App
This is a simple web application which shows the user the price of the bitcoin in usd and the average price in the last 10 months.
It also shows a scatter plot to demonstrate the decreases/increases of the price through these 10 months. 

## Installation
```
$ git clone git@github.com:ameedghanem/bitcoin-usd-app.git
...
$ cd bitcoin-usd-app/
```

## Deployment
In order to run the app you need at first to build the docker image and run it.
Go then to http://127.0.0.1:5000/ to view the app.
Note: building the docker image takes some time
```
$  docker build -t bitcoin-app .
$  docker run -d -it -p5000:5000 bitcoin-app