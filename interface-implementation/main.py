# クライアントコード

from interface_implementation import PaymentProcessor


class OrderService:

    def __init__(self, payment_processor: PaymentProcessor):
        # インターフェースに依存する、具体的な実装には依存しない
        self.payment_processor = payment_processor

    def complete_order(self, order_data: dict):
        amount = order_data['amount']
        card_info = order_data['card_info']

        # 支払いを処理
        if self.payment_processor.process_payment(amount, card_info):
            print("注文が完了しました。")
            return True
        else:
            print("支払い処理に失敗しました。")
            return False


# 使用例：実装を簡単に差し替え可能
def main():
    # Stripe決済を使用
    from interface_implementation import StripePaymentProcessor
    stripe_processor = StripePaymentProcessor()
    order_service = OrderService(stripe_processor)

    order_data = {
        'amount': 1000.0,
        'card_info': {'number': '1234-5678-9012-3456', 'expiry': '12/25'}
    }
    order_service.complete_order(order_data)

    # PayPal決済を使用
    from interface_implementation import PayPalPaymentProcessor
    paypal_processor = PayPalPaymentProcessor()
    order_service = OrderService(paypal_processor)

    order_service.complete_order(order_data)
