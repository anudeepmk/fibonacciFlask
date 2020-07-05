# Solution for the bash onliner mentioned [here](https://github.com/anudeepmk/fibonacciFlask/blob/master/history.txt)

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

If you also have kubernetes installed

```
anudeep@deeps:~/Documents/FlaskIntro/fibonaci_task$ kubectl create ns fibonaci
namespace/fibonaci created
anudeep@deeps:~/Documents/FlaskIntro/fibonaci_task$ kubectl apply -f fibdeploy.yaml --namespace=fibonaci
deployment.apps/fibonaci created
anudeep@deeps:~/Documents/FlaskIntro/fibonaci_task$ kubectl get deploy -n fibonaci
NAME       READY   UP-TO-DATE   AVAILABLE   AGE
fibonaci   1/1     1            1           60s
anudeep@deeps:~/Documents/FlaskIntro/fibonaci_task$ kubectl apply -f fibSvc.yaml --namespace=fibonaci 
service/fibonaci created
anudeep@deeps:~/Documents/FlaskIntro/fibonaci_task$ kubectl get ep fibonaci -n fibonaci 
NAME       ENDPOINTS          AGE
fibonaci   10.1.51.119:5000   26s
anudeep@deeps:~/Documents/FlaskIntro/fibonaci_task$ kubectl get svc -n fibonaci 
NAME       TYPE       CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
fibonaci   NodePort   10.152.183.152   <none>        5000:30425/TCP   44s
anudeep@deeps:~/Documents/FlaskIntro/fibonaci_task$ curl localhost:30425/fib/11
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
anudeep@deeps:~/Documents/FlaskIntro/fibonaci_task$ curl localhost:30425/fib/aa
{
  "errorCode": 404, 
  "message": "Invalid value entered"
}
anudeep@deeps:~/Documents/FlaskIntro/fibonaci_task$ 

```




## Tech stack used

* python 3.7
* Flask 1.1
* Docker 19.03
