import inspect
import os
import logging

log_file_path = "logs/outputs/main.log"

def configure_logger(log_file: str = log_file_path) -> None:
    """Configures the logger to write to a file with a specific format."""
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s"
    )


def info(*msg: str) -> None:
    # Caller info (1 level up the stack)
    frame = inspect.stack()[1]
    file_name = os.path.basename(frame.filename)
    func_name = frame.function
    line_no = frame.lineno

    # Prefix
    prefix = (
        f"[{file_name} -> {func_name}():{line_no}]\t\t"
    )

    for m in msg:
        logging.info((f"{prefix}{m}"))

def warning(*msg: str) -> None:
    # Caller info (1 level up the stack)
    frame = inspect.stack()[1]
    file_name = os.path.basename(frame.filename)
    func_name = frame.function
    line_no = frame.lineno

    # Prefix
    prefix = (
        f"[{file_name} -> {func_name}():{line_no}]\t\t"
    )

    for m in msg:
        logging.warning((f"{prefix}{m}"))
        print(f"{prefix}    WARNING!       {msg}")

def error(*msg: str) -> None:
    # Caller info (1 level up the stack)
    frame = inspect.stack()[1]
    file_name = os.path.basename(frame.filename)
    func_name = frame.function
    line_no = frame.lineno

    # Prefix
    prefix = (
        f"[{file_name} -> {func_name}():{line_no}]\t\t"
    )

    for m in msg:
        logging.error((f"{prefix}{m}"))
        print(f"{prefix}   !!!ERROR!!!     {msg}")
