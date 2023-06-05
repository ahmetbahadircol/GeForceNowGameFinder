from geforce_now_game_getter import get_game_price
import time

start = time.time()
get_game_price()
end = time.time()
print(f"Execution time: {(end - start)}")
