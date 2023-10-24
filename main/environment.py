from utils.reward import portfolio_change

def env_change(state,
               action, 
               prices):
    """
    """
    new_state = 0
    price = [0] * len(new_state)
    price_t_plus = [0] * len(new_state)
    reward = portfolio_change(port_t_plus=new_state,
                              port_t=state,
                              price_t_plus=price_t_plus,
                              price_t=price)
    return new_state, reward

class SimulatedEnv:
    def __init__(self, ):
        pass
    def step(self, ):
        """"""
        pass