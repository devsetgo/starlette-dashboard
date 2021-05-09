# -*- coding: utf-8 -*-
"""
functions to run test, install, etc...
"""

import os

import click


def list_keys(process):
    # list of keys in dictionary
    result = []
    # get all keys
    for k, v in process.items():
        result.append(k)

    # return results sorted
    result.sort()
    return result


@click.command()
@click.option(
    "--run",
    prompt="Run Process",
    help="autoflake, dev, flake8, force, hello, install, isort, prd, reinstall, test",
)
def start_process(run):
    process: dict = {
        "test": "run_tests.sh",
        "dev": "run_dev.sh",
        "prd": "run_prd.sh",
        "install": "requirements_install.sh",
        "reinstall": "requirements_reinstall.sh",
        "force": "requirements_force_reinstall.sh",
        "flake8": "flake8.sh",
        "isort": "isort_run.sh",
        "autoflake": "autoflake.sh",
        "hello": "hello.sh",
        # add more as necessary
    }

    if run.lower() == "help":
        # get keys from key value pair in process dictionary
        keys = list_keys(process)
        print(f"Here are the commands you can use {keys}")

    elif run.lower() in process:
        # run os command entered
        command = f"./scripts/{process[run.lower()]}"
        os.system(command)
    else:
        # error and notification
        print(f"Cannot run process {run} as it is not a valid option")


if __name__ == "__main__":
    start_process()
