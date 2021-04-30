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
        "include": "tis-common.config"
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
