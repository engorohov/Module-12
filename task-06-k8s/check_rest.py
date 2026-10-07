import sys
from kubernetes import client, config


def check_restarts(namespace: str, pod_name: str) -> None:
    config.load_kube_config()
    v1 = client.CoreV1Api()

    pod = v1.read_namespaced_pod(name=pod_name, namespace=namespace)

    print(f"Под: {namespace}/{pod_name}")
    print(f"Фаза: {pod.status.phase}")
    print()

    total = 0
    for cs in pod.status.container_statuses or []:
        restarts = cs.restart_count
        total += restarts
        print(f"  {cs.name:<30} рестартов: {restarts}")

    print()
    print(f"Всего рестартов: {total}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: check_restarts.py <namespace> <pod>")
        sys.exit(1)
    check_restarts(sys.argv[1], sys.argv[2])
