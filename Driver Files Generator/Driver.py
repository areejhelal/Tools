import os,sys
a=input('Please Enter Driver Name : ')
os.mkdir(a+'_driver')
os.chdir(a+'_driver')
file = open((a +'_interface.h'),'w')
file = open((a +'_config.h'),'w')
file = open((a +'_private.h'),'w')
file = open((a +'_register.h'),'w')
file = open((a +'_program.c'),'w')
file.write('#include "STD_TYPES.h"'+'\n')
file.write('#include "BIT_MATH.h"'+'\n')
file.write('#include "'+a+'_interface.h"'+'\n')
file.write('#include "'+a+'_config.h"'+'\n')
file.write('#include "'+a+'_register.h"'+'\n')
