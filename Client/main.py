import sys, time
sys.path.append("/Data")
import Data
import webhook
import threading

wh = webhook.WebhookManager()
thread = threading.Thread(target=wh.run())
thread.start()
dm = Data.DataManager()

while True:
    wh.update_data(dm.return_data_json())
    time.sleep(1)