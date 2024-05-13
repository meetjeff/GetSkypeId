from skpy import Skype
# from dotenv import load_dotenv
# import os

def get_account():
    try:
        # load_dotenv()
        # username = os.getenv('skype_username')
        # password = os.getenv('skype_password')
        username = input("Enter Skype Account : ")
        password = input("Password : ")

        return(username, password)
    except:
        print("get account info failed")

def login_sk(username, password):
    try:
        sk_account = Skype(username, password)
        return sk_account
    except:
        print("login failed")

def get_id_dict(sk_account):
    try:
        id_list = dict()
        while True:
            groups = sk_account.chats.recent()
            if len(groups) == 0 :
                break
            else:
                for n in groups:
                    if n[:2] == '19':
                        id_list[groups[n].topic] = groups[n].id
        return id_list
    except:
        print("get id list failed")

def print_each_group(id_list):
    try:
        for id in id_list:
            print("Group: ", id)
            print("Chat_ID: ", id_list[id])
            print("==========================================================")
    except:
        print("id_list has problem")

if __name__ == '__main__':
    username, password = get_account()
    sk_account = login_sk(username, password)
    id_list = get_id_dict(sk_account)
    print_each_group(id_list)
    print(id_list)
