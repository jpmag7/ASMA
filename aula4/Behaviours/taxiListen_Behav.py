from spade.behaviour import OneShotBehaviour
from spade.message import Message
import time

class TaxiListenBehav(OneShotBehaviour):

    async def run(self):
        while True:
            msg = await self.receive(timeout=1000)
            toDo = msg.get_metadata("performative")

            if toDo == "take_client":
                info = msg.body.split("|")
                client, x, y = info[0], float(info[1]), float(info[2])

                time.sleep(3)
                self.agent.x_pos = x
                self.agent.y_pos = y

                msg = Message(to="manager@192.168.56.1")
                msg.set_metadata("performative", "trip_end")
                msg.body = f"{str(self.agent.jid)}|{self.agent.x_pos}|{self.agent.y_pos}"
                print(f"Taxi ending trip")
                await self.send(msg)

                msg = Message(to=client)
                msg.set_metadata("performative", "trip_end")
                msg.body = f"{str(self.agent.jid)}|{self.agent.x_pos}|{self.agent.y_pos}"
                await self.send(msg)