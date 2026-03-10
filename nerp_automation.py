def scale_cluster() -> None:
    print("Scaling Kubernetes cluster")
    print("kubectl scale deployment api --replicas=6")


def no_action() -> None:
    print("No scaling needed")
