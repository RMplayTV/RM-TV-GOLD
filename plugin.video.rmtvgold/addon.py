plugin.video.rmtvgold/addon.py

<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<addons>
    <addon id="plugin.video.rmtvgold"
           name="RM TV GOLD"
           version="1.0.0"
           provider-name="RMplayTV">

        <requires>
            <import addon="xbmc.python" version="3.0.0"/>
        </requires>

        <extension point="xbmc.python.pluginsource" library="addon.py">
            <provides>video</provides>
        </extension>

        <extension point="xbmc.addon.metadata">
            <summary>RM TV GOLD</summary>
            <description>TV, Filmes, Séries, Animes e Desenhos</description>
            <platform>all</platform>
        </extension>

    </addon>
</addons>
