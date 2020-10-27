import base64
import os


message = open(os.path.expanduser('~/.kube/config'), "r").read()

print("Kubeconfig => " + "\n" + "#-----------#" +"\n" + message + "\n" + "#-----------#" )

message_bytes = message.encode('UTF-8')
base64_bytes = base64.b64encode(message_bytes)
base64_message = base64_bytes.decode('UTF-8')

print(base64_message)

file = open("fileencode.txt", "w")
str_base64_message = repr(base64_message)
file.write(str_base64_message)
file.close()




f = open("fileencode.txt", "r")
config = ""
for line in f:
    config += line.split("\n")[0]
# print(config)
file = open("fileencode-split.txt", "w")
str_split_base64_message = repr(config)
file.write(str_split_base64_message)
file.close()
print(config)