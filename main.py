import os

import lxml
import lxml.etree as et

# The utility makes pretty print xml file/files out of a minified xml file or files
# Input and output directories has to be separate
inp_dir = r'xml_samples'
output_dir = r'output'


def beautify_one_file(full_input_file_path_, output_file_):
    tree = lxml.etree.parse(full_input_file_path_)
    pretty = lxml.etree.tostring(tree, encoding="UTF-8", pretty_print=True, xml_declaration=True)
    f = open(output_file_, 'wb')
    f.write(pretty)
    f.close()


def beautify_many_files(input_dir_path_, output_dir_path_, beautify_one_file_):
    for root, dirs, files in os.walk(input_dir_path_):
        for inp_file in files:
            inp_file_abs_path = os.path.join(root, inp_file)
            out_file = output_dir_path_ + '\\' + inp_file
            beautify_one_file_(inp_file_abs_path, out_file)


beautify_many_files(inp_dir, output_dir, beautify_one_file)
