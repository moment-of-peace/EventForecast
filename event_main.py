#!/usr/bin/python3.5
import preprocessing as pr

columnToDel = [0,2,3,4,53,54,56,57]

clean_file_path = pr.del_columns('data-2013/', columnToDel)
print('cleaned file path: ' + clean_file_path)

# notice: after delete, column index of a attr will change !
attr_path = pr.get_specified_data(clean_file_path,[32],'Australia',22)
print('attr file path' + attr_path)
