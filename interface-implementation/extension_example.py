"""
新機能追加時の違いを実際に示す例
Push通知機能を追加する場合
"""

from abc import ABC, abstractmethod

print("=" * 60)
print("新機能追加時の違い - Push通知追加例")
print("=" * 60)

# ========== 密結合実装に新機能追加 ==========
class TightCoupledNotificationService:
    """密結合実装 - 新機能追加時に既存コードを大幅修正"""
    
    def __init__(self, notification_type: str):
        self.notification_type = notification_type
        
        # 新しいPush通知を追加するために既存コードを修正
        if notification_type == "email":
            self.sender = EmailSender()
        elif notification_type == "sms":
            self.sender = SMSSender()
        elif notification_type == "push":  # ← 新規追加
            self.sender = PushSender()  # ← 新規追加
        else:
            raise ValueError(f"未対応の通知タイプ: {notification_type}")

    def send_notification(self, message: str, recipient: str):
        # 新しいPush通知のために既存メソッドを修正
        if self.notification_type == "email":
            return self.sender.send_email(message, recipient)
        elif self.notification_type == "sms":
            return self.sender.send_sms(message, recipient)
        elif self.notification_type == "push":  # ← 新規追加
            return self.sender.send_push(message, recipient)  # ← 新規追加

    def send_with_priority(self, message: str, recipient: str, priority: str):
        # このメソッドも修正が必要
        if self.notification_type == "email":
            return self.sender.send_email(f"[{priority}] {message}", recipient)
        elif self.notification_type == "sms":
            return self.sender.send_sms(f"[{priority}] {message}", recipient)
        elif self.notification_type == "push":  # ← 新規追加
            return self.sender.send_push(f"[{priority}] {message}", recipient)  # ← 新規追加

class EmailSender:
    def send_email(self, message: str, recipient: str):
        return f"Email送信: {message} to {recipient}"

class SMSSender:
    def send_sms(self, message: str, recipient: str):
        return f"SMS送信: {message} to {recipient}"

class PushSender:  # ← 新規クラス
    def send_push(self, message: str, recipient: str):
        return f"Push通知送信: {message} to {recipient}"

# ========== 疎結合実装に新機能追加 ==========
class NotificationSender(ABC):
    """既存のインターフェース - 変更不要"""
    @abstractmethod
    def send(self, message: str, recipient: str) -> str:
        pass

class LooseCoupledEmailSender(NotificationSender):
    """既存実装 - 変更不要"""
    def send(self, message: str, recipient: str) -> str:
        return f"Email送信: {message} to {recipient}"

class LooseCoupledSMSSender(NotificationSender):
    """既存実装 - 変更不要"""
    def send(self, message: str, recipient: str) -> str:
        return f"SMS送信: {message} to {recipient}"

class LooseCoupledPushSender(NotificationSender):  # ← 新規クラスのみ追加
    """新機能 - インターフェースを実装するだけ"""
    def send(self, message: str, recipient: str) -> str:
        return f"Push通知送信: {message} to {recipient}"

class LooseCoupledNotificationService:
    """既存サービス - 全く変更不要"""
    def __init__(self, sender: NotificationSender):
        self.sender = sender
    
    def send_notification(self, message: str, recipient: str):
        return self.sender.send(message, recipient)
    
    def send_with_priority(self, message: str, recipient: str, priority: str):
        return self.sender.send(f"[{priority}] {message}", recipient)

# ========== 実行と比較 ==========
if __name__ == "__main__":
    print("\n--- 密結合実装での新機能追加 ---")
    print("✗ TightCoupledNotificationServiceのコンストラクタを修正")
    print("✗ send_notificationメソッドを修正")
    print("✗ send_with_priorityメソッドを修正")
    print("✗ 他にも類似メソッドがあれば全て修正が必要")
    print("→ 既存コードの複数箇所を変更するためバグ混入リスク大")
    
    tight_push_service = TightCoupledNotificationService("push")
    print(tight_push_service.send_notification("新機能テスト", "device123"))
    
    print("\n--- 疎結合実装での新機能追加 ---")
    print("✓ 新しいクラス（LooseCoupledPushSender）のみ追加")
    print("✓ 既存コードは一切変更不要")
    print("✓ 既存機能への影響ゼロ")
    print("→ 安全に新機能を追加可能")
    
    loose_push_service = LooseCoupledNotificationService(LooseCoupledPushSender())
    print(loose_push_service.send_notification("新機能テスト", "device123"))
    
    print("\n" + "=" * 60)
    print("【実際の開発現場での影響】")
    print("=" * 60)
    print("\n■ 密結合実装の現実")
    print("• 新機能追加のたびに既存コードレビューが必要")
    print("• 既存機能の回帰テストが必要")
    print("• 複数人で開発する際のコンフリクト発生")
    print("• リリース前の総合テスト工数増大")
    
    print("\n■ 疎結合実装の現実")
    print("• 新機能のみの単体テストで済む")
    print("• 既存機能への影響を心配する必要がない")
    print("• 並行開発が容易")
    print("• 段階的リリースが可能")
