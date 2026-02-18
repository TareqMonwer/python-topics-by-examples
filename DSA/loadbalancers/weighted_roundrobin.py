class WeightedRoundRobin:
    def __init__(self, servers, weights):
        self.servers = servers
        self.weights = weights
        self.current_index = -1
        self.current_weight = 0

    def get_next_server(self):
        while True:
            self.current_index = (self.current_index + 1) % len(self.servers)
            if self.current_index == 0:
                self.current_weight -= 1
                if self.current_weight <= 0:
                    self.current_weight = max(self.weights)
            if self.weights[self.current_index] >= self.current_weight:
                return self.servers[self.current_index]


if __name__ == "__main__":
    servers = ["Server-1", "Server-2", "Server-3"]
    weights = [5, 1, 1]
    load_balancer = WeightedRoundRobin(servers, weights)

    for i in range(10):
        server = load_balancer.get_next_server()
        print(f"Hit-{i + 1}: {server}")