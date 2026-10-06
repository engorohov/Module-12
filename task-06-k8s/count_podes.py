from kubernetes import client, config
from collections import Counter

config.load_kube_config()
v1 = client.CoreV1Api()

pods = v1.list_pod_for_all_namespaces()

counter = Counter(p.metadata.namespace for p in pods.items)

print("Поды по неймспейсам:")
for ns, count in counter.most_common():
    print(f"  {ns:<25} {count}")