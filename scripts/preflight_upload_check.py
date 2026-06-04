#!/usr/bin/env python3
"""Public-safe upload preflight for charlesSKILL."""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

BLOCKED_PATHS = [
    re.compile(pattern, re.IGNORECASE)
    for pattern in [
        r"(^|/)\.env($|\.(?!example$))",
        r"(^|/)(private|exports|downloads|screenshots|logs|trace|traces)(/|$)",
        r"(^|/)(cookies|storage-state)\.json$",
        r"\.(xlsx|xls|csv|tsv|pptx|ppt|zip|7z|rar|log|pem|key|p12|pfx|token|secret)$",
        r"(secret|credential|credentials).*\.(json|ya?ml|toml|ini)$",
    ]
]

SECRET_TEXT = [
    re.compile(pattern, re.IGNORECASE)
    for pattern in [
        r"BEGIN [A-Z ]*PRIVATE KEY",
        r"(api[_-]?key|access[_-]?key|client[_-]?secret|app[_-]?secret|password|passwd|cookie|bearer|token)\s*[:=]\s*['\"][^'\"\s.]{16,}['\"]",
        r"(webhook|refresh_token|session)\s*[:=]\s*['\"][^'\"\s.]{16,}['\"]",
    ]
]

BUSINESS_TEXT = [
    re.compile(pattern, re.IGNORECASE)
    for pattern in [
        r"(身份证号|银行卡号|支付流水)\s*[:=：]",
        r"(真实客户|真实学生|真实家长|真实合同|真实报价|真实营收|真实成本)\s*[:=：]",
    ]
]

TEXT_EXTENSIONS = {".css", ".html", ".ini", ".js", ".json", ".md", ".mjs", ".py", ".sh", ".txt", ".yaml", ".yml"}


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def git_visible_files() -> list[Path]:
    result = subprocess.run(
        ["git", "ls-files", "--cached", "--others", "--exclude-standard"],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if result.returncode != 0:
        print(result.stderr.strip() or "git ls-files failed", file=sys.stderr)
        sys.exit(result.returncode)
    return [ROOT / line for line in result.stdout.splitlines() if line.strip()]


def should_skip(path: Path) -> bool:
    parts = set(path.relative_to(ROOT).parts)
    return ".git" in parts or "node_modules" in parts or "__pycache__" in parts


def scan_paths() -> list[str]:
    findings: list[str] = []
    for path in git_visible_files():
        if should_skip(path) or not path.is_file():
            continue
        relative = rel(path)
        for pattern in BLOCKED_PATHS:
            if pattern.search(relative):
                findings.append(f"blocked path: {relative}")
                break
    return findings


def scan_text() -> list[str]:
    findings: list[str] = []
    for path in git_visible_files():
        if should_skip(path) or not path.is_file() or path.suffix.lower() not in TEXT_EXTENSIONS:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for line_no, line in enumerate(text.splitlines(), start=1):
            if any(pattern.search(line) for pattern in SECRET_TEXT):
                findings.append(f"possible secret: {rel(path)}:{line_no}")
            if any(pattern.search(line) for pattern in BUSINESS_TEXT):
                findings.append(f"possible business data: {rel(path)}:{line_no}")
    return findings


def main() -> int:
    findings = scan_paths() + scan_text()
    if findings:
        print("Preflight upload check failed:")
        for finding in findings:
            print(f"- {finding}")
        return 1
    print("Preflight upload check passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
