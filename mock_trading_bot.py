import logging
from typing import Optional

LOG_FILE = "trading_bot.log"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.FileHandler(LOG_FILE, encoding="utf-8")]
)

logger = logging.getLogger(__name__)


class MockBinanceClient:
    order_id = 10000

    def futures_change_leverage(self, symbol, leverage):
        logger.info(f"[MOCK] Leverage set -> {symbol} @ {leverage}x")
        return {"symbol": symbol, "leverage": leverage, "status": "SUCCESS"}

    def futures_create_order(self, symbol, side, order_type, quantity, **kwargs):
        MockBinanceClient.order_id += 1
        order = {
            "symbol": symbol,
            "side": side,
            "type": order_type,
            "origQty": quantity,
            "price": kwargs.get("price", "MARKET"),
            "status": "FILLED",
            "orderId": MockBinanceClient.order_id,
            "clientOrderId": f"mock-{MockBinanceClient.order_id}"
        }
        logger.info(f"[MOCK] Order placed -> {order}")
        return order


class BasicBot:
    def __init__(self):
        logger.info("Bot initialized in MOCK MODE (no API needed)")
        self.client = MockBinanceClient()

    def _log_and_print_order(self, order: dict) -> None:
        logger.info(f"Order response: {order}")
        print("\n" + "=" * 50)
        print("               ORDER EXECUTED")
        print("=" * 50)
        print(f"  Symbol      : {order.get('symbol')}")
        print(f"  Side        : {order.get('side')}")
        print(f"  Type        : {order.get('type')}")
        print(f"  Status      : {order.get('status')}")
        print(f"  Order ID    : {order.get('orderId')}")
        print(f"  Client ID   : {order.get('clientOrderId')}")
        print(f"  Price       : {order.get('price')}")
        print(f"  Quantity    : {order.get('origQty')}")
        print("=" * 50 + "\n")

    def set_leverage(self, symbol: str, leverage: int) -> None:
        response = self.client.futures_change_leverage(symbol, leverage)
        logger.info(f"Leverage response: {response}")

    def place_market_order(self, symbol: str, side: str, quantity: float, leverage: Optional[int] = None) -> None:
        symbol = symbol.upper()
        side = side.upper()
        if leverage:
            self.set_leverage(symbol, leverage)
        order = self.client.futures_create_order(symbol=symbol, side=side, order_type="MARKET", quantity=quantity)
        self._log_and_print_order(order)

    def place_limit_order(self, symbol: str, side: str, quantity: float, price: float, leverage: Optional[int] = None) -> None:
        symbol = symbol.upper()
        side = side.upper()
        if leverage:
            self.set_leverage(symbol, leverage)
        order = self.client.futures_create_order(
            symbol=symbol, side=side, order_type="LIMIT", quantity=quantity, price=str(price)
        )
        self._log_and_print_order(order)


def get_positive_float(prompt: str) -> float:
    while True:
        value = input(f"  {prompt} ").strip()
        try:
            num = float(value)
            if num > 0:
                return num
            print("  ❗ Enter a positive number.")
        except ValueError:
            print("  ❗ Invalid number. Try again.")


def get_side() -> str:
    while True:
        side = input("  Enter side (BUY / SELL): ").strip().upper()
        if side in ("BUY", "SELL"):
            return side
        print("  ❗ Invalid side. Choose BUY or SELL.")


def main():
    print("=" * 60)
    print("            BINANCE FUTURES TRADING BOT (MOCK MODE)")
    print("=" * 60)
    print("Running WITHOUT real API keys")
    print("Orders are simulated and logged.")
    print("=" * 60 + "\n")

    bot = BasicBot()

    while True:
        print("Choose an action:")
        print("  1) Market Order")
        print("  2) Limit Order")
        print("  3) Exit")
        print("-" * 50)

        choice = input("Select option (1 / 2 / 3): ").strip()

        if choice == "3":
            print("\nExiting... Goodbye! 👋")
            print("=" * 60)
            break

        if choice not in ("1", "2"):
            print("  ❗ Invalid choice. Please try again.\n")
            continue

        print("\n--- Order Details ---")
        symbol = input("  Enter symbol (example: BTCUSDT): ").strip().upper()
        side = get_side()
        quantity = get_positive_float("Enter quantity:")

        leverage_input = input("  Enter leverage (1-125) or press Enter: ").strip()
        leverage = int(leverage_input) if leverage_input else None

        if choice == "1":
            bot.place_market_order(symbol, side, quantity, leverage)
        else:
            price = get_positive_float("Enter limit price:")
            bot.place_limit_order(symbol, side, quantity, price, leverage)

        print("-" * 50 + "\n")


if __name__ == "__main__":
    main()
