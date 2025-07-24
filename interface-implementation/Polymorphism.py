from abc import ABC, abstractmethod


class NotificationSender(ABC):
    @abstractmethod
    def send(self, message: str, recipient: str) -> bool:
        pass


class EmailNotification(NotificationSender):
    def send(self, message: str, recipient: str) -> bool:
        print(f"Email送信: {message} to {recipient}")
        return True