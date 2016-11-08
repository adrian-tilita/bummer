from monitor.builder import build

config = {

    "system": {
        "filters": {
            "net_io": True,
            "memory": True,
            "cpu": True
        }
    }
}

monitor = build(config)
it = 0
while it < 1:
    print(monitor.start())
    it += 1