import toml
from pathlib import Path
import uuid


def generate_project_config(project_title, base_path, paths):
    config = {
        "title": project_title,
        "type": "gstr-9c-project",
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