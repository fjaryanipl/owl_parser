#!/usr/bin/env python
# coding: utf-8
import argparse
from argparse import RawTextHelpFormatter

def argument_parser():

    parser = argparse.ArgumentParser(
        description=__doc__,
        prog='mainowlparser.py',
        formatter_class=RawTextHelpFormatter
    )
    parser.add_argument(
        "-i",
        "--input",
        dest="input_file_path",
        required=True,
        help="a path to the input file."
    )
    parser.add_argument(
        "-o",
        "--output",
        dest="output_file_path",
        required=True,
        help="a path to the out file."
    )

    args = parser.parse_args()
    input_file_path = args.input_file_path
    output_file_path = args.output_file_path
#return the owlfile
    return input_file_path,output_file_path


#remove extra data
def remove(string):
    return string.replace(" ", "")
# parse the owl file
def ParseowlFile(owlfile):
#open the owl file
    f=open(owlfile,'r')
    lines=f.readlines()
    newlines=[]
    for i  in range(len(lines)):
        newline={}
        if "<oboInOwl:id>" in lines[i] and "<rdfs:label>" in lines[i+3]:
            s1_original=lines[i][21:-15]
            s2_original=lines[i+3][20:-14]
            s2=remove(linzes[i+3][20:-14]).replace('_','')
            s1=remove(lines[i][21:-15]).replace('_','')
            s2=remove(lines[i+3][20:-14]).replace('_','')
            if s1 != s2:
                newline['Term']='[term]'
                newline['id']= s1_original
                newline['name']= s2_original
                newlines.append(newline)
        else:
            if "<oboInOwl:id>" in lines[i] and "<rdfs:label>" in lines[i+2]:
                s1=remove(lines[i][21:-15]).replace('_','')
                s2=remove(lines[i+2][20:-14]).replace('_','')
                if s1 != s2:
                    newline['Term']='[term]'
                    newline['id']= s1
                    newline['name']= s2
                    newlines.append(newline)
    return newlines

# xmllist=ParseowlFile('dron.owl')


# In[4]:


def xmltoobo(xmllist,output_file_path):
    with open(output_file_path, 'w') as _outfile:
        for item in xmllist:
            for key, value in item.items():
                _outfile.write('{}:{}\n'.format(key,value))
                if key == 'name':
                            _outfile.write('\n')


def main():
#call argument parse
    input_file_path,output_file_path = argument_parser()
    xmllist=ParseowlFile(input_file_path)
    xmltoobo(xmllist,output_file_path)
if __name__=="__main__":
    main()





