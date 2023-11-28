import os

import dotenv

PATH = os.path.join(os.pardir, "config.env")


def load_skills() -> list:
    dotenv.load_dotenv(os.path.join(os.pardir, "config.env"))
    skills = os.environ["SCRAPY_SKILLS"]
    skills = skills.lower()
    skills = skills.replace("\n", " ")
    skills = skills.split(", ")
    return skills
