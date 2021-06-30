from diagrams import Diagram
from diagrams.k8s.network import Ingress,Service
from diagrams.k8s.compute import Deployment,Pod,ReplicaSet


with Diagram("K8s",show=True,direction="TB"):
    net = Ingress("example.com") >> Service("svc")
    net >> Deployment("backend") >> ReplicaSet("rs") >> [Pod("pod1"),
                               Pod("pod2"),
                               Pod("pod3") ]