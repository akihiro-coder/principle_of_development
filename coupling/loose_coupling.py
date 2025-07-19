# 疎結合のい解決策 疎けつごうでは、　インターフェース（抽象化）を定義して、クラス間の依存関係をゆるくします。

from abc import ABC, abstractmethod


# 抽象インターフェースを定義
class MailServerInterface(ABC):

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def send_mail(self, to, subject, body):
        pass


# 具体的な実装1
class SMTPServer(MailServerInterface):

    def __init__(self, host, port):
        self.host = host
        self.port = port

    def connect(self):
        print(f"SMTP接続", f"{self.host}:{self.port}")

    def send_mail(self, to, subject, body):
        print(f"SMTP送信: {to} - {subject}")
        print(f"本文: {body}")


# 具体的な実装2
class SendGridServer(MailServerInterface):

    def __init__(self, api_key):
        self.api_key = api_key

    def connect(self):
        print("SendGrid API接続")

    def send_mail(self, to, subject, body):
        print(f"SendGrid送信: {to} - {subject}")
        print(f"本文: {body}")


# 疎結合なEmailSenderクラス
class EmailSender:

    def __init__(self, mail_server: MailServerInterface):
        # インターフェースに依存
        self.mail_server = mail_server

    def send_notification(self, user_email, message):
        self.mail_server.connect()
        self.mail_server.send_mail(user_email, "通知", message)


if __name__ == "__main__":
    # SMTPServerを使ったEmailSenderのインスタンス化
    smtp_server = SMTPServer("smtp.example.com", 587)
    smtp_email_sender = EmailSender(mail_server=smtp_server)
    smtp_email_sender.send_notification("example@gmail.com", "これはSMTPのテストメールです。")
    # SendGridServerを使ったEmailSenderのインスタンス化
    sendgrid_server = SendGridServer("sendgrid_api_key")
    sendgrid_email_sender = EmailSender(mail_server=sendgrid_server)
    sendgrid_email_sender.send_notification("example@gmail.com", "これはSendGridのテストメールです。")




"""
このコードの利点
- 実装の変更が他のクラスに影響しない。
- テスト時にモックオブジェクトを簡単に注入可能
- 新しい実装を追加しても、EmailSenderのコードを変更する必要がない。
"""
