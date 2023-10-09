from templated_mail.mail import BaseEmailMessage


class CustomerRobotInStockEmail(BaseEmailMessage):
    template_name = "email/robot_in_stock.html"

    def get_context_data(self):
        context = super().get_context_data()

        robot = context.get("robot").split('-')
        context["model"] = robot[0]
        context["version"] = robot[1]
        return context
