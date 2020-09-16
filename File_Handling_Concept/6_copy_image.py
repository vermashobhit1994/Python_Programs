#program to copy image
input_filename = 'Image_to_be_copied.jpg'
output_filename = 'copied_image.jpg'

fd_input = open(input_filename,mode = 'rb')#read the image in binary i.e 'b'

fd_output = open(output_filename ,mode = 'wb')
for byte_data in fd_input:
    fd_output.write(byte_data)

