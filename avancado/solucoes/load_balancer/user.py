class User:
    def __init__(self, ttask: int):
        self.ttask = ttask

    def execute(self) -> None:
        """Execute a tick from ttask."""
        self.ttask -= 1

    def complete(self) -> bool:
        """Verify if the task still have ttask."""
        return self.ttask <= 0
