import re
string = """hi abc@xyz.com , how are you ?"""
email = re.findall('\S+@\S+', string)
print(email)
