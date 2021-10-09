# MyApp

## Install

```shell
pip install -e .
```

Optionally, you can install and use the external_plugin separately. If you don't install this plugin sepately then it will not be detected by the main application. This is an example of using dynamic plugin discovery at runtime (check the main app's cli function to see how it finds and loads these).

```shell
pip install -e ./external_plugins/my_external_plugin
```

## Usage

Usage for the app:
```shell
myapp
```

Running the internal plugin:
```shell
myapp my_internal_plugin
```

Running the external plugin
```shell
myapp my_external_plugin
```

Note: Because the external plugin is also installed separately, it can also be used by its console script:

running the usage for the standalone plugin
```shell
my_external_plugin
```

Running the external plugin standalone
```shell
my_external_plugin run
```

## How it works

The main app has its own entry point for its cli. It also registers its internal plugin to the `myapp_plugins` entry point.
```toml
[options.entry_points]
console_scripts =
  myapp = myapp:cli
myapp_plugins =
  my_internal_plugin = myapp.plugins.my_internal_plugin:run
```

The source code for the app uses `pgk_resources` to find and load the entry points that are registered for the app. In this case, any package that is installed and registered with a `myapp_plugins` entrypoint will get picked up by the fire cli. 

```python
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
```

## Next Steps

1. Create a `__main__.py` file for the main application.
2. Move the cli to the `__main__.py` file.
3. Add core functionality to the main application.
4. Move the `myapp_plugins` entry_points name to the config file as a constant.