start = "25 17 * * *"
stop = "26 06 * * *"

file = open('another-autoscaler-start.conf',"w")
file.write(f'''
apiVersion: v1
kind: ConfigMap
metadata:
  name: cron
data:
  another-autoscaler/start-time: "{start}"
  another-autoscaler/stop-time: "{stop}"
  another-autoscaler/start-replicas: "2"
  another-autoscaler/stop-replicas: "0"
 ''')

file = open('deploy1.yaml',"w")
file.write(f'''
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx
  labels:
    app: nginx
  annotations:
   another-autoscaler/start-time: "{start}"
   another-autoscaler/stop-time: "{stop}"
   another-autoscaler/start-replicas: "2"
   another-autoscaler/stop-replicas: "0"
spec:
  replicas: 0
  selector:
    matchLabels:
       app: nginx
  template:
    metadata:
       labels:
         app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:latest
        ports:
        - containerPort: 80
        # env:
        #    - name: another-autoscaler-start
        #      valueFrom:
        #          configMapKeyRef:  
        #             name: cron
        #             key: another-autoscaler/start-time
        #    - name: another-autoscaler-stop
        #      valueFrom:
        #          configMapKeyRef:  
        #             name: cron
        #             key: another-autoscaler/stop-time
        #    - name: another-autoscaler-start
        #      valueFrom:
        #          configMapKeyRef:  
        #             name: cron
        #             key: another-autoscaler/start-replicas
        #    - name: another-autoscaler-stop
        #      valueFrom:
        #          configMapKeyRef:  
        #             name: cron
        #             key: another-autoscaler/stop-replicas

 ''')
