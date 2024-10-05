from spade import agent
import random

from Behaviours.taxiListen_Behav import TaxiListenBehav
from Behaviours.taxiStart_Behav import TaxiStartBehav


class Taxi(agent.Agent):

    async def setup(self):
        print("Taxi Agent {}".format(str(self.jid)) + "starting...")

        self.x_pos = random.randint(0, 1000)
        self.y_pos = random.randint(0, 1000)

        a = TaxiListenBehav()
        b = TaxiStartBehav()

        self.add_behaviour(a)
        self.add_behaviour(b)