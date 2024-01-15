class RecentCounter:

    def __init__(self):
        self.queue = deque()

    def ping(self, t: int) -> int:
        self.queue.append(t)

        time = t - 3000

        # 큐의 맨 앞 요소가 현재 시간에서 3000 밀리초 이전의 시간보다 작을 때까지 제거합니다.
        while self.queue[0] < time:
            self.queue.popleft()
        
        return len(self.queue)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)