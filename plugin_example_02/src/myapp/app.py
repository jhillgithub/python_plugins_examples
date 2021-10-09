import fire
import pkg_resources

def load_plugins():
    plugins = {}
    for entry_point in pkg_resources.iter_entry_points('myapp_plugins'):
        plugins[entry_point.name] = entry_point.load()
    return plugins

def cli():
    print("Running Cli")
    fire.Fire(load_plugins())
    
if __name__ == '__main__':
    cli()