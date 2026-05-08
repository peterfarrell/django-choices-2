from importlib.metadata import PackageNotFoundError, version

from .choices import C, ChoiceItem, DjangoChoices

try:
    __version__ = version("django-choices-2")
except PackageNotFoundError:
    # The package is not installed, so we don't know the version.
    __version__ = "0.0.0"

__all__ = ["ChoiceItem", "DjangoChoices", "C"]
