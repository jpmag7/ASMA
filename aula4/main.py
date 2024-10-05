from customer import Customer
from manager import Manager
from taxi import Taxi
import time

PASSWORD = "Openfire_password1"

if __name__ == "__main__":
    manager  = Manager ("manager@192.168.56.1", PASSWORD)
    taxi     = Taxi    ("taxi@192.168.56.1", PASSWORD)
    customer = Customer("customer@192.168.56.1", PASSWORD)
    
    future = manager.start()
    future.wait()

    future = taxi.start()
    future.wait()

    future = customer.start()
    future.wait()

    while customer.is_alive():
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            manager.stop()
            taxi.stop()
            customer.stop()
            break
    print("Agents finished")