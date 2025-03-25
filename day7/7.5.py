

import sys
import os
import importlib.util


file_path = os.path.join(os.path.dirname(__file__), '../day2/2.5.py')


spec = importlib.util.spec_from_file_location("calculator", file_path)
calculator_module = importlib.util.module_from_spec(spec)
sys.modules["calculator"] = calculator_module
spec.loader.exec_module(calculator_module)


if __name__ == "__main__":
    calculator_module.calculator() 
