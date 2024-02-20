from pathlib import Path
import ast

def read_instance(instance_name):
    with Path().absolute().joinpath("instances/"+instance_name).open() as reader:
        lines = reader.readlines()
        u_size = ast.literal_eval(lines[1])
        s_size = ast.literal_eval(lines[4])
        s = ast.literal_eval(lines[7])
        sol = ast.literal_eval(lines[10])
        seq = ast.literal_eval(lines[13])
        return u_size, s_size, s, sol, seq