# Deadlock-encryption-messenger



Currently available for linux users.

A python based end-to-end encrypted messenger and text and file encryption tool. It uses RSA asymmetric encryption to encrypt text and file and your messages. 
Keys for text and file encryption are generated within the deadlock program.

Encrypted text is saved in a text file in 'Documents/encrypted_text' and while decrypting the encrypted bytes are read from that file and dislpayed after decryption.
Files are encrypted and saved by file's original name and .encrypted extension.

Messenger generates its own unique key for every session and then sends it automatically to your contact. You can send text and file messages using the messenger. You can run messenger within the deadlock or you can just run "chatbox.py" from terminal. 

Chats of every session will be deleted as the connection is terminated but if you want to save your chats just run 'record()' command while chatting it will start recording messaged sent and received there on. Recording will be saved in 'Documents\Chat_recording' directory.

To send files just type 'send() file_name'

## Installation

```bash
  sudo python3 setup.py
```
Installs necessary packages

```bash
  chatbox.py
```
To run messenger

```bash
  deadlock.py
```
To use text or file encryption from anywhere.

## Support

For support, email deadlock_chatbox@proton.me

Stay tuned for regular updates

Last update: 17-9-2022
