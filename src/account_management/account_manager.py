class AccountManager:
    def __init__(self, accounts):
        self.accounts = accounts
    
    def fetch_accounts(self):
        # Placeholder for API call to fetch and update accounts data
        pass

    def select_accounts_based_on_probability(self, trade_probability, trade_details, market_condition):
        eligible_accounts = []

        for account in self.accounts:
            if not account.target_reached() and self.account_meets_criteria(account, trade_probability, market_condition):
                if self.is_diversified(account, trade_details):
                    eligible_accounts.append(account)
        return eligible_accounts

    def account_meets_criteria(self, account, trade_probability, market_condition):
        # Enhanced logic incorporating dynamic risk adjustment and market conditions
        if trade_probability > 0.9:
            return True
        if trade_probability > 0.85 and account.type == 'funded' and not account.status_for_withdrawal:
            return True
        if trade_probability > 0.8 and account.type == 'challenge':
            return True
        if trade_probability > 0.7 and account.type == 'challenge' and account.drawdown_within_limits(80, 100):
            return True
        # Adjust based on market conditions
        if market_condition == "volatile" and account.type == 'funded':
            # Example adjustment for volatile market
            return False
        return False

    def is_diversified(self, account, trade_details):
        # Placeholder for checking if the new trade increases portfolio diversification
        return True  # Implement logic based on current_positions and trade_details
