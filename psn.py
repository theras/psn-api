import json
import re
import requests

from bs4 import BeautifulSoup


class Psn(object):
    def __init__(self):
        self._basic_username = 'c7y-basic01'
        self._basic_password = 'A9QTbosh0W0D^{7467l-n_>2Y%JG^v>o'
        self._trophy_username = 'c7y-trophy01'
        self._trophy_password = "jhlWmT0|:0!nC:b:#x/uihx'Y74b5Ycx"
        self._firmware = None
        request = requests.get("http://fus01.ps3.update.playstation.net/update/ps3/list/us/ps3-updatelist.txt")
        content = request.text
        version = re.findall('\;SystemSoftwareVersion=(.*?)00\;', content)
        self._firmware = ''.join(version)

    def jid(self, psn_id):
        urls = {
            'us': 'http://searchjid.usa.np.community.playstation.net/basic_view/func/search_jid',
            'gb': 'http://searchjid.eu.np.community.playstation.net/basic_view/func/search_jid',
            'jp': 'http://searchjid.jpn.np.community.playstation.net/basic_view/func/search_jid',
        }
        headers = {
            'User-Agent': 'PS3Community-agent/1.0.0 libhttp/1.0.0',
            'Content-Types': 'Content-Type: text/xml; charset=UTF-8',
        }
        data = "<?xml version='1.0' encoding='utf-8'?><searchjid platform='ps3' sv='{firmware}'><online-id>{psn_id}</online-id></searchjid>".format(firmware=self._firmware, psn_id=psn_id)
        jid = list()
        for region, url in urls.iteritems():
            request = requests.post(
                url,
                headers=headers,
                auth=requests.auth.HTTPDigestAuth(self._basic_username, self._basic_password),
                data=data,
            )
            xml = BeautifulSoup(request.text, 'lxml')
            jids = dict()
            jids['region'] = region
            jids['jid'] = xml.find('jid').text
            jid.append(jids)
        return jid

    def profile(self, jid):
        headers = {
            'User-Agent': 'PS3Community-agent/1.0.0 libhttp/1.0.0',
            'Content-Types': 'Content-Type: text/xml; charset=UTF-8',
        }
        data = "<profile platform='ps3' sv='{firmware}'><jid>{jid}</jid></profile>".format(firmware=self._firmware, jid=jid['jid'])
        request = requests.post(
            "http://getprof.{region}.np.community.playstation.net/basic_view/func/get_profile".format(region=jid['region']),
            headers=headers,
            auth=requests.auth.HTTPDigestAuth(self._basic_username, self._basic_password),
            data=data,
        )
        xml = BeautifulSoup(request.text, 'lxml')
        profile = dict()
        profile['online_name'] = xml.find('onlinename').text
        profile['country'] = xml.find('country').text
        profile['about_me'] = xml.find('aboutme').text
        profile['avatar_url'] = xml.find('avatarurl').text
        profile['color'] = xml.find('ucbgp').text[-8:]
        profile['psn_plus'] = xml.find('plusicon')
        return json.dumps(profile, indent=4, separators=(',', ': '))

    def trophies(self, jid):
        headers = {
            'User-Agent': 'PS3Application libhttp/3.5.5-000 (CellOS)',
            'Content-Types': 'Content-Type: text/xml; charset=UTF-8',
        }
        data = "<nptrophy platform='ps3' sv='{firmware}'><jid>{jid}</jid></nptrophy>".format(firmware=self._firmware, jid=jid['jid'])
        request = requests.post(
            "http://trophy.ww.np.community.playstation.net/trophy/func/get_user_info",
            headers=headers,
            auth=requests.auth.HTTPDigestAuth(self._trophy_username, self._trophy_password),
            data=data,
        )
        xml = BeautifulSoup(request.text, 'lxml')
        trophies = dict()
        trophies['points'] = xml.find('point').text
        trophies['level'] = xml.find('level').text
        trophies['levels'] = dict()
        trophies['levels']['base'] = xml.find('level')['base']
        trophies['levels']['next'] = xml.find('level')['next']
        trophies['levels']['progress'] = xml.find('level')['progress']
        trophies['types'] = dict()
        trophies['types']['platinum'] = xml.find('types')['platinum']
        trophies['types']['gold'] = xml.find('types')['gold']
        trophies['types']['silver'] = xml.find('types')['silver']
        trophies['types']['bronze'] = xml.find('types')['bronze']
        return json.dumps(trophies, indent=4, separators=(',', ': '))

    def games(self, jid):
        ''' Returns game id and trophies for a user. '''
        headers = {
            'User-Agent': 'PS3Application libhttp/3.5.5-000 (CellOS)',
            'Content-Types': 'Content-Type: text/xml; charset=UTF-8',
        }
        data = "<nptrophy platform='ps3' sv='{firmware}'><jid>{jid}</jid><start>1</start><max>1</max></nptrophy>".format(firmware=self._firmware, jid=jid['jid'])
        auth = requests.auth.HTTPDigestAuth(self._trophy_username, self._trophy_password)
        request = requests.post(
            "http://trophy.ww.np.community.playstation.net/trophy/func/get_title_list",
            headers=headers,
            auth=auth,
            data=data,
        )
        xml = BeautifulSoup(request.text, 'lxml')
        game_count = int(xml.find('title').text)
        games = list()
        for gc in xrange(1, game_count+1):
            data = "<nptrophy platform='ps3' sv='{firmware}'><jid>{jid}</jid><start>{gc}</start><max>64</max></nptrophy>".format(firmware=self._firmware, jid=jid['jid'], gc=gc)
            request = requests.post(
                "http://trophy.ww.np.community.playstation.net/trophy/func/get_title_list",
                headers=headers,
                auth=auth,
                data=data,
            )
            xml = BeautifulSoup(request.text, 'lxml')
            game = dict()
            game['npcommid'] = xml.find('info')['npcommid']
            game['last_updated'] = xml.find('last-updated').text
            game['trophies'] = dict()
            game['trophies']['platinum'] = xml.find('types')['platinum']
            game['trophies']['gold'] = xml.find('types')['gold']
            game['trophies']['silver'] = xml.find('types')['silver']
            game['trophies']['bronze'] = xml.find('types')['bronze']
            games.append(game)
        return json.dumps(games, indent=4, separators=(',', ': '))

    def game_trophies(self, jid, npcommid):
        headers = {
            'User-Agent': 'PS3Application libhttp/3.5.5-000 (CellOS)',
            'Content-Types': 'Content-Type: text/xml; charset=UTF-8',
        }
        data = "<nptrophy platform='ps3' sv='{firmware}'><jid>{jid}</jid><list><info npcommid='{npcommid}'><target>FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF</target></info></list></nptrophy>".format(firmware=self._firmware, jid=jid['jid'], npcommid=npcommid)
        request = requests.post(
            "http://trophy.ww.np.community.playstation.net/trophy/func/get_trophies",
            headers=headers,
            auth=requests.auth.HTTPDigestAuth(self._trophy_username, self._trophy_password),
            data=data,
        )
        xml = BeautifulSoup(request.text, 'lxml')
        game_trophies = list()
        for trophy in xml.findAll('trophy'):
            game_trophy = dict()
            game_trophy['id'] = trophy['id']
            if trophy['type'] == '0':
                game_trophy['type'] = 'bronze'
            elif trophy['type'] == '1':
                game_trophy['type'] = 'silver'
            elif trophy['type'] == '2':
                game_trophy['type'] = 'gold'
            else:
                game_trophy['type'] = 'platinum'
            game_trophy['date_obtained'] = trophy.text
            game_trophies.append(game_trophy)
        return json.dumps(game_trophies, indent=4, separators=(',', ': '))

