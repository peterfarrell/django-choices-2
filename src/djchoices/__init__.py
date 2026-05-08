from importlib.metadata import PackageNotFoundError, version

from .choices import C, ChoiceItem, DjangoChoices

try:
    # Get the version of the installed 'waybill' package
    __version__ = version("django-choices")
except PackageNotFoundError:
    # Fallback for when the package is not installed
    __version__ = "0.0.0"


__all__ = ["ChoiceItem", "DjangoChoices", "C"]
