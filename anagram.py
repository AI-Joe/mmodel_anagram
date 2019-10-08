import sys

def isAnagram(str1, str2):
    if(''.join(reversed(str1)) == str2):
        return True
    return False

if __name__ == '__main__':
    print(isAnagram(sys.argv[1],sys.argv[2]))