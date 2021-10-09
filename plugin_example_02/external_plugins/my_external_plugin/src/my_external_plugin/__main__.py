import fire
from .app import run

def cli():
    fire.Fire(run)

if __name__ == '__main__':
    cli()