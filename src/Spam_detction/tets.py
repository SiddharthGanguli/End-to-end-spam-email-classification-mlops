from Spam_detction.logger import setup_logger

logger = setup_logger("test", "test.log")
logger.info("IF YOU SEE THIS, LOGGING WORKS")

print("Script ran")
