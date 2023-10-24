from typing import List

def portfolio_change(port_t_plus: List,
                     port_t: List,
                     price_t_plus: List,
                     price_t: List):
    """calculate the portfolio value change between time t+1 and time t"""
    # TODO: add some assertion
    return sum([x*y for x, y in zip(port_t_plus, price_t_plus)]) - sum([x*y for x, y in zip(port_t, price_t)])