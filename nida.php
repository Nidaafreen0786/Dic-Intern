<?php
function encrypt($data, $key) {
   
    $iv = '1234567890123456';
    
    $encrypted = openssl_encrypt($data, 'aes-128-cbc', $key, 0, $iv);
    
    return base64_encode($encrypted);
}

function decrypt($encryptedData, $key) {
   
    $encryptedData = base64_decode($encryptedData);
    $iv = '1234567890123456'; 
   
    return openssl_decrypt($encryptedData, 'aes-128-cbc', $key, 0, $iv);
}


$key = 'thisisasecretkey'; 
$data = 'Hello, secret message!';

$encryptedData = encrypt($data, $key);
echo "Encrypted: " . $encryptedData . "\n";

$decryptedData = decrypt($encryptedData, $key);
echo "Decrypted: " . $decryptedData . "\n";
?>