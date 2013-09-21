### Things to Note

* This uses a hacked together backdoor into the API, therefore it lacks such things as game names, trophy images, etc. It's better than nothing, credit to the people who found the backdoor.
* It would be wise to cache the JSON, making a request and parsing the response is a time-expensive task. Perhaps set a cron job to call this script every 24 hours or so.
* This may stop working at anytime, so be forewarned.
* Pull requests welcome. :)

### Samples

**Profile:**

```python
from psn import Psn


psn = Psn()
jid = psn.jid("Luumina")
print psn.profile(jid[0])
```

**JSON Ouput:**

```json
{
    "color": "393939ff",
    "country": "gb",
    "psn_plus": null,
    "avatar_url": "http://static-resource.np.community.playstation.net/avatar/3RD/UP43611208W01_5E8AE3139D24EE68D8A0_L.png",
    "about_me": "",
    "online_name": "Luumina"
}
```

**Trophies:**

```python
from psn import Psn


psn = Psn()
jid = psn.jid("Luumina")
print psn.trophies(jid[0])
```

**JSON Ouput:**

```json
{
    "points": "6165",
    "types": {
        "platinum": "1",
        "bronze": "191",
        "silver": "44",
        "gold": "20"
    },
    "levels": {
        "progress": "8",
        "base": "6000",
        "next": "8000"
    },
    "level": "7"
}
```

**Games:**

```python
from psn import Psn


psn = Psn()
jid = psn.jid("Luumina")
print psn.games(jid[0])
```

**JSON Ouput:**

```json
[
    {
        "npcommid": "NPWR03885_00",
        "last_updated": "2013-09-20T20:04:10Z",
        "trophies": {
            "platinum": "0",
            "bronze": "5",
            "silver": "0",
            "gold": "0"
        }
    },
    {
        "npcommid": "NPWR01818_00",
        "last_updated": "2013-09-17T20:29:10Z",
        "trophies": {
            "platinum": "0",
            "bronze": "5",
            "silver": "1",
            "gold": "0"
        }
    },
    {
        "npcommid": "NPWR01662_00",
        "last_updated": "2013-09-08T16:14:15Z",
        "trophies": {
            "platinum": "0",
            "bronze": "11",
            "silver": "0",
            "gold": "0"
        }
    },
    {
        "npcommid": "NPWR03546_00",
        "last_updated": "2013-09-07T18:41:26Z",
        "trophies": {
            "platinum": "0",
            "bronze": "20",
            "silver": "8",
            "gold": "1"
        }
    },
    {
        "npcommid": "NPWR00132_00",
        "last_updated": "2013-08-29T19:29:45Z",
        "trophies": {
            "platinum": "0",
            "bronze": "30",
            "silver": "2",
            "gold": "1"
        }
    },
    {
        "npcommid": "NPWR01008_00",
        "last_updated": "2013-08-11T15:03:21Z",
        "trophies": {
            "platinum": "0",
            "bronze": "5",
            "silver": "0",
            "gold": "0"
        }
    },
    {
        "npcommid": "NPWR00772_00",
        "last_updated": "2013-08-10T14:18:21Z",
        "trophies": {
            "platinum": "0",
            "bronze": "35",
            "silver": "9",
            "gold": "2"
        }
    },
    {
        "npcommid": "NPWR01566_00",
        "last_updated": "2013-07-24T20:04:37Z",
        "trophies": {
            "platinum": "0",
            "bronze": "13",
            "silver": "2",
            "gold": "0"
        }
    },
    {
        "npcommid": "NPWR01254_00",
        "last_updated": "2013-07-22T00:52:25Z",
        "trophies": {
            "platinum": "0",
            "bronze": "26",
            "silver": "12",
            "gold": "1"
        }
    },
    {
        "npcommid": "NPWR02303_00",
        "last_updated": "2013-07-12T00:14:49Z",
        "trophies": {
            "platinum": "0",
            "bronze": "2",
            "silver": "0",
            "gold": "0"
        }
    },
    {
        "npcommid": "NPWR03073_00",
        "last_updated": "2013-07-11T19:00:48Z",
        "trophies": {
            "platinum": "0",
            "bronze": "2",
            "silver": "2",
            "gold": "1"
        }
    },
    {
        "npcommid": "NPWR01605_00",
        "last_updated": "2013-07-02T14:56:08Z",
        "trophies": {
            "platinum": "0",
            "bronze": "30",
            "silver": "3",
            "gold": "2"
        }
    },
    {
        "npcommid": "NPWR00590_00",
        "last_updated": "2013-06-28T20:56:38Z",
        "trophies": {
            "platinum": "0",
            "bronze": "7",
            "silver": "4",
            "gold": "1"
        }
    },
    {
        "npcommid": "NPWR02044_00",
        "last_updated": "2013-06-21T15:51:48Z",
        "trophies": {
            "platinum": "1",
            "bronze": "0",
            "silver": "1",
            "gold": "11"
        }
    }
]
```

**Game Trophies:**

```python
from psn import Psn


psn = Psn()
jid = psn.jid('Luumina')
print psn.game_trophies(jid[0], 'NPWR02044_00')
```

**JSON Ouput:**

```json
[
    {
        "date_obtained": "2013-06-21T15:51:00Z",
        "type": "platinum",
        "id": "1"
    },
    {
        "date_obtained": "2013-06-21T15:22:29Z",
        "type": "gold",
        "id": "2"
    },
    {
        "date_obtained": "2013-06-21T12:32:57Z",
        "type": "gold",
        "id": "3"
    },
    {
        "date_obtained": "2013-06-21T15:24:39Z",
        "type": "gold",
        "id": "4"
    },
    {
        "date_obtained": "2013-06-21T14:59:14Z",
        "type": "gold",
        "id": "5"
    },
    {
        "date_obtained": "2013-06-21T15:50:59Z",
        "type": "gold",
        "id": "6"
    },
    {
        "date_obtained": "2013-06-21T15:34:02Z",
        "type": "gold",
        "id": "7"
    },
    {
        "date_obtained": "2013-06-21T15:19:00Z",
        "type": "gold",
        "id": "8"
    },
    {
        "date_obtained": "2013-06-21T15:11:05Z",
        "type": "gold",
        "id": "9"
    },
    {
        "date_obtained": "2013-06-21T13:41:32Z",
        "type": "gold",
        "id": "10"
    },
    {
        "date_obtained": "2013-06-21T15:43:54Z",
        "type": "gold",
        "id": "11"
    },
    {
        "date_obtained": "2013-06-21T12:27:17Z",
        "type": "gold",
        "id": "12"
    },
    {
        "date_obtained": "2013-06-21T12:11:20Z",
        "type": "silver",
        "id": "13"
    }
]
```

### License

*No license, use as you wish.*