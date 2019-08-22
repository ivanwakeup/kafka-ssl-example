

days=100

keytool -keystore server.keystore.jks -alias localhost -validity $days -genkey -keyalg RSA
