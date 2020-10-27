import base64

message = open("~/.kube/config")
message_bytes = message.encode('ascii')
base64_bytes = base64.b64encode(message_bytes)
base64_message = base64_bytes.decode('ascii')

print(base64_message)

base64_message = file.write('fileencode.txt')
file.close()

print(base64_message)


f = open("fileencode.txt", "r")
config = ""
for line in f:
    config += line.split("\n")[0]
print(config)