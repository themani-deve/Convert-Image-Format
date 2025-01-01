from PIL import Image
from Authentication import login, register


# Convert Format Image Section

def converting():
    image_path = input('Enter Your Image Path: ')
    if image_path.endswith('.webp'):
        img = Image.open(image_path)
        if img:
            print('1.jpg', '2.png', )
            new_format = input('Be Che Formati Tabdil Beshe? ')
            str_new_format = str(new_format.lower())
            if str_new_format == '1' or str_new_format == 'jpg':
                remove_word = '.webp'
                output_path = image_path.replace(remove_word, '.jpg')
                if img.mode == 'RGBA':
                    img = img.convert('RGB')
                    img.save(output_path, 'JPEG')
                else:
                    img.save(output_path, 'JPEG')
            elif str_new_format == '2' or str_new_format == 'png':
                remove_word = '.webp'
                output_path = image_path.replace(remove_word, '.png')
                if img.mode == 'RGBA':
                    img = img.convert('RGB')
                    img.save(output_path, 'PNG')
                else:
                    img.save(output_path, 'PNG')
            else:
                print('We Cannot Convert To Your Format Selected!')
        else:
            print('Your Path Not Correct!')
    elif image_path.endswith('.jpg'):
        img = Image.open(image_path)
        if img:
            print('1.png', '2.webp')
            new_format = input('Be Che Formati Tabdil Beshe? ')
            str_new_format = str(new_format.lower())
            if str_new_format == '1' or str_new_format == 'png':
                remove_word = '.jpg'
                output_path = image_path.replace(remove_word, '.png')
                if img.mode == 'RGBA':
                    img = img.convert('RGB')
                    img.save(output_path, 'PNG')
                else:
                    img.save(output_path, 'PNG')
            elif str_new_format == '2' or str_new_format == 'webp':
                remove_word = '.jpg'
                output_path = image_path.replace(remove_word, '.webp')
                if img.mode == 'RGB':
                    img = img.convert('RGBA')
                    img.save(output_path, 'WEBP')
                else:
                    img.save(output_path, 'WEBP')
            else:
                print('We Cannot Convert To Your Format Selected!')
        else:
            print('Your Path Not Correct!')
    elif image_path.endswith('.png'):
        img = Image.open(image_path)
        if img:
            print('1.jpg', '2.webp')
            new_format = input('Be Che Formati Tabdil Beshe? ')
            str_new_format = str(new_format.lower())
            if str_new_format == '1' or str_new_format == 'jpg':
                remove_word = '.png'
                output_path = image_path.replace(remove_word, '.jpg')
                if img.mode == 'RGBA':
                    img = img.convert('RGB')
                    img.save(output_path, 'JPEG')
                else:
                    img.save(output_path, 'JPEG')
            elif str_new_format == '2' or str_new_format == 'webp':
                remove_word = '.png'
                output_path = image_path.replace(remove_word, '.webp')
                if img.mode == 'RGB':
                    img = img.convert('RGBA')
                    img.save(output_path, 'WEBP')
                else:
                    img.save(output_path, 'WEBP')
            else:
                print('We Cannot Convert To Your Format Selected!')
        else:
            print('Your Path Not Correct!')
    else:
        print('Cant Convert This Format To Any!!!')


print('1.Login', '2.Register')
authentication_input = input('Select One of The List: ')
str_authentication_input = str(authentication_input.lower())

if str_authentication_input == '1' or str_authentication_input == 'login':
    login()
    converting()
elif str_authentication_input == '2' or str_authentication_input == 'register':
    register()
    converting()
