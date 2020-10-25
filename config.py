# File: config.py
# Aim: Maintaince the config and logging of the package

# %%
# Imports
import configparser
import logging
import logging.config
import os
import pandas as pd

# %%


def beside(name):
    return os.path.join(os.path.dirname(__file__), name)


class Config(object):
    def __init__(self):
        pass

    def load_logger(self, log_filepath='./logfile.log', name='root', cfg_path=None):
        # Load logger from config
        if cfg_path is None:
            cfg_path = beside('logging.ini')

        logging.config.fileConfig(cfg_path,
                                  defaults={'log_filepath': log_filepath})

        logger = logging.getLogger(name)

        self.logger = logger
        self.logger.info(f'Logger initialized as "{name}" using "{cfg_path}"')

    def reload_cfg(self, cfg_path=None):
        if cfg_path is None:
            cfg_path = beside('logging.ini')

        self.config = pd.DataFrame()
        # Load config from config
        parser = configparser.RawConfigParser()
        parser.read(cfg_path)
        # Read sections
        for section in parser.sections():
            # Read options
            for option in parser.options(section):
                self.append(section, option, parser.get(section, option))
        # Report what we got
        self.logger.debug('Configure is loaded: \n{}'.format(
            self.config.to_string()))

    def append(self, section, option, value):
        self.config = self.config.append(pd.Series(dict(SECTION=section,
                                                        OPTION=option,
                                                        VALUE=value)),
                                         ignore_index=True)
        self.logger.debug(
            f'Append new config: "{section}":"{option}" as "{value}"')

    def display(self):
        # Display the config
        print(self.config)

    def query(self, section, option, ignore_not_found=True):
        # Query in the config
        result = self.config.query(
            f'SECTION=="{section}" & OPTION=="{option}"')
        num = len(result)

        # No result found
        if num == 0:
            self.logger.error(
                f'No records found for {section}: {option}')
            if ignore_not_found:
                # Ignore the notFound error
                return None
            else:
                raise Exception(f'No records found for {section}: {option}')

        # Found more than one record
        if num > 1:
            self.logger.warning(
                f'Multiple ({num}) records found for {section}: {option}')

        return result.iloc[-1].VALUE


# %%
