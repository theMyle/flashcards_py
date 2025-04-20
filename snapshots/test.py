from datetime import datetime, timedelta

today = datetime.now().date()
print(f"{today=}")

tommorrow = today + timedelta(days=10)
print(f"{tommorrow=}")

