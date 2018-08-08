Str = "this is string example....wow!!!";
Str = Str.encode(encoding='base64', errors='strict')

print ("Encoded String: " , Str)
print ("Decoded String: " , Str.decode('base64','strict'))