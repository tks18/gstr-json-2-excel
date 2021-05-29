import toml
from pathlib import Path
import uuid


def generate_project_config(project_title, other_details, base_path, paths):
    config = {
        "valid": True,
        "title": project_title,
        "type": "gstr-9c-project",
        "year": other_details["year"],
        "branch": other_details["branch"],
        "unique-project-id": str(uuid.uuid4()),
        "config-path": str(Path(base_path, "project_config.toml")),
        "paths": {path["name"]: str(path["path"]) for path in paths},
    }

    with open(Path(base_path, "project_config.toml"), mode="w") as toml_config:
        toml.dump(config, f=toml_config)

    return config


def load_toml_config(path):
    config = None
    with open(path, mode="r") as toml_config:
        config = toml.load(f=toml_config)

    project_uuid = config["unique-project-id"]
    try:
        uuid.UUID(project_uuid)
    except ValueError:
        config["valid"] = False
    else:
        config["valid"] = True

    return config


def update_config(config):
    before_conf = None
    with open(Path(config["config-path"]), mode="r") as toml_config:
        before_conf = toml.load(f=toml_config)

    project_uuid = before_conf["unique-project-id"]
    try:
        uuid.UUID(project_uuid)
    except ValueError:
        before_conf["valid"] = False
        return before_conf
    else:
        before_conf["valid"] = True
        new_config = config

        with open(Path(before_conf["config-path"]), mode="w") as toml_config:
            toml.dump(new_config, f=toml_config)
            return new_config