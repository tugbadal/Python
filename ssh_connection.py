# -*- coding: utf-8 -*-
import os
import paramiko

class SSHConnection:
    server = ""
    username = ""
    password = ""
    ssh = None
    stdin = None
    stdout = None
    stderr = None

    def __init__(self, server, username, password):
        self.server = server
        self.username = username
        self.password = password
        # self.port = '22' # default port
        self.ssh = None

    def login(self):
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(self.server, username=self.username, password=self.password)

    def logout(self):
        self.ssh.close()

    def run_command(self, command):
        ssh_stdin, ssh_stdout, ssh_stderr = self.ssh.exec_command(command)
        self.stdout = ssh_stdout.read()
        self.stderr = ssh_stderr.read()

        print "stdout:\n", self.stdout
        print "error: ", len(self.stderr)

# Örnek kullanım senaryosu
#a=SSHConnection("ip ","username","password")
#a.login()
#a.run_command("ls -l")
#a.logout()

