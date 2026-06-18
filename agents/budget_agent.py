class BudgetAgent:
    '''
    Defines major methods like allocate and distribute budget for a task -- total budget to speaker, venue, food logistics etc. ask user for allocation of budget for each task and distribute the budget accordingly. Maintain a record of how each agent is spending and add methods to deduct and add budget as per requirements.
    '''
    def __init__(self):
        self.budgets = {
            "speaker": 0,
            "venue": 0,
            "food": 0,
            "logistics": 0
        }

    def allocate_budget(self, category, amount):
        if category in self.budgets:
            self.budgets[category] += amount

    def distribute_budget(self):
        total = sum(self.budgets.values())
        for category in self.budgets:
            self.budgets[category] /= total if total > 0 else 1

    def get_budget_report(self):
        return self.budgets
