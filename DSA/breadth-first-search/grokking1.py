from collections import deque


def is_mango_seller(person):
    return person[-1] == "m"


def breadth_first_search(search_queue):
    searched = list()
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if is_mango_seller(person):
                print(person, "is a mangoo seller")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False


if __name__ == "__main__":
    graph = dict()
    graph["tareq"] = ["alice", "bob", "claire"]
    graph["alice"] = ["peggie"]
    graph["bob"] = ["anuj", "peggie"]
    graph["claire"] = ["thom", "jonny"]
    graph["peggie"] = []
    graph["anuj"] = []
    graph["thom"] = []
    graph["jonny"] = []

    search_queue = deque()
    search_queue += graph["tareq"]

    print(breadth_first_search(search_queue))
