import numpy as np
import webbrowser
import time
import hashlib
import random
import pandas as pd

############## Question 2 ##########

### TO DO BEFORE RUNNING python parta.py#######
# git clone https://github.com/coinables/buidljs.git
# git clone https://github.com/davidshimjs/qrcodejs.git
def q2():
    file = open('Dapp.html', 'w')

    # the html code which will go in the file GFG.html
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <script src="buidljs/buidl.js"></script>
        <script src="qrcodejs/qrcode.js"></script>
        
        </head>
        <body>
        <script>
        function createKeys(letter){
        var letter = String(letter)
        var newPair = buidl.createFrom(letter);
        var address = newPair.p2pkh;
        var privateKey = newPair.pk;
        return {
            address: address,
            privateKey: privateKey,
        };
    }
    var A= createKeys('A_password');
    var B= createKeys('B_password');
    var C= createKeys('C_password');
    var D= createKeys('D_password');
    var accounts = String(A.address) + " , " + String(A.privateKey) + " , A " + String(B.address) + " , " + String(B.privateKey) + " , B " + String(C.address) + " , " + String(C.privateKey) + " , C "+ String(D.address) + " , " + String(D.privateKey) + " , D "
    console.log(accounts)
    var blob = new Blob([accounts],
                    { type: "text/plain;charset=utf-8" })
    saveAs(blob, "blockchain.txt");                
        </script>
        <h1>headers</h1>
        <div id="identities">
            <div>A</div>
            <div>B</div>
            <div>C</div>
            <div>D</div>
        </div>
        <h4>Public wallet address</h4>
        <div id="wallet address">
            <div id=a_address></div>
            <div id=b_address></div>
            <div id=c_address></div>
            <div id=d_address></div>
        </div>
        <h4>Private ID</h4>
        <div id="wallet address">
            <div id=a_pk></div>
            <div id=b_pk></div>
            <div id=c_pk></div>
            <div id=d_pk></div>
            </div>
        
        
    <script type="text/javascript">
    new QRCode(document.getElementById("a_address"), A.address);
    new QRCode(document.getElementById("b_address"), B.address);
    new QRCode(document.getElementById("c_address"), C.address);
    new QRCode(document.getElementById("d_address"), D.address);
    new QRCode(document.getElementById("a_pk"), A.privateKey);
    new QRCode(document.getElementById("b_pk"), B.privateKey);
    new QRCode(document.getElementById("c_pk"), C.privateKey);
    new QRCode(document.getElementById("d_pk"), D.privateKey);
    </script>
    </body>
        
    </html>
    """

    # writing the code into the file
    file.write(html)

    # close the file
    file.close()



    # open html file
    webbrowser.open('Dapp.html')

q2()



########## Question 3 ##############


blockchain = []

def makeTransaction(by,to,product,quantity,best_before,batchId):
    return dict(by=by,to=to,product=product,quantity=quantity,bestbefore=best_before,batchId=batchId)

def merkleHash(transactions):
    hashed_transactions = []
    for transaction in transactions:
        transaction_message = ""
        for x in transaction:
            transaction_message = transaction_message + str(transaction[x])
        hashed_transaction = hashlib.sha256(transaction_message.encode('utf-8')).hexdigest()
        hashed_transactions.append(hashed_transaction)
    while len(hashed_transactions) != 1:
        new_hashed_transactions = [] 
        for i in range(1,len(hashed_transactions),2):
            concated_hashes = hashed_transactions[i-1] + hashed_transactions[i]
            new_hashed_transaction = hashlib.sha256(concated_hashes.encode('utf-8')).hexdigest()
            new_hashed_transactions.append(new_hashed_transaction)
            if i + 2 == len(hashed_transactions):
                new_hashed_transactions.append(hashed_transactions[-1])
        hashed_transactions = new_hashed_transactions.copy()
    return hashed_transactions[0]
#print(merkleHash([dict(product="grape",lol='123'),dict(product="carrot",lol="122"),dict(product="carrot",lol="122"),dict(product="carrot",lol="122"),dict(product="carrot",lol="122")]))

def littleEndian(hex):
    a = hex[-2::-2]
    b = hex[::-2]
    new_hex = ''
    for i in range(0,len(hex)//2):
        new_hex= new_hex + a[i]
        new_hex= new_hex + b[i]
    if new_hex[-1] == 'x':
        new_hex = new_hex[:-2]
    return new_hex
def makeTarget(leading_zeros):
    f = (32-leading_zeros) * 'f'
    f = '0x' + f[:].zfill(32)
    return f
easy = makeTarget(3)
def createBlock(transactions,previous_Hash,nonce,target):
    # create parameters
    block_Id = len(blockchain)
    timestamp = int(time.time())
    transaction_count = len(transactions)
    # convert to little endian hex
    hex_block_ID = hex(block_Id)
    hex_block_ID = littleEndian('0x' + hex_block_ID[2:].zfill(8))
    hex_timestamp = hex(timestamp)
    hex_timestamp = littleEndian('0x' + hex_timestamp[2:].zfill(8))
    hex_transaction_count = hex(transaction_count)
    hex_transaction_count = littleEndian('0x' + hex_transaction_count[2:].zfill(8))
    hex_target = littleEndian(target)
    hex_nonce = hex(nonce)
    hex_nonce = '0x' + hex_nonce[2:].zfill(32)
    hex_nonced = littleEndian(hex_nonce)
    # find the merkle hash of the transactions
    merkle = hex(int(merkleHash(transactions),16))
    merkle = littleEndian('0x' + merkle[2:].zfill(32))
    hex_previous_Hash= littleEndian('0x' + previous_Hash[2:].zfill(32))
    #concat all the data
    concated_strings = hex_block_ID + hex_timestamp +hex_transaction_count+hex_previous_Hash+hex_target+hex_nonced+merkle
    # hash twice the concatenation then put it in littleEndian format
    first_hash = hashlib.sha256(concated_strings.encode('utf-8')).hexdigest()
    block_Hash = littleEndian(hashlib.sha256(first_hash.encode('utf-8')).hexdigest())
    block = {
        "Block ID" : block_Id,
        "Timestamp" : timestamp,
        "Transaction count": transaction_count,
        "Previous block hash" : previous_Hash,
        "Target" : target,
        "Nonce" : hex_nonce,
        "Transaction hash": merkle,
        "Transactions" : transactions,
        "hash": block_Hash
    }
    blockchain.append(block)
    return block
#Genisis block
genisis = createBlock([dict(product="grape",quantity=123)],'',121111,easy)
second_block = createBlock([dict(product="grape",lol='123'),dict(product="carrot",lol="122"),dict(product="carrot",lol="122"),dict(product="carrot",lol="122"),dict(product="carrot",lol="122")],blockchain[-1].get('hash'),121111,makeTarget(5))
#print(blockchain)


########### Question 4 ###########
def find_valid_nonce(target):
    target = int(target,0)
    start = time.time()
    current_nonce = int(makeTarget(0),0)
    max_nonce = current_nonce
    brute_force_attempts = 0
    while target < current_nonce:
        now = time.time()
        if now - start > 10:
            return current_nonce,'It’s very difficult to find nonce',brute_force_attempts
        current_nonce = random.randint(0,max_nonce)
        brute_force_attempts += 1
    finish = time.time()
    timed = finish - start
    return current_nonce, timed , brute_force_attempts

def q4(max_difficulty):
    time_df = pd.DataFrame()
    attempts_df = pd.DataFrame()
    for i in range(0,max_difficulty+1):
        timed = True
        difficulty = i
        n = 6
        for j in range(0,n):
            target = makeTarget(difficulty)
            transactions = [dict(by='lol',quantity=10)]
            valid_nonce,timed,brute_force_attempts = find_valid_nonce(target)
            if timed == 'It’s very difficult to find nonce':
                print(timed)
                break
            time_df.loc[j,i] = timed
            attempts_df.loc[j,i] = brute_force_attempts
            createBlock(transactions,blockchain[-1].get('hash'),valid_nonce,target)
        if timed == 'It’s very difficult to find nonce':
            break
    time_df.to_csv('time.csv')
    attempts_df.to_csv('bruteforce.csv')
#q4(15)    
#print(blockchain)
#print(timed,brute_force_attempts)

#def q5():