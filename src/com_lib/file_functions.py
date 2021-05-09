# -*- coding: utf-8 -*-
import csv
import json
import os
import random
from datetime import datetime
from pathlib import Path
from typing import List

from loguru import logger

# Directory Path
directory_to__files: str = "data"


def delete_file(file_name: str):

    if isinstance(file_name, str) is not True:
        raise TypeError(f"{file_name} is not a valid string")

    elif "/" in file_name or "\\" in file_name:
        raise TypeError(f"{file_name} cannot contain \\ or /")

    file_named, file_type = file_name.split(".")
    logger.info(f"file {file_named} and file type {file_type}")

    if file_type == "csv":
        directory = file_type
    elif file_type == "json":
        directory = file_type
    else:
        directory = "text"

    file_directory = f"{directory_to__files}/{directory}"
    directory_path = Path.cwd().joinpath(file_directory)
    file_path = f"{directory_path}/{file_name}"

    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"file not found error: {file_name}")

    os.remove(file_path)
    logger.info(f"file {file_name} deleted from file path: {file_path}")
    return "complete"


# get list of files in directory
def get_data_directory_list(directory: str):

    if isinstance(directory, str) is not True:
        raise TypeError(f"{directory} is not a valid string")

    file_directory = f"{directory_to__files}/{directory}"
    directory_path = Path.cwd().joinpath(file_directory)
    file_list: list = os.listdir(directory_path)
    return file_list


# Json File Processing
# Json Save new file
def save_json(filename: str, data):
    file_name = f"{filename}"
    file_directory = f"{directory_to__files}/json"
    file_save = Path.cwd().joinpath(file_directory).joinpath(file_name)

    if isinstance(data, (list, dict)) is not True:
        raise TypeError(
            f"{data} must be a list or a dictionary instead of type {type(data)}"
        )
    elif "/" in file_name or "\\" in file_name:
        raise TypeError(f"{file_name} cannot contain \\ or /")

    # open/create file
    with open(file_save, "w+") as write_file:
        # write data to file
        json.dump(data, write_file)

    logger.info(f"File Create: {file_name}")
    return "complete"


# TODO: figure out a method of appending an existing json file
# def append_json(filename, data):
#     return 'some result'

# Json Open file
def open_json(filename: str):
    # add extension to file name
    file_name = f"{filename}"
    file_directory = f"{directory_to__files}/json"
    # create file in filepath
    file_save = Path.cwd().joinpath(file_directory).joinpath(file_name)
    # Try/Except block
    if not os.path.isfile(file_save):
        raise FileNotFoundError(f"file not found error: {file_save}")

    try:
        if isinstance(filename, str) is not True:
            raise TypeError(f"{file_name} is not a valid string")
        # open file
        with open(file_save) as read_file:
            # load file into data variable
            result: dict = json.load(read_file)

        logger.info(f"File Opened: {file_name}")
        return result

    except FileNotFoundError as e:
        # log error if
        logger.critical(e)
    except TypeError as e:
        # log error if
        logger.critical(e)


# CSV File Processing
# CSV Save new file
def save_csv(filename: str, data: list):
    # add extension to file name
    file_name = f"{filename}"
    file_directory = f"{directory_to__files}/csv"
    # create file in filepath
    file_save = Path.cwd().joinpath(file_directory).joinpath(file_name)

    if isinstance(data, list) is not True:
        raise TypeError(f"{data} is not a valid string")
    elif "/" in file_name or "\\" in file_name:
        raise TypeError(f"{file_name} cannot contain \\ or /")
    # open/create file
    with open(file_save, "w+", encoding="utf-8", newline="") as write_file:
        # write data to file
        file_writer = csv.writer(
            write_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL
        )
        for row in data:
            file_writer.writerow(row)

    logger.info(f"File Create: {file_name}")
    return "complete"


# TODO: figure out a method of appending an existing json file
# def append_json(filename, data):
#     return 'some result'

# TODO: Figure out a method of appending existing CSV files
# def append_csv(filename, data):
#     return 'some result'


# CSV Open file
# pass file name and optional delimiter (default is ',')
# Output is dictionary/json
# expectation is for file to be quote minimal and skipping initial spaces is
# a good thing
# modify as needed
def open_csv(filename: str, delimit: str = None):
    if delimit is None:
        delimit = ","
    # add extension to file name
    file_name: str = f"{filename}"
    file_directory: str = f"{directory_to__files}/csv"
    # create file in filepath
    file_save = Path.cwd().joinpath(file_directory).joinpath(file_name)

    if not os.path.isfile(file_save):
        raise FileNotFoundError(f"file not found error: {file_save}")

    # Try/Except block
    # open file
    data = []
    with open(file_save) as read_file:
        # load file into data variable
        csv_data = csv.DictReader(
            read_file,
            delimiter=delimit,
            quoting=csv.QUOTE_MINIMAL,
            skipinitialspace=True,
        )

        # convert list to JSON object
        title = csv_data.fieldnames
        # iterate through each row to create dictionary/json object
        for row in csv_data:
            data.extend([{title[i]: row[title[i]] for i in range(len(title))}])
        logger.info(f"File Opened: {file_name}")
    return data


def create_sample_files(filename: str, sample_size: int):

    first_name: list = [
        "Daniel",
        "Catherine",
        "Valerie",
        "Mike",
        "Kristina",
        "Linda",
        "Olive",
        "Mollie",
        "Nadia",
        "Elisha",
        "Lorraine",
        "Nedra",
        "Voncile",
        "Katrina",
        "Alan",
        "Clementine",
        "Kanesha",
    ]

    csv_data = []
    count = 0
    for _ in range(sample_size):
        r_int: int = random.randint(0, len(first_name) - 1)
        if count == 0:
            sample_list: List[str] = ["name", "birth_date"]
        else:
            sample_list: List[str] = [
                first_name[r_int],
                str(gen_datetime()),
            ]  # type: ignore

        count += 1
        csv_data.append(sample_list)

    csv_file = f"{filename}.csv"
    save_csv(csv_file, csv_data)

    json_data = []
    for _ in range(sample_size):
        r_int = random.randint(0, len(first_name) - 1)
        sample_dict: dict = {
            "name": first_name[r_int],
            "birthday_date": str(gen_datetime()),
        }
        json_data.append(sample_dict)
    json_file = f"{filename}.json"
    save_json(json_file, json_data)


def gen_datetime(min_year: int = None, max_year: int = None):
    if min_year is None:
        min_year = 1900
    if max_year is None:
        max_year = datetime.now().year
    # generate a datetime in format yyyy-mm-dd hh:mm:ss.000000
    year: int = random.randint(min_year, max_year)
    month: int = random.randint(1, 12)
    day: int = random.randint(1, 28)
    hour: int = random.randint(0, 12)
    minute: int = random.randint(0, 59)
    second: int = random.randint(0, 59)
    date_value: datetime = datetime(year, month, day, hour, minute, second)

    # print(date_value)
    return date_value


# CSV File Processing
# CSV Save new file
def save_text(filename: str, data: str) -> str:
    """
    Save text to file. Input is the name of the file (x.txt, x.html, etc..)
    and the data to be written to file.

    Arguments:
        filename {str} -- [description]
        data {str} -- [description]

    Returns:
        str -- [description]
    """
    # add extension to file name
    file_name = f"{filename}"
    file_directory = f"{directory_to__files}/text"
    # create file in filepath
    file_save = Path.cwd().joinpath(file_directory).joinpath(file_name)

    if isinstance(data, str) is not True:
        raise TypeError(f"{file_name} is not a valid string")

    elif "/" in file_name or "\\" in file_name:
        raise TypeError(f"{file_name} cannot contain \\ or /")

    # open/create file
    f = open(file_save, "w+", encoding="utf-8")
    # write data to file
    f.write(data)
    f.close()
    logger.info(f"File Create: {file_name}")
    return "complete"


def open_text(filename: str) -> str:
    """
    Open text file and return as string

    Arguments:
        filename {str} -- [description]

    Returns:
        str -- [description]
    """
    # add extension to file name
    file_name: str = f"{filename}"
    file_directory: str = f"{directory_to__files}/text"
    # create file in filepath
    file_save = Path.cwd().joinpath(file_directory).joinpath(file_name)
    if not os.path.isfile(file_save):
        raise FileNotFoundError(f"file not found error: {file_save}")

    if isinstance(filename, str) is not True:
        raise TypeError(f"{file_name} is not a valid string")

    elif "/" in filename or "\\" in filename:
        raise TypeError(f"{file_name} cannot contain \\ or /")
    # open/create file
    f = open(file_save, "r", encoding="utf-8")
    # write data to file
    data = f.read()

    logger.info(f"File Create: {file_name}")
    return data
