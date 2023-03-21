import importlib
import pkgutil

package = importlib.import_module(__name__)
sub_modules = {}
for _, module_name, _ in pkgutil.walk_packages(package.__path__):
    full_path = package.__name__+ '.' + module_name
    try:
        sub_modules[full_path] = importlib.import_module(full_path)
    except ModuleNotFoundError:
        print(full_path, ' was not loaded.')
        continue