#!/usr/bin/env python3

import paramiko, os

t = paramiko.Transport('10.10.2.3', 22) 

t.connect(username='bender', password='alta3')

sftp = paramiko.SFTPClient.from_transport(t)

for x in os.listdir('/home/student/filestocopy/'):
    sftp.put(f'/home/student/filestocopy/{x}', f'/tmp/{x}')

sftp.close()


