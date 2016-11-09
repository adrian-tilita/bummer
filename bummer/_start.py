from core.builder import build
import time

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
time.sleep(2)
monitor.stop()
time.sleep(10)
monitor.start()
time.sleep(10)
monitor.stop()
