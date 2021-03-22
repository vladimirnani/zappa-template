import os
import sys

stage_name = sys.argv[1]


def dump_dot_env():
    name = f".env.{stage_name}"
    with open(name, "w") as f:
        lines = []
        for key, value in os.environ.items():
            lines.append(f"{key}={value}\n")
        f.writelines(lines)


dump_dot_env()

os.system('aws configure set aws_access_key_id $AWS_ACCESS_KEY_ID --profile profile1')
os.system('aws configure set aws_secret_access_key $AWS_SECRET_ACCESS_KEY --profile profile1')
os.system('zappa update ' + stage_name)
