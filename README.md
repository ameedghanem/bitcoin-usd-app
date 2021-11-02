# Bitcoin-USD-App
This is a simple web application which shows the user the price of the bitcoin in usd and the average price in the last 10 months.
It also shows a scatter plot to demonstrate the decreases/increases of the price through these 10 months.

## Prerequisties
  jenkins (for using the jenkins file)\
  docker (for building image and running)

## Installation
```
$ git clone git@github.com:ameedghanem/bitcoin-usd-app.git
  ...
$ cd bitcoin-usd-app/
``` 

## Deployment
In order to run the app you need at first to build the docker image and run it.
Go then to http://127.0.0.1:5000/ to view the app.<br />
Note: building the docker image takes some time
```
$ docker build -t bitcoin-app .
$ docker run -d -it -p5000:5000 bitcoin-app
```

## About the Jenkins file
#### This jenkins file creates a job that pushes the created image to your Dockerhub account
  - Make sure you add the user jenkins to the group docker by running the following command:
    ```
    $ sudo usermod -a -G docker jenkins
    ```
  - Restart jenkins by running the following command:
    ```
    $ sudo /etc/init.d/jenkins restart
    ```
  - Most importantly, make sure that you have saved the docker hub credentials in jenkins. See [this link](https://dzone.com/articles/building-docker-images-to-docker-hub-using-jenkins)
