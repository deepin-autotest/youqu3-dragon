import pathlib


class Config:

    root_dir = pathlib.Path(__file__).parent.absolute()

config = Config()