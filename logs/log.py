import inspect
import os
import logging

log_file_path = "logs/outputs/main.log"




def get_logger(name: str, log_file: str):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        handler = logging.FileHandler(log_file)
        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(message)s"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger


def _prefix():
    frame = inspect.stack()[2]
    file_name = os.path.basename(frame.filename)
    func_name = frame.function
    line_no = frame.lineno
    return f"[{file_name} -> {func_name}():{line_no}]\t"


def info(logger, *msg: str) -> None:
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
        logger.info((f"{prefix}{m}"))

def warning(logger, *msg: str) -> None:
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
        logger.warning((f"{prefix}{m}"))
        print(f"{prefix}    WARNING!       {msg}")

def error(logger, *msg: str) -> None:
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
        logger.error((f"{prefix}{m}"))
        print(f"{prefix}   !!!ERROR!!!     {msg}")
