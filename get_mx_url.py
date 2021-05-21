import meraki
import time
import bs4
import pickle

bs = bs4.BeautifulSoup


def store_id():
    API_KEY = ''
    org_id = ''
    dashboard = meraki.DashboardAPI(API_KEY)
    n = dashboard.organizations.getOrganizationNetworks(org_id, total_pages='all')
    stores = []

    for e in n:
        s = e['id'], e['name'], e['tags']
        stores.append(s)

    urls = []

    for id in stores:

        devicess = dashboard.networks.getNetworkDevices(id[0])
        for d in devicess:
            if 'MX' in d['model']:
                try:
                    if 'merakiname' in d['name']:
                        net_dev = d['url'], d['serial'], id[1]
                        urls.append([net_dev])
                        time.sleep(1)
                except:
                    continue
                else:
                    continue

            else:
                continue

    file = open('pmx.pkl', 'wb')
    pickle.dump(urls, file)
    file.close()


store_id()
