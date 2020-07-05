# fibonacciFlask

This project has a webservice created with Flask on Python

## Usage

Ensure you have docker installed

```
anudeep@mylocal:~$ docker run -d -p 5000:5000 anudeepmk/fibflask:1 
a629f1970fb21109743383e4b963c86a0a7b2de96e8267e255cfc3caa91d15e2
anudeep@mylocal:~$ docker ps
CONTAINER ID        IMAGE                  COMMAND             CREATED             STATUS              PORTS                    NAMES
a629f1970fb2        anudeepmk/fibflask:1   "python main.py"    26 seconds ago      Up 4 seconds        0.0.0.0:5000->5000/tcp   infallible_swartz
anudeep@mylocal:~$ curl localhost:5000/fib/11
[
  [
    3, 
    3, 
    5
  ], 
  [
    2, 
    2, 
    2, 
    5
  ], 
  [
    2, 
    3, 
    3, 
    3
  ], 
  [
    2, 
    2, 
    2, 
    2, 
    3
  ]
]
anudeep@deeps:~$ curl localhost:5000/fib/-1
{
  "errorCode": 404, 
  "message": "Invalid value entered"
}
anudeep@mylocal:~$ curl localhost:5000/fib/aa
{
  "errorCode": 404, 
  "message": "Invalid value entered"
}
anudeep@mylocal:~$
```


## Tech stack used

* python 3.7
* Flask 1.1
* Docker 19.03
