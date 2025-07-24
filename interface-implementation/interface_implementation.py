from abc import ABC, abstractmethod


# インターフェース：「何をするか」を定義
class PaymentProcessor(ABC):
    """支払い処理の契約を定義"""

    @abstractmethod
    def process_payment(self, amount: float, card_info: dict) -> bool:
        """支払いを処理する"""
        pass

    @abstractmethod
    def refund_payment(self, transaction_id: str) -> bool:
        """支払いを返金する"""
        pass

    @abstractmethod
    def get_transaction_status(self, transaction_id: str) -> str:
        """取引状況を取得する"""
        pass


# 実装1: Stripe決済
class StripePaymentProcessor(PaymentProcessor):
    def process_payment(self, amount: float, card_info: dict) -> bool:
        print(f"Stripeで{amount}円を処理")
        # 実際のStripe API呼び出しをここに実装
        return True

    def refund_payment(self, transaction_id: str) -> bool:
        print(f"Stripeで取引ID {transaction_id} を返金")
        # 実際のStripe API呼び出しをここに実装
        return True

    def get_transaction_status(self, transaction_id: str) -> str:
        print(f"Stripeで取引ID {transaction_id} のステータスを取得")
        # 実際のStripe API呼び出しをここに実装
        return "成功"

# 実装2: PayPal決済
class PayPalPaymentProcessor(PaymentProcessor):
    def process_payment(self, amount: float, card_info: dict) -> bool:
        print(f"PayPalで{amount}円を処理")
        # 実際のPayPal API呼び出しをここに実装
        return True

    def refund_payment(self, transaction_id: str) -> bool:
        print(f"PayPalで取引ID {transaction_id} を返金")
        # 実際のPayPal API呼び出しをここに実装
        return True

    def get_transaction_status(self, transaction_id: str) -> str:
        print(f"PayPalで取引ID {transaction_id} のステータスを取得")
        # 実際のPayPal API呼び出しをここに実装
        return "成功"


















