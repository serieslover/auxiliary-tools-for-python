##  auxiliary tools to transform python files from 2.x to 3.x, when deploying old 2.x projects.
##  Author: XZhou,  19th April 2018

# encoding: UTF-8
import re

InputFile = r'F:\PythonSpace\ReansformPyfileFrom2xTo3x_example.py'
OutputFile = InputFile+'.py3x'

## First Step, update the function of print
print('start to replace "print xxx" by "print (xxx)"!')
with open(OutputFile, 'w') as ofd:
    with open(InputFile) as fd:
        while 1:
            line = fd.readline()
            if not line:
                break
            if re.match(r'^[ ]*print[ ]+.*', line):
                if not re.search('^[ ]*print[  ]*\(.*\)$', line):
                    splitlines = re.split(r'^([   ]*print[  ]+)(.*)([   ]*)$', line)
                    ofd.write(splitlines[1]+'('+splitlines[2]+splitlines[3]+')' + '\n')
                else:
                    ofd.write(line)
            else:
                ofd.write(line)
