class Account:
    def __init__(self, account_id, type, equity, max_drawdown, current_drawdown, target, met_minimum_days, status_for_withdrawal, current_positions=None, total_phases=None, current_phase=None, cost_so_far=None, max_daily_loss=None, current_profit=None, days_traded=None, last_traded_day=None, max_leverage=None):
        self.account_id = account_id
        self.type = type  # 'challenge', 'funded'
        self.equity = equity
        self.max_drawdown = max_drawdown
        self.current_drawdown = current_drawdown
        self.target = target
        self.met_minimum_days = met_minimum_days
        self.status_for_withdrawal = status_for_withdrawal
        self.current_positions = current_positions if current_positions else []
        self.total_phases = total_phases
        self.current_phase = current_phase
        self.cost_so_far = cost_so_far
        self.max_daily_loss = max_daily_loss
        self.current_profit = current_profit
        self.days_traded = days_traded
        self.last_traded_day = last_traded_day
        self.max_leverage = max_leverage

    def target_reached(self):
        return self.current_drawdown <= self.target

    def is_eligible_for_withdrawal(self):
        return self.status_for_withdrawal and self.met_minimum_days

    def drawdown_within_limits(self, min_percentage, max_percentage):
        drawdown_limit = self.max_drawdown * (min_percentage / 100)
        return self.current_drawdown >= drawdown_limit and self.current_drawdown <= self.max_drawdown * (max_percentage / 100)
    # Placeholder for additional account-related methods