# Creating Config map
kubectl delete -f efk-demo/fluentd-es-configmap.yaml

# Creating Fluent D Daemon Set
kubectl delete -f efk-demo/fluentd-es-ds.yaml
