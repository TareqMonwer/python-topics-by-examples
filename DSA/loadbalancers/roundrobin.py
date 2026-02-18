class RoundRobin:
    def __init__(self, servers: list[str]):
        self.servers = servers
        self.current_index = -1
    
    def get_next_server(self):
        self.current_index = (self.current_index + 1) % len(self.servers)
        return self.servers[self.current_index]


if __name__ == "__main__":
    servers = ["Server-1", "Server-2", "Server-3"]

    loadbalancer = RoundRobin(servers)

    for i in range(6):
        next_server = loadbalancer.get_next_server()
        print(next_server)
