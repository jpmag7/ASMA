from spade import agent

from Behaviours.managerListen_Behav import ManagerListenBehav


class Manager(agent.Agent):

    async def setup(self):
        print("Manager Agent {}".format(str(self.jid)) + "starting...")

        self.taxis = []
        self.queue = []

        a = ManagerListenBehav()
        self.add_behaviour(a)

