from spade.behaviour import OneShotBehaviour
from spade.message import Message
import random

class CustomerListenBehav(OneShotBehaviour):

    async def run(self):
        while True:
            msg = await self.receive(timeout=1000)
            toDo = msg.get_metadata("performative")
            print(f"Customer received: {toDo}")

            if toDo == "trip_end":
                break