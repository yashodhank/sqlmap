#!/usr/bin/env python

"""
Copyright (c) 2006-2018 sqlmap developers (http://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""

optDict = {
    # Family: {"parameter name": "parameter datatype"},
    # --OR--
    # Family: {"parameter name": ("parameter datatype", "category name used for common outputs feature")},

    "Target": {
        "direct": "string",
        "url": "string",
        "logFile": "string",
        "bulkFile": "string",
        "requestFile": "string",
        "sessionFile": "string",
        "googleDork": "string",
        "configFile": "string",
        "sitemapUrl": "string",
    },

    "Request": {
        "method": "string",
        "data": "string",
        "paramDel": "string",
        "cookie": "string",
        "cookieDel": "string",
        "loadCookies": "string",
        "dropSetCookie": "boolean",
        "agent": "string",
        "randomAgent": "boolean",
        "host": "string",
        "referer": "string",
        "headers": "string",
        "authType": "string",
        "authCred": "string",
        "authFile": "string",
        "ignoreCode": "integer",
        "ignoreProxy": "boolean",
        "ignoreRedirects": "boolean",
        "ignoreTimeouts": "boolean",
        "proxy": "string",
        "proxyCred": "string",
        "proxyFile": "string",
        "tor": "boolean",
        "torPort": "integer",
        "torType": "string",
        "checkTor": "boolean",
        "delay": "float",
        "timeout": "float",
        "retries": "integer",
        "rParam": "string",
        "safeUrl": "string",
        "safePost": "string",
        "safeReqFile": "string",
        "safeFreq": "integer",
        "skipUrlEncode": "boolean",
        "csrfToken": "string",
        "csrfUrl": "string",
        "forceSSL": "boolean",
        "hpp": "boolean",
        "evalCode": "string",
    },

    "Optimization": {
        "optimize": "boolean",
        "predictOutput": "boolean",
        "keepAlive": "boolean",
        "nullConnection": "boolean",
        "threads": "integer",
    },

    "Injection": {
        "testParameter": "string",
        "skip": "string",
        "skipStatic": "boolean",
        "paramExclude": "string",
        "dbms": "string",
        "dbmsCred": "string",
        "os": "string",
        "invalidBignum": "boolean",
        "invalidLogical": "boolean",
        "invalidString": "boolean",
        "noCast": "boolean",
        "noEscape": "boolean",
        "prefix": "string",
        "suffix": "string",
        "tamper": "string",
    },

    "Detection": {
        "level": "integer",
        "risk": "integer",
        "string": "string",
        "notString": "string",
        "regexp": "string",
        "code": "integer",
        "textOnly": "boolean",
        "titles": "boolean",
    },

    "Techniques": {
        "tech": "string",
        "timeSec": "integer",
        "uCols": "string",
        "uChar": "string",
        "uFrom": "string",
        "dnsDomain": "string",
        "secondUrl": "string",
    },

    "Fingerprint": {
        "extensiveFp": "boolean",
    },

    "Enumeration": {
        "getAll": "boolean",
        "getBanner": ("boolean", "Banners"),
        "getCurrentUser": ("boolean", "Users"),
        "getCurrentDb": ("boolean", "Databases"),
        "getHostname": "boolean",
        "isDba": "boolean",
        "getUsers": ("boolean", "Users"),
        "getPasswordHashes": ("boolean", "Passwords"),
        "getPrivileges": ("boolean", "Privileges"),
        "getRoles": ("boolean", "Roles"),
        "getDbs": ("boolean", "Databases"),
        "getTables": ("boolean", "Tables"),
        "getColumns": ("boolean", "Columns"),
        "getSchema": "boolean",
        "getCount": "boolean",
        "dumpTable": "boolean",
        "dumpAll": "boolean",
        "search": "boolean",
        "getComments": "boolean",
        "db": "string",
        "tbl": "string",
        "col": "string",
        "exclude": "string",
        "pivotColumn": "string",
        "dumpWhere": "string",
        "user": "string",
        "excludeSysDbs": "boolean",
        "limitStart": "integer",
        "limitStop": "integer",
        "firstChar": "integer",
        "lastChar": "integer",
        "query": "string",
        "sqlShell": "boolean",
        "sqlFile": "string",
    },

    "Brute": {
        "commonTables": "boolean",
        "commonColumns": "boolean",
    },

    "User-defined function": {
        "udfInject": "boolean",
        "shLib": "string",
    },

    "File system": {
        "rFile": "string",
        "wFile": "string",
        "dFile": "string",
    },

    "Takeover": {
        "osCmd": "string",
        "osShell": "boolean",
        "osPwn": "boolean",
        "osSmb": "boolean",
        "osBof": "boolean",
        "privEsc": "boolean",
        "msfPath": "string",
        "tmpPath": "string",
    },

    "Windows": {
        "regRead": "boolean",
        "regAdd": "boolean",
        "regDel": "boolean",
        "regKey": "string",
        "regVal": "string",
        "regData": "string",
        "regType": "string",
    },

    "General": {
        # "xmlFile": "string",
        "trafficFile": "string",
        "batch": "boolean",
        "binaryFields": "string",
        "charset": "string",
        "checkInternet": "boolean",
        "crawlDepth": "integer",
        "crawlExclude": "string",
        "csvDel": "string",
        "dumpFormat": "string",
        "encoding": "string",
        "eta": "boolean",
        "flushSession": "boolean",
        "forms": "boolean",
        "freshQueries": "boolean",
        "harFile": "string",
        "hexConvert": "boolean",
        "outputDir": "string",
        "parseErrors": "boolean",
        "saveConfig": "string",
        "scope": "string",
        "testFilter": "string",
        "testSkip": "string",
        "updateAll": "boolean",
    },

    "Miscellaneous": {
        "alert": "string",
        "answers": "string",
        "beep": "boolean",
        "cleanup": "boolean",
        "dependencies": "boolean",
        "disableColoring": "boolean",
        "googlePage": "integer",
        "identifyWaf": "boolean",
        "mobile": "boolean",
        "offline": "boolean",
        "purgeOutput": "boolean",
        "skipWaf": "boolean",
        "smart": "boolean",
        "tmpDir": "string",
        "webRoot": "string",
        "wizard": "boolean",
        "verbose": "integer",
    },

    "Hidden": {
        "dummy": "boolean",
        "disablePrecon": "boolean",
        "profile": "boolean",
        "forceDns": "boolean",
        "murphyRate": "integer",
        "smokeTest": "boolean",
        "liveTest": "boolean",
        "stopFail": "boolean",
        "runCase": "string",
    },

    "API": {
        "api": "boolean",
        "taskid": "string",
        "database": "string",
    }
}
