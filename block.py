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
	let newPair = buidl.createFrom("");
	let address = newPair.p2pkh;
	let privateKey = newPair.pk;
	console.log(address, privateKey);
	</script>
	<div id="qrcode"></div>
<script type="text/javascript">
new QRCode(document.getElementById("qrcode"), privateKey);
</script>
</body>
    
</html>
"""

# writing the code into the file
file.write(html)

# close the file
file.close()



# open html file
webbrowser.open('GFG.html')