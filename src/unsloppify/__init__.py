"""unsloppify — strip AI slop from prose."""

__version__ = "0.1.1"

from unsloppify.engine import Finding, Rule, load_rules, scan_text
from unsloppify.fixers import apply_fixes

__all__ = ["Finding", "Rule", "__version__", "apply_fixes", "load_rules", "scan_text"]
