

class Node:
    def __init__(self, load_balancer):
        self.load_balancer = load_balancer
        self.ip = "192.168.0.10"
        while self.ip in load_balancer.nodes:
            ip = self.ip.split('.')
            new_ip = tuple(ip[:3] + [str(int(ip[-1])+1)])
            self.ip = "%s.%s.%s.%s" % new_ip
        load_balancer.nodes[self.ip] = self
