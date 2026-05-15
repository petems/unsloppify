"""JSON reporter for machine consumption / CI integration."""

from __future__ import annotations

import json
from collections import Counter
from typing import Any

from unsloppify.engine import Finding


class JsonReporter:
    def report(self, findings: list[Finding], fixes_applied: int = 0) -> None:
        payload: dict[str, Any] = {
            "version": 1,
            "summary": {
                "total": len(findings),
                "by_severity": dict(Counter(f.severity for f in findings)),
                "fixes_applied": fixes_applied,
            },
            "findings": [
                {
                    "file": str(f.file),
                    "line": f.line,
                    "column": f.column,
                    "end_line": f.end_line,
                    "end_column": f.end_column,
                    "rule_id": f.rule_id,
                    "category": f.category,
                    "severity": f.severity,
                    "message": f.message,
                    "snippet": f.snippet,
                    "fixable": f.fixable,
                }
                for f in findings
            ],
        }
        print(json.dumps(payload, indent=2))
