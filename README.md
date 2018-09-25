# aks-logging

This contains the sourcecodes for 3 types of logging which are easy to implement when using Azure Kubernetes Service.

- The default out of the box logging, using log analytics and needs no additional configuration. Usage of this is shown in my youtube channel. No sourcecode for this.
- EFK stack; stands for ElesticSearch FluentD and Kibana and is excellent for centralized application logging. Demo is using the Game of Thrones voting app, results are directly visible in Kibana.
- Prometheus; execellent timelaps data solution for near realtime logging of infrastructural events

## Steps

- Create your ResourceGroup: az group create -n aks-demo-rg -l westeurope
- Create your AKS cluster with the following command:  az aks create --node-vm-size Standard_D2s_v3 -g aks-demo-rg -n aks-demo-cluster ( we need machines with more than 4GB mem )
- az aks get-credentials -g aks-demo-rg -n aks-demo-cluster
- git clone this repo: git clone https://github.com/chrisvugrinec/aks-logging.git
- cd elastic-fluentd-kibana
- 1_labelNodes.sh
- 2_elasticSearch.sh
- 3_fluentd.sh
- 4_kibana.sh
- Switch to namespace used in scripts efk_demo:  kubectl config use-context aks-demo-cluster  --namespace efk-demo
- Please be patient when accessing kibinan...initialization can takeup 15 minutes or so...  once you changed the context and namepspace, do: kubectl get svc and access the public ip for accessing Kibana
- cd ../got-webapp
- 1_redis.sh
- 2_helloworld.sh
- Check the public IP for the got webapp: kubectl get svc --namespace got-webapp