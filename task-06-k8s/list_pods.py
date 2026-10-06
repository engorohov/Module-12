from kubernetes import client, config

config.load_kube_config()
v1 = client.CoreV1Api()

pods = v1.list_pod_for_all_namespaces(watch=False)

print(f"{'NAMESPACE':<20} {'NAME':<50} {'STATUS':<12}")
print("-" * 84)
for p in pods.items:
    print(f"{p.metadata.namespace:<20} {p.metadata.name:<50} {p.status.phase:<12}")