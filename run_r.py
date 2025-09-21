import subprocess, sys, shlex, os
from pathlib import Path

RSCRIPT = r"C:\Program Files\R\R-4.4.2\bin\Rscript.exe"

def run_r(*args, timeout_sec: int = 1800, workdir: str | None = None, env: dict | None = None) -> int:
    cmd = [RSCRIPT, *map(str, args)]
    pretty = " ".join(shlex.quote(c) for c in cmd)
    print(f"[run_r] Running: {pretty}")

    proc_env = os.environ.copy()
    if env:
        proc_env.update(env)

    proc = subprocess.Popen(
        cmd,
        cwd=workdir,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        env=proc_env,
    )
    try:
        assert proc.stdout is not None
        for line in proc.stdout:
            print(line, end="")
        proc.wait(timeout=timeout_sec)
    except subprocess.TimeoutExpired:
        proc.kill()
        print(f"\n[run_r] ERROR: Timed out after {timeout_sec} seconds.", file=sys.stderr)
        return 124

    return proc.returncode

def run_r_expr(expr: str, timeout_sec: int = 1800, workdir: str | None = None, env: dict | None = None) -> int:
    return run_r("-e", expr, timeout_sec=timeout_sec, workdir=workdir, env=env)

if __name__ == "__main__":
    code = run_r("--version")
    sys.exit(code)
