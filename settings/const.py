from urllib2 import HTTPBasicAuthHandler, build_opener, install_opener

#Database settings
database_connect = "dbname='ridprod'"
kv1_database_connect = "dbname='kv1tmp'"
iff_database_connect = "dbname='ifftmp'"
pool_generation_enabled = False
import_arriva_trains = False

# Subscribe to https://ndovloket.nl/aanvragen/
#
# username and password can be found here:
# https://groups.google.com/forum/#!topic/ndovloket-meldingen/IxEPpXds_Qo

#NDOVLoket settings
ndovloket_url = "data.ndovloket.nl"
ndovloket_user = None
ndovloket_password = None

if not ndovloket_user or not ndovloket_password:
    print("Subscribe to https://ndovloket.nl/aanvragen/\n\nusername and password can be found here:\nhttps://groups.google.com/forum/#!topic/ndovloket-meldingen/IxEPpXds_Qo")

auth_handler = HTTPBasicAuthHandler()
auth_handler.add_password(realm=ndovloket_url,
                          uri=ndovloket_url,
                          user=ndovloket_user,
                          passwd=ndovloket_password)
opener = build_opener(auth_handler)
install_opener(opener)
