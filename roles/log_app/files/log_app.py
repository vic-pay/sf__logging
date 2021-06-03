#!/bin/env python3

import sys, logging

if __name__ == '__main__':

    logging.basicConfig(
        level=logging.INFO,
        format='{"time": "%(asctime)s", "level": "%(levelname)s", "message": "%(message)s"}',
        handlers=[
            logging.FileHandler("/var/log/log_app.log"),
            logging.StreamHandler()
        ]
    )

    if len(sys.argv) != 2:
        logging.error("One arg required. Exiting")
        sys.exit(1)
    
    if not sys.argv[1].isdigit():
        logging.error("Input is not number. Exiting")
        sys.exit(2)

    input  = int(sys.argv[1])
    result = input * 2
    logging.info(f"Success. Input is {input}. Result is {result}")