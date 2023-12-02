import importlib
import pkg_resources

@python
def locate(module: str):
    # Create generator to store all CLI scripts
    pkgs = pkg_resources.iter_entry_points(group='console_scripts')

    # Store entry points; pkgs is a generator, so it exhausts itself
    entry_points = []

    # Iterate and store
    for pkg in pkgs:
        entry_points.append(pkg)

    bandit_entry = None
    for entry in entry_points:
        if entry.name == module:
            bandit_entry = entry.module_name


    mod = importlib.import_module(bandit_entry)
    return mod

if __name__ == "__main__":
    locate()
