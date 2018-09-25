# Creating Kibana deploy
kubectl create -f efk-demo/kibana-deployment.yaml

# Creating Kibana Service (LB == public loadbalancer)
kubectl create -f efk-demo/kibana-service.yaml
