### How to use

Download psn.py and included it in your projects, a demo has been included (demo.py). By default, it returns data in json format but you can eaisly customise this to your needs.

**Demo.py:**

```python
from psn import Psn


psn = Psn()
jid = psn.jid("Luumina")
print psn.profile(jid[0])
```

**Will return:**

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

*No license, use as you wish.*