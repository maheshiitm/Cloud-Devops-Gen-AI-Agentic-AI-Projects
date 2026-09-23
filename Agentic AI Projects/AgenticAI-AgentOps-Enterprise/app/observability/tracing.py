from contextlib import contextmanager
from time import perf_counter
import logging

logger = logging.getLogger("agenticai")

@contextmanager
def span(name, **attributes):
    start = perf_counter()
    logger.info("TRACE START %s %s", name, attributes)
    try:
        yield
    finally:
        logger.info("TRACE END %s duration_ms=%.2f", name, (perf_counter()-start)*1000)

def emit_metric(name, value, **labels):
    logger.info("METRIC %s=%s labels=%s", name, value, labels)
