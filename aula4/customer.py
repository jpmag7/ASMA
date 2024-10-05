from spade import agent
import random

from Behaviours.customerListen_Behav import CustomerListenBehav
from Behaviours.customerStart_Behav import CustomerStartBehav


class Customer(agent.Agent):

    async def setup(self):
        print("Customer Agent {}".format(str(self.jid)) + "starting...")
        self.x_pos = random.randint(0, 1000)
        self.y_pos = random.randint(0, 1000)

        a = CustomerStartBehav()
        b = CustomerListenBehav()

        self.add_behaviour(a)
        self.add_behaviour(b)