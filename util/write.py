"""
This module is used to sort and display the output on console
"""


def write_display(final_dict):
    print('{')
    for key in sorted(final_dict.keys()):
        print('\t\t{}: {}'.format(key,final_dict[key]))
    print('}')
