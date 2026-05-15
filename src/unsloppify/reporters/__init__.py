"""Output formatters for findings."""

from unsloppify.reporters.github import GitHubReporter
from unsloppify.reporters.json_ import JsonReporter
from unsloppify.reporters.text import TextReporter

REPORTERS = {
    "text": TextReporter,
    "json": JsonReporter,
    "github": GitHubReporter,
}

__all__ = ["REPORTERS", "GitHubReporter", "JsonReporter", "TextReporter"]
