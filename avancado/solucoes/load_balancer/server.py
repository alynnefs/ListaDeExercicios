class Server:
    def __init__(self, umax: int):
        self.COST_PER_TICK = 1.00
        self.umax = umax
        self.users = list()
        self.total = int()

    def available(self) -> bool:
        """Verify the server availability."""
        return len(self.users) < self.umax

    def is_empty(self):
        return len(self.users) == 0

    def connect(self, user) -> None:
        """Connect a user/task on server."""
        self.users.append(user)

    def total_users(self) -> int:
        """Return the total user/tasks running."""
        return len(self.users)

    def execute_tasks(self):
        for user in self.users:
            user.execute()
        self.users = [u for u in self.users if not u.complete()]
