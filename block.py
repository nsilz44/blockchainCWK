import numpy as np
import webbrowser
import json
import time
import hashlib

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

#q2()



########## Question 3 ##############
blockchain = []
def createBlock(transactions,previous_Hash,nonce):
    block_Id = len(blockchain)
    timestamp = int(time.time())
    transaction_count = len(transactions)
    # convert to hex
    hex_block_ID = hex(block_Id)
    hex_timestamp = hex(timestamp)
    hex_transaction_count = hex(transaction_count)
    hex_nonce = hex(nonce)

    print(block_Id,timestamp,transaction_count,previous_Hash,nonce,transactions)
    print(hex_block_ID,hex_timestamp,hex_transaction_count,hex_nonce)
'''
    block = {
        "Block ID" : block_Id,
        "Timestamp" : timestamp,
        "Transaction count": transaction_count,
        "Previous block hash" : previous_Hash,
        "Nonce" : nonce,
        "Transactions" : transactions
        "hash": block_Hash
    }
    blockchain.append(block)'''

createBlock([{"a":'lol'}],11221,121111)