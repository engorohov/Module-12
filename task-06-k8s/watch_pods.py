from kubernetes import client, config, watch

config.load_kube_config()
v1 = client.CoreV1Api()

w = watch.Watch()
print("Слушаю изменения подов (Ctrl+C для выхода)...")

for event in w.stream(v1.list_pod_for_all_namespaces, timeout_seconds=60):
    p = event["object"]
    print(f"[{event['type']:<8}] {p.metadata.namespace}/{p.metadata.name} → {p.status.phase}")