# name = "Иван"
# age = 25
# is_devops = True
# salary = 150_000.50
# print(f"{name}, {age} лет, доход: {salary} руб")
# print(type(name), type(age), type(is_devops), type(salary))

# for i in range(1, 31):
#     if i % 15 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)

# servers = ["web-1", "web-2", "db-1", "cache-1", "web-3"]

# print(servers[0])
# print(servers[-1])
# print(servers[1:4])
# print([s for s in servers if s.startswith("web")])
# print(len(servers))

# servers.remove("cache-1")
# servers.append("monitor-1")
# print(servers)
# print ()
# server = { "name": "web-1", "ip": "10.0.0.1", "tags": ["frontend", "production"], "port": 80, }
# print(server["name"])
# print(server.get("nonexistent", "по умолчанию")) # без падения
# for key,value in server.items(): print(f"{key} = {value}")
# server["healthy"] = True
# print(server)
# print()
# def is_healthy(server: dict, threshold: int = 80) -> bool: 
# 	"""Проверка живости сервера по CPU."""
# 	cpu = server.get("cpu", 0)
# 	return cpu < threshold
# print(is_healthy({"cpu": 50}))
# print(is_healthy({"cpu": 95}))
# print(is_healthy({"cpu": 75}, threshold=70))
# print()
# def safe_divide(a: float, b: float) -> float:
#     try:
#         return a / b
#     except ZeroDivisionError:
#         print("Делить на ноль нельзя!")
#         return 0.0
#     except TypeError as e:
#         print(f"Неправильные типы: {e}")
#         return 0.0


# print(safe_divide(10, 2))
# print(safe_divide(10, 5))
# print(safe_divide(10, "abc"))
# print()
# def parse_server_line(line: str) -> dict:
# 	parts = line.strip().split()
# 	return { "name": parts[0], "ip": parts[1], "port": int(parts[2]), "status": parts[3], }
# print(parse_server_line("web-1 10.0.0.1 80 healthy"))
# print("==========================")
def show(*args, **kwargs): 
    print("args:", args) 
    print("kwargs:", kwargs) 
show(1, 2, 3, name="ivan", role="devops") # распаковка 
first, *rest = [1, 2, 3, 4, 5] 
print(first, rest) 
    
config = {"host": "localhost", "port": 8080} 

def connect(host: str, port: int):  
    print(f"connecting to {host}:{port}") 
    connect(**config)