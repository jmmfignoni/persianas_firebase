from ota_update.main.ota_updater import OTAUpdater


def download_and_install_update_if_available():
    token = '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'
    ota_updater = OTAUpdater('https://github.com/jmmfignoni/persianas_firebase', headers={'Authorization': 'token {}'.format(token)})
    ota_updater.download_and_install_update_if_available('wifi-ssid', 'wifi-password')

def start():
    # your custom code goes here. Something like this: ...
    # from main.x import YourProject
    # project = YourProject()
    # ...
    print('Version 1')
    
def boot():
    download_and_install_update_if_available()
    start()


boot()
