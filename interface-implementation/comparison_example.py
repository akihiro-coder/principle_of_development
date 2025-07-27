"""
インターフェース分離あり/なしの比較例
"""

from abc import ABC, abstractmethod

print("=" * 60)
print("インターフェース分離の有無による比較")
print("=" * 60)

# ========== インターフェース分離なし（密結合） ==========
print("\n【密結合な実装の問題点】")

class DirectEmailSender:
    def send_email(self, message: str, recipient: str):
        return f"Email送信: {message} to {recipient}"

class DirectSMSSender:
    def send_sms(self, message: str, recipient: str):
        return f"SMS送信: {message} to {recipient}"

class TightCoupledService:
    def __init__(self):
        self.email_sender = DirectEmailSender()
        self.sms_sender = DirectSMSSender()
    
    def send_notification(self, method: str, message: str, recipient: str):
        if method == "email":
            return self.email_sender.send_email(message, recipient)
        elif method == "sms":
            return self.sms_sender.send_sms(message, recipient)
        # 新しい通知方法を追加するたびにここを修正する必要がある
        else:
            raise ValueError(f"未対応の通知方法: {method}")

# ========== インターフェース分離あり（疎結合） ==========
print("\n【疎結合な実装の利点】")

class NotificationSender(ABC):
    @abstractmethod
    def send(self, message: str, recipient: str) -> str:
        pass

class LooseCoupledEmailSender(NotificationSender):
    def send(self, message: str, recipient: str) -> str:
        return f"Email送信: {message} to {recipient}"

class LooseCoupledSMSSender(NotificationSender):
    def send(self, message: str, recipient: str) -> str:
        return f"SMS送信: {message} to {recipient}"

class LooseCoupledService:
    def __init__(self, sender: NotificationSender):
        self.sender = sender
    
    def send_notification(self, message: str, recipient: str):
        return self.sender.send(message, recipient)

# ========== 比較実行 ==========
if __name__ == "__main__":
    print("\n--- 密結合実装の使用例 ---")
    tight_service = TightCoupledService()
    print(tight_service.send_notification("email", "テストメッセージ", "user@example.com"))
    print(tight_service.send_notification("sms", "テストメッセージ", "+1234567890"))
    
    print("\n--- 疎結合実装の使用例 ---")
    email_service = LooseCoupledService(LooseCoupledEmailSender())
    sms_service = LooseCoupledService(LooseCoupledSMSSender())
    print(email_service.send_notification("テストメッセージ", "user@example.com"))
    print(sms_service.send_notification("テストメッセージ", "+1234567890"))

    print("\n" + "=" * 60)
    print("【メリット・デメリット分析】")
    print("=" * 60)
    
    print("\n■ インターフェース分離なし（密結合）")
    print("【メリット】")
    print("✓ 実装が単純で理解しやすい")
    print("✓ 小規模プロジェクトでは開発速度が速い")
    print("✓ オーバーエンジニアリングを避けられる")
    print("✓ デバッグが容易（呼び出し先が明確）")
    
    print("\n【デメリット】")
    print("✗ 新機能追加時に既存コードの修正が必要")
    print("✗ テストが困難（モックやスタブが作りにくい）")
    print("✗ コードの再利用性が低い")
    print("✗ 変更の影響範囲が広い")
    print("✗ 並行開発が困難")
    
    print("\n■ インターフェース分離あり（疎結合）")
    print("【メリット】")
    print("✓ 新機能追加時に既存コードを変更不要")
    print("✓ テストが容易（モック実装を簡単に作成可能）")
    print("✓ コードの再利用性が高い")
    print("✓ 変更の影響範囲が限定的")
    print("✓ 並行開発が容易")
    print("✓ 保守性が高い")
    
    print("\n【デメリット】")
    print("✗ 初期実装が複雑")
    print("✗ 小規模プロジェクトではオーバーエンジニアリング")
    print("✗ 抽象化により理解が困難になる場合がある")
    print("✗ パフォーマンスのオーバーヘッド（わずか）")
