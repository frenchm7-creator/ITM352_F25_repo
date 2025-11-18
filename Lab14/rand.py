import importlib
import sys

packages = ["scipy", "statsmodels", "matplotlib"]

# try to get version via module attribute or importlib.metadata
try:
    from importlib.metadata import version as _get_version
except Exception:
    try:
        from importlib_metadata import version as _get_version  # type: ignore
    except Exception:
        _get_version = None

def check_packages(pkgs):
    for name in pkgs:
        try:
            mod = importlib.import_module(name)
            ver = getattr(mod, "__version__", None)
            if ver is None and _get_version is not None:
                try:
                    ver = _get_version(name)
                except Exception:
                    ver = "unknown"
            print(f"{name}: installed, version {ver}")
        except ImportError:
            print(f"{name}: NOT installed")

if __name__ == "__main__":
    check_packages(packages)