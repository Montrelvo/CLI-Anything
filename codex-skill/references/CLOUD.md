# Codex in a cloud or managed environment

## What is installed

CLI-Anything teaches Codex to build, refine, test, validate, and discover command-line
harnesses for real software. Codex executes the workflow with its own tools.
Claude Code and Claude slash commands are not dependencies. Generated CLIs can be
called directly from the shell, including `--help` and `--json` modes.

This installation does not create or register an MCP server. A CLI harness and an
MCP transport are separate integrations. Do not report a CLI as an MCP tool, or
edit host MCP configuration without an actual server and a supported registration
mechanism. A managed ChatGPT session may not expose newly installed local servers
in its connector tool list.

## Install

From a full checkout, use the standard installer for local Codex:

```bash
bash codex-skill/scripts/install.sh
```

For managed hosts, use the host's supported skill installation workflow. When that
workflow provides a writable skill checkout, the installer can populate it:

```bash
bash codex-skill/scripts/install.sh --dest-root /absolute/managed/skills-checkout
```

PowerShell supports the equivalent `-DestRoot` parameter. The destination contains
`cli-anything/`, with the full methodology and helpers bundled. Existing skills
are never overwritten. Complete any host-required validation and saving steps;
copying into a cloud filesystem alone does not guarantee persistence or discovery.
Refresh the host skill list if necessary. An already running agent can read the
installed `SKILL.md` directly; do not promise immediate automatic discovery.

## Check capabilities before using a target

Run the bundled, read-only diagnostic with the Python interpreter that will run
the harness:

```bash
python3 /path/to/cli-anything/scripts/doctor.py --json --backend godot
```

Without `--backend`, it checks the installed methodology resources and basic Python
modules. Specify `--backend blender`, for example, to require that executable.
It performs no installs, network requests, or configuration changes. Exit status
0 means the requested checks passed; 1 means a requirement is missing. An executable
on PATH still needs a real workflow test to establish backend compatibility.

Use an isolated Python environment for target packages:

```bash
python3 -m venv /absolute/workspace/cli-anything-venv
/absolute/workspace/cli-anything-venv/bin/python -m pip install -e ./godot/agent-harness pytest
/absolute/workspace/cli-anything-venv/bin/cli-anything-godot --help
CLI_ANYTHING_FORCE_INSTALLED=1 /absolute/workspace/cli-anything-venv/bin/python -m pytest \
  ./godot/agent-harness/cli_anything/godot/tests -q
```

Put the environment's `bin` directory on PATH when subprocess tests require an
installed command. Use an environment outside the source tree, and save a setup
recipe in the target repository if the cloud environment is temporary.

Prefer one-shot subcommands in non-interactive cloud execution. Keep prompts,
progress output, and REPL sessions out of machine-readable JSON output.

## Report actual limits

Check real backends, display/headless support, network access, service credentials,
and export templates as needed for the requested target. Do not install every
bundled application just to install the builder. A missing backend blocks its real
E2E tests; record that limitation rather than substituting fake output. Existing
repository test counts are historical claims, not results of the current run.

Use the session's connected services and supported browser controls where required
by the host. A generated CLI does not grant new credentials, network permissions,
or permission to bypass those controls.
