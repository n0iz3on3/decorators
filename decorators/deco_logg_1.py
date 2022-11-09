import logging


def logger(old_function):

    def new_function(*args, **kwargs):
        result = old_function(*args, **kwargs)
        name = old_function.__name__
        arguments = f'{args} {kwargs}'
        msg_format = f'{name} - {arguments} - {result}'

        Log_Format = "%(levelname)s %(asctime)s - %(message)s"
        logging.basicConfig(filename = 'main.log',
                            filemode = "w",
                            format = Log_Format, 
                            level = logging.INFO)
        
        logger = logging.getLogger()
        logger.info(msg_format)
            
        return result

    return new_function