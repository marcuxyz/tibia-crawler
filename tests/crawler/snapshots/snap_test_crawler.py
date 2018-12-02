# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['test_tibia_search_character 1'] = {
    'account_status': 'Premium Account',
    'achievement': '141',
    'created_at': GenericRepr("FakeDatetime(2018, 12, 12, 0, 0)"),
    'deaths': [
        {
            'description': 'Died at Level 543 by a hellflayer.',
            'timestamp': 'Nov 25 2018, 19:49:43 CET'
        },
        {
            'description': 'Killed  at Level 544 by Rosha Runner and a plaguesmith.',
            'timestamp': 'Nov 25 2018, 19:28:25 CET'
        },
        {
            'description': 'Killed  at Level 541 by Rosha Runner and a plaguesmith.',
            'timestamp': 'Nov 22 2018, 18:29:04 CET'
        },
        {
            'description': 'Died at Level 542 by a grimeleech.',
            'timestamp': 'Nov 22 2018, 16:48:41 CET'
        },
        {
            'description': 'Died at Level 535 by Grand Master Oberon.',
            'timestamp': 'Nov 15 2018, 00:52:05 CET'
        },
        {
            'description': 'Eliminated  at Level 533 by Enri Crys, Rhuar, Zippow Ba, Majkel De Lavega, Zevelina, Temudjinn, Silvfix, Demonique, Bossesaurus Rex, Siliana, Vanxi, Blue Tree, Lord Toivic, Archmage Jaina Proudmoore, Zuzulanka and Don Gregor Corleone.Assisted by Miichal, Easy Kuba, Sick Joe and Unlegitrod.',
            'timestamp': 'Nov 13 2018, 22:54:50 CET'
        },
        {
            'description': 'Killed  at Level 530 by Rosha Runner and a demon.',
            'timestamp': 'Nov 10 2018, 17:24:01 CET'
        },
        {
            'description': 'Crushed  at Level 526 by Ruhar, Ingen Ba, Terror Janek, Zevelina, Neph Thol, Izidor, Silvfix, Bossesaurus Rex, Gonzo piaty waza, Don Mefju, Chrysaor Dardanos, Matew, Pain Drain and Xerxes magik.Assisted by Queen Smoka.',
            'timestamp': 'Nov 06 2018, 00:08:52 CET'
        },
        {
            'description': 'Eliminated  at Level 526 by Ruhar, Ingen Ba, Terror Janek, Zevelina, Neph Thol, Izidor, Silvfix, Bossesaurus Rex, Sio Generation, Don Mefju, Chrysaor Alexander, Main Priority, Pain Drain, Bill The Headcase and Xerxes magik.Assisted by Don Kaizer, Pzyclones and Spiworek Highlights.',
            'timestamp': 'Nov 06 2018, 00:02:04 CET'
        }
    ],
    'extract_former_name': 'Orzesz Ty',
    'last_login': 'Dec 01 2018, 15:02:58 CET',
    'level': '548',
    'name': 'Rosha Runner',
    'residence': 'Roshamuul',
    'sex': 'male',
    'vocation': 'Elder Druid',
    'word': 'Antica'
}
