#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
import yaml
import os


def read_yaml(filename):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(base_dir, "data", filename)
    with open(file_path, "r", encoding="utf-8") as f:
        return yaml.load(f, Loader=yaml.FullLoader)


if __name__ == '__main__':
    print(read_yaml("login_data"))