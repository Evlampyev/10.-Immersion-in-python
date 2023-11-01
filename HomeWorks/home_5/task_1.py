def get_file_info(file_path: str) -> tuple:
    ind_slash = file_path.rfind('/')
    path = file_path[:ind_slash + 1]
    ind_punkt = file_path.rfind('.')

    if ind_punkt == -1:
        expansion = file_path[ind_slash + 1:]
        only_name = ''
    else:
        expansion = file_path[ind_punkt:]
        only_name = file_path[ind_slash + 1:ind_punkt]
    result = (path, only_name, expansion)
    return result


print(get_file_info('C:/Users/User/Documents/example.txt'))
