from typing import List
import pandas as pd


def mapping_action(param: int = 5,
                   param_name: str = 'window_size',
                   state: List = None, 
                   mapping_rule: dict = None):
    """Map parameter and state ... to a feasible action

    TODO: replace the following
    use a sample: param is the 
    """
    # TODO: Replace the rule
    from random import randint
    if state is None:
        state = [randint(3, 30) for i in range(10)]
    
    latest_ma = pd.Series(state).rolling(window=param).mean().to_list()[-1]
    if latest_ma > 20: return 1
    elif latest_ma > 10: return 0
    return -1
