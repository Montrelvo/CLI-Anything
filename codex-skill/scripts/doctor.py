#!/usr/bin/env python3
"""Read-only checks for a self-contained CLI-Anything Codex installation."""
import argparse
import importlib.util
import json
from pathlib import Path
import shutil


def diagnose(skill_dir, backends):
    checks = []
    resources = [
        "SKILL.md", "references/HARNESS.md", "references/CLOUD.md",
        "references/docs/PREVIEW_PROTOCOL.md", "scripts/repl_skin.py",
        "scripts/preview_bundle.py", "scripts/skill_generator.py",
        "scripts/templates/SKILL.md.template",
    ]
    resources += [f"references/commands/{mode}.md" for mode in
                  ("cli-anything", "refine", "test", "validate", "list")]
    for resource in resources:
        checks.append({"kind": "resource", "name": resource,
                       "ok": (skill_dir / resource).is_file()})
    for module in ("click", "prompt_toolkit"):
        checks.append({"kind": "python_module", "name": module,
                       "ok": importlib.util.find_spec(module) is not None})
    for backend in backends:
        executable = shutil.which(backend)
        checks.append({"kind": "backend", "name": backend,
                       "ok": executable is not None, "executable": executable})
    return {"ok": all(check["ok"] for check in checks), "checks": checks}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true", help="Emit JSON only")
    parser.add_argument("--backend", action="append", default=[],
                        help="Require an executable on PATH; repeat for multiple backends")
    args = parser.parse_args()
    report = diagnose(Path(__file__).resolve().parent.parent, args.backend)
    if args.json:
        print(json.dumps(report, indent=2))
    else:
        for check in report["checks"]:
            print(f"{'OK' if check['ok'] else 'MISSING'} {check['kind']}: {check['name']}")
    return 0 if report["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
