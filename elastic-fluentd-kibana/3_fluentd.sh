# Creating Config map
kubectl create -f efk-demo/fluentd-es-configmap.yaml

# Creating Fluent D Daemon Set
kubectl create -f efk-demo/fluentd-es-ds.yaml
