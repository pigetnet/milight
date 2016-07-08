| /do/milight/blue   |                                                                         |
|:-------------------|:------------------------------------------------------------------------|
| Info               | [alpha] [undocumented]                                                  |
| Modules            | python3 /do/milight/python/milight.py -i milight.local -c $1 --cc aqua, |

| /do/milight/bright   |                                                                       |
|:---------------------|:----------------------------------------------------------------------|
| Info                 | [alpha] [undocumented]                                                |
| Modules              | python3 /do/milight/python/milight.py -i milight.local -c $1 --br 25, |

| /do/milight/color   |                                                                       |
|:--------------------|:----------------------------------------------------------------------|
| Info                | [alpha] [undocumented]                                                |
| Modules             | python3 /do/milight/python/milight.py -i milight.local -c $1 --cc $2, |

| /do/milight/dim   |                                                                      |
|:------------------|:---------------------------------------------------------------------|
| Info              | [alpha] [undocumented]                                               |
| Modules           | python3 /do/milight/python/milight.py -i milight.local -c $1 --br 5, |

| /do/milight/green   |                                                                          |
|:--------------------|:-------------------------------------------------------------------------|
| Info                | [alpha] [undocumented]                                                   |
| Modules             | python3 /do/milight/python/milight.py -i milight.local -c $1 --cc green, |

| /do/milight/help   |                                               |
|:-------------------|:----------------------------------------------|
| Info               | [alpha] [undocumented]                        |
| Modules            | python3 /do/milight/python/milight.py --help, |


| /do/milight/milight   |                                           |
|:----------------------|:------------------------------------------|
| Info                  | [alpha] [undocumented]                    |
| Modules               | python3 /do/milight/python/milight.py $@, |

| /do/milight/off   |                                                                     |
|:------------------|:--------------------------------------------------------------------|
| Info              | [alpha] [undocumented]                                              |
| Modules           | python3 /do/milight/python/milight.py -i milight.local -c $1 --off, |

| /do/milight/on   |                                                                    |
|:-----------------|:-------------------------------------------------------------------|
| Info             | [alpha] [undocumented]                                             |
| Modules          | python3 /do/milight/python/milight.py -i milight.local -c $1 --on, |

| /do/milight/pair              |                                                                                                            |
|:------------------------------|:-----------------------------------------------------------------------------------------------------------|
| Info                          | [alpha] [undocumented]                                                                                     |
| Variables                     | ip=$(/do/milight/scan), isIP=$(/show/isIP $ip), repair=$(/string/searchString /etc/hosts "milight.local"), |
| Modules                       | ip=$(/do/milight/scan),                                                                                    |
| 1. [MILIGHT] Pairing gateway  |                                                                                                            |
| 1. $ip --> milight.local      |                                                                                                            |
| 2. $ip --> milight.local      |                                                                                                            |
| 3. No milight gateway founded |                                                                                                            |

| /do/milight/red   |                                                                        |
|:------------------|:-----------------------------------------------------------------------|
| Info              | [alpha] [undocumented]                                                 |
| Modules           | python3 /do/milight/python/milight.py -i milight.local -c $1 --cc red, |

| /do/milight/scan   |                                                                                                    |
|:-------------------|:---------------------------------------------------------------------------------------------------|
| Info               | [alpha] [undocumented]                                                                             |
| Variables          | ip=$(python3 /do/milight/python/milight.py --scan|grep "ip address"|awk '{print $4}'), ip=${ip:1}, |
| Modules            | ip=$(python3 /do/milight/python/milight.py --scan|grep "ip address"|awk '{print $4}'),             |

| /do/milight/white   |                                                                    |
|:--------------------|:-------------------------------------------------------------------|
| Info                | [alpha] [undocumented]                                             |
| Modules             | python3 /do/milight/python/milight.py -i milight.local -c $1 --ew, |

| /do/milight/yellow   |                                                                           |
|:---------------------|:--------------------------------------------------------------------------|
| Info                 | [alpha] [undocumented]                                                    |
| Modules              | python3 /do/milight/python/milight.py -i milight.local -c $1 --cc yellow, |

