from spade.behaviour import OneShotBehaviour
from spade.message import Message

class ManagerListenBehav(OneShotBehaviour):

    async def run(self):
        while True:
            msg = await self.receive(timeout=1000)
            toDo = msg.get_metadata("performative")
            print(f"Manager received: {toDo}")

            if toDo == "client_request":
                info = msg.body.split("|")
                client, x, y = info[0], float(info[1]), float(info[2])

                min_dist = 10000000
                taxi = None
                for t in self.agent.taxis:
                    if t["available"]:
                        dist = (t["x"] - x) * (t["x"] - x) + (t["y"] - y) * (t["y"] - y)
                        if dist < min_dist:
                            min_dist = dist
                            taxi = t

                if taxi == None:
                    self.agent.queue.append(f"{client}|{x}|{y}")
                else:
                    t["available"] = False
                    msg = Message(to=taxi["id"])
                    msg.set_metadata("performative", "take_client")
                    msg.body = f"{client}|{x}|{y}"
                    print(f"Manager dispatching taxi {taxi['id']}")
                    await self.send(msg)
            
            elif toDo == "taxi_subscribe":
                info = msg.body.split("|")
                t, x, y = info[0], float(info[1]), float(info[2])
                taxi = {
                    "id" : t,
                    "available" : True,
                    "x" : x,
                    "y" : y
                }
                self.agent.taxis.append(taxi)

            elif toDo == "trip_end":
                info = msg.body.split("|")
                t, x, y = info[0], float(info[1]), float(info[2])
                for tax in self.agent.taxis:
                    if tax["id"] == t:
                        tax["x"] = x
                        tax["y"] = y
                        if len(self.agent.queue) > 0:
                            msg = Message(to=tax["id"])
                            msg.set_metadata("performative", "take_client")
                            msg.body = self.agent.queue[0]
                            self.agent.queue.pop(0)
                            print(f"Manager dispatching taxi {tax['id']}")
                            await self.send(msg)
                        else:
                            tax["available"] = True