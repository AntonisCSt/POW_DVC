import os

data_path = os.path.join('data','poem.txt')
def main():
    with open (data_path,'r') as f:
        print(f.read())

if __name__=='__main__':
    main()