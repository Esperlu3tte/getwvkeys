import argparse

from pathlib import Path
from flask import Flask

from getwvkeys import config
from getwvkeys.libraries import User
from getwvkeys.models.Shared import db

app = Flask(__name__.split(".")[0], root_path=str(Path(__file__)))
app.config["SQLALCHEMY_DATABASE_URI"] = config.SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = config.SECRET_KEY
app.app_context().push()

db.init_app(app)

parser = argparse.ArgumentParser(prog="Create User")

parser.add_argument("username")

parser.add_argument("-K", "--api-key", required=False)
parser.add_argument("-F", "--flags", type=int, required=False)
parser.add_argument("-D", "--discriminator", required=False)
parser.add_argument("-A", "--avatar", required=False)
parser.add_argument("-P", "--public-flags", type=int, required=False)

args = parser.parse_args()

userDict = dict()
userDict["username"] = args.username
if args.api_key != None:
    userDict["api_key"] = args.api_key
if args.flags != None:
    userDict["flags_raw"] = args.flags
if args.discriminator != None:
    userDict["discriminator"] = args.discriminator
if args.avatar != None:
    userDict["avatar"] = args.avatar
if args.public_flags != None:
    userDict["public_flags"] = args.public_flags

user = User.create(db, userDict)

print("      ID:", user.id)
print("Username:", user.username)
print(" API Key:", user.api_key)
