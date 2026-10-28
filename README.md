# Roguelike Snake + OpenClaw

Dự án mẫu Python/Pygame tích hợp OpenClaw như trợ lý tùy chọn. Repo này là lớp tích hợp game, không sao chép toàn bộ mã nguồn OpenClaw.

## Tính năng
- Snake chạy bằng Pygame; di chuyển bằng mũi tên hoặc WASD.
- Nhấn H để yêu cầu OpenClaw gợi ý chơi; R để chơi lại; Esc để thoát.
- Game vẫn chạy nếu OpenClaw chưa được cài.

## Cài đặt (Windows PowerShell)

    py -m venv .venv
    .\.venv\Scripts\Activate.ps1
    python -m pip install -r requirements.txt
    Copy-Item .env.example .env
    python main.py

Nếu PowerShell chặn kích hoạt, chạy `.venv\Scripts\python.exe main.py`.

## OpenClaw (tùy chọn)
Cài đặt và cấu hình theo https://docs.openclaw.ai/start/getting-started rồi kiểm tra lệnh `openclaw` trong terminal. Phím H dùng OpenClaw CLI đã cấu hình sẵn. `OPENCLAW_COMMAND` mặc định là `openclaw`; `OPENCLAW_TIMEOUT` mặc định là 30 giây. Không lưu API key/token trong repo và không mở Gateway ra Internet chỉ để kết nối game.

## Tệp chính
- `main.py`: game Pygame
- `openclaw_bridge.py`: gọi CLI bằng subprocess, không dùng shell
- `requirements.txt`, `.env.example`, `.gitignore`

## Tham khảo
- OpenClaw: https://github.com/openclaw/openclaw
- Tài liệu OpenClaw: https://docs.openclaw.ai
- Pygame: https://www.pygame.org/docs/
