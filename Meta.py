import os
from platform import architecture
if architecture()[0]=='64bit':os.system('pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests');os.system('git pull;chmod +x META;./META')
else:exit('\033[1;31m\n Sorry 32bit device not support ')
