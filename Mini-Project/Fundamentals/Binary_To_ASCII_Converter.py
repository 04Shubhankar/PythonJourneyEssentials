import binascii

# Create a byte string containing the text "Python for evryone"
Text = b"Python for evryone"

# Encode the byte string into a Base64-encoded string using the b2a_uu function
Ascii = binascii.b2a_uu(Text)

# Print the resulting Base64-encoded string
print(Ascii)
