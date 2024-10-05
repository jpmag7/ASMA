from spade.behaviour import OneShotBehaviour
from spade.message import Message

class CustomerStartBehav(OneShotBehaviour):

    async def run(self):
        msg = Message(to="manager@192.168.56.1")
        msg.set_metadata("performative", "client_request")
        msg.body = f"{str(self.agent.jid)}|{self.agent.x_pos}|{self.agent.y_pos}"
        print(f"Client requesting taxi")
        await self.send(msg)