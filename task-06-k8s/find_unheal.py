from kubernetes import client, config

config.load_kube_config()
v1 = client.CoreV1Api()

pods = v1.list_pod_for_all_namespaces()

problems = [
    p for p in pods.items
    if p.status.phase not in ("Running", "Succeeded")
]

if not problems:
    print("✅ Все поды Running")
else:
    print(f"❌ Проблемных подов: {len(problems)}")
    for p in problems:
        for cs in (p.status.container_statuses or []):
            if not cs.ready:
                reason = ""
                if cs.state.waiting:
                    reason = cs.state.waiting.reason
                elif cs.state.terminated:
                    reason = cs.state.terminated.reason
                print(f"  {p.metadata.namespace}/{p.metadata.name} → {cs.name}: {reason}")