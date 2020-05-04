# -*- coding: utf-8 -*-
import json
import sys
from hl7_utils import hl7_str_to_dict


def processor(input):
    input_file = open(input, "r")
    input_str = '\r'.join(input_file.readlines())

    # Convert it
    input_dict = hl7_str_to_dict(input_str)

    with open("outputs/" + input[6:-4] + ".json", "w+") as output_file:
        json.dump(input_dict, output_file, indent=2)


if __name__ == "__main__":
    processor(sys.argv[1])
