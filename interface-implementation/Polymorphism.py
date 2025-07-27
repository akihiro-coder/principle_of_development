# 密結合な通知システム - インターフェース分離なし

class EmailNotification:
    def send_email(self, message: str, recipient: str) -> bool:
        print(f"Email送信: {message} to {recipient}")
        return True


class SMSNotification:
    def send_sms(self, message: str, recipient: str) -> bool:
        print(f"SMS送信: {message} to {recipient}")
        return True


class SlackNotification:
    def send_slack(self, message: str, recipient: str) -> bool:
        print(f"Slack送信: {message} to {recipient}")
        return True


# 密結合なクライアントコード - 具体的な実装に依存
class NotificationService:
    def __init__(self, notification_type: str):
        self.notification_type = notification_type

        # 具体的なクラスに直接依存
        if notification_type == "email":
            self.sender = EmailNotification()
        elif notification_type == "sms":
            self.sender = SMSNotification()
        elif notification_type == "slack":
            self.sender = SlackNotification()
        else:
            raise ValueError(f"未対応の通知タイプ: {notification_type}")

    def notify_user(self, user_id: str, message: str):
        # 各実装の異なるメソッド名に対応するため分岐が必要
        if self.notification_type == "email":
            return self.sender.send_email(message, user_id)
        elif self.notification_type == "sms":
            return self.sender.send_sms(message, user_id)
        elif self.notification_type == "slack":
            return self.sender.send_slack(message, user_id)

    def send_bulk_notification(self, users: list, message: str):
        """複数ユーザーへの一括通知 - 新しい通知タイプを追加するたびに修正が必要"""
        results = []
        for user in users:
            if self.notification_type == "email":
                results.append(self.sender.send_email(message, user))
            elif self.notification_type == "sms":
                results.append(self.sender.send_sms(message, user))
            elif self.notification_type == "slack":
                results.append(self.sender.send_slack(message, user))
        return results


# クライアントコードの実行例
if __name__ == "__main__":
    # メリット: シンプルで直感的
    email_service = NotificationService("email")
    sms_service = NotificationService("sms")
    slack_service = NotificationService("slack")

    message = "こんにちは！「システムメンテナンスのお知らせ」です。"

    email_service.notify_user("user@example.com", message)
    sms_service.notify_user("+1234567890", message)
    slack_service.notify_user("@username", message)

    # デメリットの例: 新しい通知タイプを追加する場合
    # 1. 新しいクラスを作成
    # 2. NotificationServiceのコンストラクタを修正
    # 3. notify_userメソッドを修正
    # 4. send_bulk_notificationメソッドも修正
    # → 既存コードの多数箇所を変更する必要がある
