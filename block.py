import numpy as np
import webbrowser

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