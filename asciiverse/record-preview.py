#!/usr/bin/env python3
"""Records asciiverse/sssnake.cast, the catalog preview, at 100x30
(hub/RECORDING.md): the snake playing itself in autopilot mode at speed
18 on a walled 30 by 24 board (60x24 on screen) with the size shown, the
--try-hard 2 solver keeping it alive, for about 45 seconds, then q. A
board the size of the whole terminal looked empty: the snake reached
only 29 in that time, against about 77 here.

sssnake is named by bare command, so the cast's header holds no local
path. Usage, from the repo root with a build in out/ (or sssnake on
PATH), under a memory cap:
  systemd-run --user --scope -p MemoryMax=4G python3 asciiverse/record-preview.py
Any extra argument is used as the cast's path instead (for test runs)."""
import fcntl, os, pty, select, struct, sys, termios, time

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
cast = sys.argv[1] if len(sys.argv) > 1 else f"{root}/asciiverse/sssnake.cast"
COLS, ROWS, PLAY = 100, 30, 45.0
env = dict(os.environ, TERM="xterm-256color", COLORTERM="truecolor", LANG="C.UTF-8",
           PATH=f"{root}/out:{os.environ['PATH']}")
for v in ("VTE_VERSION", "TERM_PROGRAM", "TERM_PROGRAM_VERSION", "TMUX"):
    env.pop(v, None)

pid, fd = pty.fork()
if pid == 0:
    os.execvpe("asciinema", ["asciinema", "rec", "--overwrite", "-q", "--idle-time-limit", "2",
        "--window-size", f"{COLS}x{ROWS}", "--capture-env", "TERM,COLORTERM,LANG",
        "--title", "sssnake",
        "--command", "sssnake -m autopilot -s 18 -z -x 30 -y 24 --try-hard 2", cast], env)
fcntl.ioctl(fd, termios.TIOCSWINSZ, struct.pack("HHHH", ROWS, COLS, 0, 0))


def pump(seconds):
    end = time.time() + seconds
    while time.time() < end:
        r, _, _ = select.select([fd], [], [], 0.05)
        if r:
            try:
                os.read(fd, 65536)
            except OSError:
                return


pump(PLAY)
os.write(fd, b"q")
for _ in range(50):
    if os.waitpid(pid, os.WNOHANG)[0]:
        break
    pump(0.2)
