import threading

from core.email import CustomerRobotInStockEmail


class EmailThread(threading.Thread):
    def __init__(self, robot, email):
        self.robot = robot
        self.email = email
        threading.Thread.__init__(self)

    def run(self):
        CustomerRobotInStockEmail(
            context={"robot": self.robot.robot_serial},
        ).send(to=[self.email])
