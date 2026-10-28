"""Optional bridge to the locally installed OpenClaw CLI."""
from __future__ import annotations
import os
import shutil
import subprocess


def ask_openclaw(prompt: str) -> str:
    """Call a preinstalled, already-configured OpenClaw CLI without a shell."""
    command = os.getenv("OPENCLAW_COMMAND", "openclaw").strip() or "openclaw"
    executable = shutil.which(command)
    if executable is None:
        return "Chưa tìm thấy OpenClaw CLI. Hãy cài đặt/cấu hình và kiểm tra PATH."
    try:
        timeout = max(1, int(os.getenv("OPENCLAW_TIMEOUT", "30")))
    except ValueError:
        timeout = 30
    try:
        result = subprocess.run([executable, "agent", "--message", prompt], capture_output=True,
            text=True, timeout=timeout, check=False, shell=False)
    except subprocess.TimeoutExpired:
        return f"OpenClaw không phản hồi trong {timeout} giây. Hãy thử lại."
    except OSError as exc:
        return f"Không thể khởi chạy OpenClaw: {exc}"
    output = (result.stdout or result.stderr).strip()
    if result.returncode != 0:
        detail = output or f"CLI thoát với mã {result.returncode}."
        return f"OpenClaw báo lỗi: {detail[:700]}"
    return output[:1200] if output else "OpenClaw không trả về nội dung."
