
"""
    The 'pprint' module does not have an option to NOT order an object up until python 3.7
"""

#from pprint import pformat
from json import dumps

"""
    Requirements
    =============================================================================================
    
    * This function should be able to return a 'prettyfied' version of any python object 
      (ie: list, dictionary).     
"""
def prettylist(results, sort=False):
    if results == []:
        pass
    else:
        """
            This piece of code is meant to work with the pprint module
            ------------------------------------------------------------------------------------------
            lengths = []
            # The "%r %" along the string returns a string with two singles quotes (') in each side.
            for r in results: lengths.append(len("%r" % str(r)))
            width = max(lengths)+2
        """
        if sort == True:
            if type(results) == list:
                results.sort()
            elif type(results) == dict:
                results = sorted(results)
        return dumps(results, indent=4)
        """
            DATE: 03/23/2020 06:13
            - The "sort_dicts" attribute is not available for python version 3.7 as of the
              moment this comment was written.
        """
        #return pformat(results, width=width)


if __name__ == '__main__':
    print(f"\n {73 * '='}")
    print(f" {32 * ' '}           {32 * ' '}")
    print(f" {32 * ' '} PRETTY IT {32 * ' '}")
    print(f" {32 * ' '}           {32 * ' '}")
    print(f" {73 * '='}\n\n")