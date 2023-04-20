# ssh-refused-pass-riskoo
iterator for sshpass when you have refused connection with hydra for not accept passwords in the command of connection

Realiza una iteración entre todos los usuarios y passwords , enviando una conexión a una ip y puerto con ssh. Todo lo hace a través de proxychains usando sshpass.

## Mi caso particular:

Estoy conectado mediante chisel a una computadora. Esta tiene conexción a otra por ssh por el puerto 2222.
Cuando ejecuto un hydra o un ataque de diccionario da fallos puesto que no acepta tener la contraseña en el mismo comando. Para solucionar esto estoy utilizando sshpass
Si no lo tienes.

```bash
apt-get insall sshpass
```

Además en mi caso , como dije antes , es el puerto 2222 .

Pues nada , pon tus usuarios en un archivo, create o usa un diccionario de passwords y ejecuta el POC, cambiando los diccionarios, la ip y el puerto.

Por dentro hará un:
```bash
proxychains sshpass -p {password} ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null -p {port} {user}@{host}
````
```bash
proxychains sshpass 

## Poc

```bash
python3.11 sshpass-proxy.py -U users -P /opt/100000.txt -H 192.168.11.11 --port 2222 
```

Espero que a alguien le pueda servir.
