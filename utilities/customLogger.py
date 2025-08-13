# import  logging # import looging package to create log
# import os
#
# class LogGen:
#
#     @staticmethod
#     def loggen():
#         # Ensure the Logs directory exists
#         # log_dir = ".\\Logs"
#         # if not os.path.exists(log_dir):
#         #     print(f"The directory '{log_dir}' does not exist. Creating it now...")
#         #     os.makedirs(log_dir)  # Create the directory
#         # else:
#         #     print(f"The directory '{log_dir}' already exists.")
#
#         logging.basicConfig(filename= ".\\Logs\\automation.log",
#                             format= '%(asctime)s: %(levelname)s: %(message)s', datefmt= '%m%d%Y %I:%M:%S %p')
#         logger = logging.getLogger()
#         logger.setLevel(logging.INFO)
# #         return logger     #whateber logger return here, will use in test cases
#
#
# import logging
# import os
#
#
# class LogGen:
#     @staticmethod
#     def loggen():
#         log_dir = ".\\Logs"
#
#         # Check if the directory exists, and create it if it doesn't
#         if not os.path.exists(log_dir):
#             os.makedirs(log_dir)
#             print(f"Directory '{log_dir}' created.")
#
#         # Configure logging: Log to file + Console
#         logging.basicConfig(
#             level=logging.INFO,  # Set the minimum level to INFO
#             format='%(asctime)s - %(levelname)s - %(message)s',
#             datefmt='%m%d%Y %I:%M:%S %p',
#             handlers=[
#                 logging.FileHandler(f"{log_dir}\\automation.log"),  # Log to file
#                 logging.StreamHandler()  # Log to console (optional)
#             ]
#         )
#
#         # Return the logger
#         logger = logging.getLogger()
#         return logger


import logging
import os

class LogGen:
    @staticmethod
    def loggen():
        logger = logging.getLogger("myLogger")
        logger.setLevel(logging.INFO)

        log_dir = "./Logs"
        if not os.path.exists(log_dir):   # to check directory is already exits or not
            os.makedirs(log_dir)      # for creating a diretory , if directory is not exits,

        # Create file handler
        log_file = os.path.join(log_dir, "automation.log")  # to ensure that you get correct path format ('.\\logs\\automation.log' is same)
        file_handler = logging.FileHandler(log_file, mode='a')   #mode = 'a' means open file in append mode so that new enetries will add in the end rather than overwriting it
        file_handler.setLevel(logging.INFO)

        # Create console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)

        # Formatter
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%m%d%Y %I:%M:%S %p')
        file_handler.setFormatter(formatter)     #Applies that format to the file handler — so logs written to the file will follow this format.
        console_handler.setFormatter(formatter)  #Applies the same format to the console output — so logs printed to the terminal will look the same.

        # Avoid duplicate handlers on re-run
        if not logger.handlers:
            logger.addHandler(file_handler)
            logger.addHandler(console_handler)

        return logger


# logger = LogGen.loggen()
# logger.info("This should show in both console and log file.")