from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB


with Diagram("Grouped Workers",show=True,direction="TB"):
    ELB("lb") >> [EC2("node1"),
                    EC2("node2"),
                    EC2("node3"),
                    EC2("node4"),
                    EC2("node5")] >> RDS("events")
