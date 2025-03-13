from utils import unzip_with_7z
import string

zip_file_path = 'congrats.7z'  
dest_path = '.'  

find_me = ''  
secret_password = find_me + 'bcmpda'  

def find_password():
    letters = string.ascii_lowercase  
    for first in letters:
        for second in letters:
            
            password = first + second + 'bcmpda'
            print(f"Trying password: {password}")
            if unzip_with_7z(zip_file_path, dest_path, password):
                print(f"Password found: {password}")
                break
        else:
            continue
        break
if __name__ == "__main__":
    find_password()
