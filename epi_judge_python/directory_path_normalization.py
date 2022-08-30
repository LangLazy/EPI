from test_framework import generic_test


def shortest_equivalent_path(path: str) -> str:
    sep = path.split('/')
    start = ""
    if path[0] =='/':
        start = '/'
    stk = []
    for p in sep:
        if p == '' or p == '.':
            continue
        elif p == '..':
            if len(stk) == 0 or stk[-1] == "..":
                stk.append("..")
            else:
                stk.pop()            
        else:
            stk.append(p)
    return start + '/'.join(stk)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('directory_path_normalization.py',
                                       'directory_path_normalization.tsv',
                                       shortest_equivalent_path))
