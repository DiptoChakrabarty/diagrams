from diagrams import Diagram,Cluster
from diagrams.k8s.network import Ingress,Service
from diagrams.k8s.compute import Deployment,Pod,ReplicaSet
from diagrams.k8s.clusterconfig import HPA


with Diagram("K8s",show=True,direction="TB"):
    net = Ingress("example.com") >> Service("svc")
    deploy = Deployment("backend")
    replicaset = ReplicaSet("rs")
    hpa = HPA("hpa")
    net >> deploy
    with Cluster("Pod Cluster"):
        pods = [Pod("pod1"),
        Pod("pod2"),
        Pod("pod3") ]
    deploy >> replicaset >> pods