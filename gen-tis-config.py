import json
import sys
from copy import deepcopy
from pathlib import Path


tis_config_template = {
        "name" : None,
        "filesystem": {
            "files": [
                {
                    "name": "tis-mkfs-stdin",
                    "from": None
                    }
                ]
            },
        "files" : [
            "bc/global.c",
            "bc/util.c",
            "bc/execute.c",
            "bc/bc.c",
            "bc/scan.c",
            "bc/load.c",
            "bc/warranty.c",
            "bc/main.c",
            "bc/storage.c",
            # "dc/numeric.c",
            # "dc/stack.c",
            # "dc/misc.c",
            # "dc/array.c",
            # "dc/eval.c",
            # "dc/dc.c",
            # "dc/string.c",
            "lib/number.c",
            # "lib/testmul.c",
            "lib/vfprintf.c",
            "lib/getopt.c",
            "lib/getopt1.c",
            "tis-mock.c",
            ],
        "compilation_cmd" : "cc -c -Os -std=c99 -Wall -Wextra -Idc -Ibc -I. -Ih",
        "no-results": True,
        # "info-json-results": "tis_results/test_array_results.json",
        # "info-csv-all": "tis_results/test_array", 
        }

def main():
    config = []
    for test_name in sys.argv:
        test_path = Path(test_name)
        if test_path.suffix != '.b':
            continue
        config_obj = deepcopy(tis_config_template)
        config_obj["name"] = test_path.stem
        config_obj["filesystem"]["files"][0]["from"] = test_name
        config.append(config_obj)
    print(json.dumps(config, sort_keys=True, indent=4))


if __name__=='__main__':
    main()
