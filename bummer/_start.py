from core.builder import build

config = {
    "monitors": {
        "system": {
            "filters": {
                "net_io": True,
                "memory": True,
                "cpu": True
            }
        },
        "memcache": {
            "config": {
                "hostname": '127.0.0.1',
                "port": 11211
            }
        }
    }
}

monitor = build(config)
monitor.start()
