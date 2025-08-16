import yaml
import os

CONFIG_PATH = "config.yml"

DEFAULT_CONFIG = {
    "TOKEN": "",
    "PREFIX": "!",
    "CLIENT_SECRET": "",
    "USER_AGENT": ""
}

class basicconfig:

    if not os.path.exists(CONFIG_PATH):
        with open(CONFIG_PATH, "w") as file:
            # Write comments and default config values
            file.write("# Your discord bot token get it by creating an application at https://discord.com/developers/applications\n")
            yaml.dump({"TOKEN": ""}, file)

            file.write("\n# Prefix is for the discord bot prefixed commands (such as !help, '!' is the prefix here)\n")
            yaml.dump({"PREFIX": "!"}, file)

            file.write("\n# Client Secret for Reddit API integrations (https://www.reddit.com/prefs/apps/)\n")
            yaml.dump({"CLIENT_SECRET": ""}, file)

            file.write("\n# User Agent string for API requests\n")
            yaml.dump({"USER_AGENT": ""}, file)

    with open(CONFIG_PATH, "r") as file:
        try:
            _config = yaml.safe_load(file)
            if not isinstance(_config, dict) or set(_config.keys()) != set(DEFAULT_CONFIG.keys()):
                raise ValueError("Invalid configuration structure.")
        except (yaml.YAMLError, ValueError):
            _config = DEFAULT_CONFIG.copy()
            with open(CONFIG_PATH, "w") as reset_file:
                reset_file.write("# Your discord bot token get it by creating an application at https://discord.com/developers/applications\n")
                yaml.dump({"TOKEN": _config["TOKEN"]}, reset_file)

                reset_file.write("\n# Prefix is for the discord bot prefixed commands (such as !help, '!' is the prefix here)\n")
                yaml.dump({"PREFIX": _config["PREFIX"]}, reset_file)

                reset_file.write("\n# Client Secret for Reddit API integrations (https://www.reddit.com/prefs/apps/)\n")
                yaml.dump({"CLIENT_SECRET": _config["CLIENT_SECRET"]}, reset_file)

                reset_file.write("\n# User Agent string for API requests\n")
                yaml.dump({"USER_AGENT": _config["USER_AGENT"]}, reset_file)

    TOKEN = _config.get("TOKEN", "")
    PREFIX = _config.get("PREFIX", "!")
    CLIENT_SECRET = _config.get("CLIENT_SECRET", "")
    USER_AGENT = _config.get("USER_AGENT", "")
