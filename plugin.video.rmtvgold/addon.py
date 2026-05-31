# -*- coding: utf-8 -*-

import sys
import urllib.parse
import xbmcplugin
import xbmcgui

HANDLE = int(sys.argv[1])


# ---------------------------
# FUNÇÃO PARA CRIAR URL
# ---------------------------
def build_url(query):
    return sys.argv[0] + '?' + urllib.parse.urlencode(query)


# ---------------------------
# ADICIONAR MENU
# ---------------------------
def add_item(title, action, is_folder=True):
    url = build_url({'action': action})
    li = xbmcgui.ListItem(label=title)
    xbmcplugin.addDirectoryItem(HANDLE, url, li, is_folder)


# ---------------------------
# MENU PRINCIPAL
# ---------------------------
def home():
    add_item("📺 TV AO VIVO", "tv")
    add_item("🎬 FILMES", "filmes")
    add_item("📺 SÉRIES", "series")
    add_item("🎌 ANIMES", "animes")
    add_item("🧸 DESENHOS", "desenhos")
    add_item("🔞 +18", "adulto")
    add_item("🔎 PESQUISA", "search")
    add_item("⚙️ CONFIGURAÇÕES", "config")

    xbmcplugin.endOfDirectory(HANDLE)


# ---------------------------
# SUBMENUS (PLACEHOLDER)
# ---------------------------
def placeholder(nome):
    li = xbmcgui.ListItem(label=f"Entrou em: {nome}")
    xbmcplugin.addDirectoryItem(HANDLE, "", li, False)
    xbmcplugin.endOfDirectory(HANDLE)


# ---------------------------
# ROUTER (NAVEGAÇÃO)
# ---------------------------
def router(param):
    if param is None:
        home()

    elif param == "tv":
        placeholder("TV AO VIVO")

    elif param == "filmes":
        placeholder("FILMES")

    elif param == "series":
        placeholder("SÉRIES")

    elif param == "animes":
        placeholder("ANIMES")

    elif param == "desenhos":
        placeholder("DESENHOS")

    elif param == "adulto":
        placeholder("+18")

    elif param == "search":
        placeholder("PESQUISA")

    elif param == "config":
        placeholder("CONFIGURAÇÕES")

    else:
        home()


# ---------------------------
# CAPTURA DE PARAMETROS
# ---------------------------
params = dict(urllib.parse.parse_qsl(sys.argv[2][1:]))

action = params.get('action')

router(action)
