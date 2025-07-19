# 密結合の例：EmailSenderがSMTPServerの具体的な実装に直接依存している

class SMTPServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def connect(self):
        print(f"SMTP接続, {self.host}:{self.port}")

    def send_mail(self, to, subject, body):
        print(f"SMTP送信: {to} - {subject}")


class EmailSender:
    def __init__(self,):
        # 具体的なSMTPServerクラスに直接依存している（密結合）
        self.server = SMTPServer("smtp.example.com", 587)

    def send_notification(self, user_email, message):
        self.server.connect()
        self.server.send_mail(user_email, "通知", message)


"""
このコードの問題点
- SMTPServerの仕様変更時に、EmailSenderも変更が必要になる。
- テスト時のモックが困難
- 他のメール送信(SendGrid, AWS SESなど)に切り替える場合、EmailSenderのコードも変更が必要になる。
"""