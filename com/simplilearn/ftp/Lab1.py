import ftplib

#https://dlptest.com/ftp-test/

HOSTNAME="ftp.dlptest.com"
USERNAME="dlpuser"
PASSWORD="rNrKYTX9g7z3RgJRmxWuGHbeu"

print("Start-Connet")
ftp_server=ftplib.FTP(HOSTNAME,USERNAME,PASSWORD)
print("End-Connet")

ftp_server.encoding="utf-8"

fileName="SBOO9.txt"

with open(fileName,"rb") as file:
    ftp_server.storbinary(f"STOR {fileName}",file)

ftp_server.dir()
ftp_server.quit()