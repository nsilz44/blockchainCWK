import numpy as np
import webbrowser
import time
import hashlib
import random
import pandas as pd
from datetime import datetime

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
    const tag = document.createElement("a");
    tag.href = URL.createObjectURL(blob);
    tag.download = "blockchain.txt";
    tag.click();
    URL.revokeObjectURL(tag.href);              
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

#q2()



########## Question 3 ##############


blockchain = []

def makeTransaction(by,to,product,quantity,best_before,batchId,transaction_count):
    transaction_count = transaction_count + 1
    return dict(by=by,to=to,product=product,quantity=quantity,bestbefore=best_before,batchId=batchId,transactionId=transaction_count),transaction_count


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
def createBlock(transaction_count,transactions,previous_Hash,nonce,target):
    # create parameters
    block_Id = len(blockchain)
    timestamp = int(time.time())
    actual_time = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    transaction_counts = len(transactions)
    # convert to little endian hex
    hex_block_ID = hex(block_Id)
    hex_block_ID = littleEndian('0x' + hex_block_ID[2:].zfill(8))
    hex_timestamp = hex(timestamp)
    hex_timestamp = littleEndian('0x' + hex_timestamp[2:].zfill(8))
    hex_transaction_count = hex(transaction_counts)
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
        "Timestamp" : actual_time,
        "Transaction count": transaction_count,
        "Previous block hash" : previous_Hash,
        "Target" : target,
        "Nonce" : hex_nonce,
        "Transaction hash": merkle,
        "Transactions" : transactions,
        "hash": block_Hash
    }
    blockchain.append(block)
    print('block ' + str(block_Id) + ' created at '+ actual_time)
    return block
#Genisis block
transactions = []
transaction_count = 0
transaction,transaction_count = makeTransaction('13W2KaWftxT3Gq1Vip31k4KadY9qdnbP96','16uiTiE6Wwnkzr6sSesAaTUJjSqNDTG2jQ','BlockyCoin',100,'',1,transaction_count)
transactions.append(transaction)
genisis = createBlock(transaction_count,transactions,'',121111,easy)
#print(blockchain)
# Second block
transactions = []
transaction,transaction_count = makeTransaction('13W2KaWftxT3Gq1Vip31k4KadY9qdnbP96','16uiTiE6Wwnkzr6sSesAaTUJjSqNDTG2jQ','Carrot',10,'10/02/23',1,transaction_count)
transactions.append(transaction)
transaction,transaction_count = makeTransaction('13W2KaWftxT3Gq1Vip31k4KadY9qdnbP96','16uiTiE6Wwnkzr6sSesAaTUJjSqNDTG2jQ','Carrot',20,'10/02/23',2,transaction_count)
transactions.append(transaction)
transaction,transaction_count = makeTransaction('13W2KaWftxT3Gq1Vip31k4KadY9qdnbP96','16uiTiE6Wwnkzr6sSesAaTUJjSqNDTG2jQ','Grape',10,'01/02/23',1,transaction_count)
transactions.append(transaction)
second_block = createBlock(transaction_count,transactions,blockchain[-1].get('hash'),121111,makeTarget(5))
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
        if now - start > 3600:
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


########## QUESTION 5 ##################
def searchByTransactionId(transaction_Id):
    for block in blockchain:
        if block.get('Transaction count') >= transaction_Id:
            transactions = block.get('Transactions')
            for transaction in transactions:
                if transaction.get('transactionId') == transaction_Id:
                    print(transaction)
                    break
            break
def searchByProduct(possible_transactions): 
    print('Type in the name of the product e.g "Grape", "Carrot", "BlockyCoin"')
    product = input('')
    probable_transactions = []
    for transaction in possible_transactions:
        if transaction.get('product') == product:
            probable_transactions.append(transaction)
    if len(probable_transactions) == 0:
        print('no product of that type in blockchain')
        searchByProduct(possible_transactions) 
    return probable_transactions

def searchBybatchId(probable_transactions):
    print('Type in the batchId')
    print('Or type in "dk" if you dont know')
    batchId = input('')
    if batchId != 'dk':
        couldbe_transactions = []
        for transaction in probable_transactions:
            if transaction.get('batchId') == batchId:
                probable_transactions.append(transaction)
        if len(probable_transactions) == 0:
            print('no batchId of that type in the blockchain')
            searchBybatchId(probable_transactions) 
    else:
        couldbe_transactions = probable_transactions
    return couldbe_transactions

def searchBybestbefore(probable_transactions):
    print('Type in the best before date in format DD/MM/YY')
    print('Or type in "dk" if you dont know')
    batchId = input('')
    if batchId != 'dk':
        couldbe_transactions = []
        for transaction in probable_transactions:
            if transaction.get('bestbefore') == batchId:
                probable_transactions.append(transaction)
        if len(probable_transactions) == 0:
            print('no bestbefore of that product in the blockchain')
            searchBybatchId(probable_transactions)
    else:
        couldbe_transactions = probable_transactions 
    return couldbe_transactions

def searchByAttributes():
    print('Type in the date of transaction in the format "YYYY-MM-DD HH:MM:SS"')
    print("Or If you dont know type in 'dk'")
    date = input('')
    possible_transactions = []
    if date != 'dk':
        try: 
            time.strptime(date, '%Y-%m-%d %H:%M:%S')
        except:
            print('wrong format or not a date')
            searchByAttributes()
        for block in blockchain:
            if block.get('Timestamp') == date:
                transactions = block.get('Transactions')
                for transaction in transactions:
                    possible_transactions.append(transaction)
    else: #'dk'
        for block in blockchain:
            transactions = block.get('Transactions')
            for transaction in transactions:
                possible_transactions.append(transaction)
    probable_transactions = searchByProduct(possible_transactions)
    probable_transactions = searchBybatchId(probable_transactions)
    probable_transactions = searchBybestbefore(probable_transactions)
    for transaction in probable_transactions:
        print(transaction)

            
#print(blockchain)
def q5(a):
# LIST OF WALLET ADDRESSES TO USE, PRIVATE KEYS, PSEUDONYMS
# 13W2KaWftxT3Gq1Vip31k4KadY9qdnbP96 , Kz51jD9BYq5P9yQhxZTZRFRBRCNRM8eiSZvv69PMqGRs6ByBapHu , A 
# 16uiTiE6Wwnkzr6sSesAaTUJjSqNDTG2jQ , L2jrhrBZrCK3nVChN4y9c1NCogSfA6LBYss9ZhrEywQHymewz2Bf , B 
# 1LAhVpGyjV66rosxJ2rwjpp9kjCA1mUuVc , Kxfj7vC9XMHxHqVvh39W53gcGjiZh75mcTvgUcDhJ3KdNCaUXRLJ , C 
# 1FPRF9JMDpCy7bABaEpSjCqavigUZAWs3Z , L3kJKL6GLAQzLDtJBfggVAwqnuXwoKLCqDvt9LDeDUdxmUwmZQhh , D 

    if a == 0:
        print("Here is the way to search and verify transactions")
    print("Type in the transaction ID. If you dont know type 'dk' ")
    try:
        transactionID = input('')
        if transactionID == 'dk':
            searchByAttributes()
            q5(0)
        transactionID = int(transactionID)
        if transactionID >= transaction_count:
            print('Too high a number')
            q5(1)
        elif transactionID == 0:
            print('transactionIDs start at 1')
            q5(1)
        else:
            searchByTransactionId(transactionID)    
    except ValueError:
        print('Not a whole number, try again')
        q5(1)
q5(0)



        