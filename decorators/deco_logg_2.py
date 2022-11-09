from time import localtime, asctime


def logger_with_args(path):

    def logger(old_function):
    
        def new_function(*args, **kwargs):
            local_time = localtime()
            pretty_time = asctime(local_time)
            result = old_function(*args, **kwargs)
            name = old_function.__name__
            arguments = f'{args} {kwargs}'
            msg_format = f'{name} - {arguments} - {result}'
    
            with open(path, 'a', encoding='utf-8') as log_file:
                report = f'{pretty_time} - {msg_format}\n'
                log_file.write(report)
                
            return result
    
        return new_function

    return logger