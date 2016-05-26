roan's blog

-> sdn
傳統：分散式
每個封包在每個機器都算一次

sdn:（網路設計理念）
data plane 切斷 control plane
dummy switch... 所有的packet routing 由controller 決定

app layer（rest api）
controller layer(安裝套件)
infrastructure layer

chipset:
intel, broadcom, intel(x64)
BOX:
edge-core網通設備, qunta computer廣達（server）, dell
NEtworkOS:類比 cisco,jyuper 的IOS
現在的OS可自選～
open switch
ONL open networking linux...debian based
Lagopus(JP)

big switch + openstack
cumulus linux + openstack
pica8 （OS廠商有提供相容的硬體表）
-> onos 2016
edge-core網通設備, qunta computer廣達（server）


# controller
## open daylight-設備商（好賣
## onos－電信商（應用很多
    Carrier Grade
    ONOS cluster
    NB app(程式寫在這裡)->controller
    分散式的instances, ONOS把你把分散的東西都處理掉
    SB(南向)->controller->


### ONOS(proxy奇數, 選取機制有關) SDN-IP（BGP？EBGP（模擬）
    VMWARE ESX （VSS(問題在此？)-VM）
        Quagga1, 2? (hypervisor1, 2)
        ONOS cluster 1~3 (hypervisor)

    NCTU->KREONET韓->INTERNET2
    NCTU->AmLight美
    send stream, 沒掉一個封包
    1. 畫出拓撲
    2.
    3. 建置團隊
    4. 專案控管
    EDGEcore switch

## 功能性驗證
1. 硬體switch manual white paper 不能相信(不一定都有實作)
    * 類似OPENVSwitch  一條一條加 flow
    * controller提供的restful API安裝flow
拿到switch+下flow+測試（要5個小時@@）

Ansible+Git
幫你管理群組cmd example:
ansible all -m command -a  'uptime'

ONIE+Pica8
## Ryu－NTT（好上手

mininet+Ryu
