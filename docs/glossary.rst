=============
その他の用語
=============

全ての用語については :ref:`genindex` から参照して下さい。


.. glossary::

    用語名
        用語の説明を書いてください。
        :term:`Sphinx` のように書くことで用語への参照になります。

    AWS
        :term:`Amazon Web Services` の略称
        
    Amazon Web Services
        Amazonが提供するIaaS環境。
        
    Sheep dog
        KVM用の分散ストレージ
        Sheepdog/概要 - Eucalyptus linux4u.jp Wiki http://eucalyptus.linux4u.jp/wiki/index.php?Sheepdog%2F%E6%A6%82%E8%A6%81
        
    Sphinx
        Python製ドキュメンテーションビルダーです。
        reStructuredTextという文法で書かれたテキスト形式のドキュメントを
        HTML, PDF, ePub などに変換します。
        このドキュメントもSphinxを用いて作成しています。詳しくは
        
        * `Sphinx-Users.jp <http://sphinx-users.jp/>`_
        * `逆引き辞典 <http://sphinx-users.jp/reverse-dict/index.html>`_

    Starter Guide
        OpenStackのStarter Guideのこと。
        
        * `OpenStack Documentation - Diablo <http://docs.openstack.org/>`_
        
    Git
        分散型バージョン管理システム。
        OpenStackのソースはgithub上におかれているので、使えると便利。
        * Pro Git - Table of Contents http://progit.org/book/ja/

    Django
        dashboard(horizon)に使われているpython製のウェブフレームワーク

    Mercurial HG
        分散バージョン管理システム。Pythonで実装されています。GUI版として
        TortoiseHG が公開されており、グラフィカルなUIなどが使用できます。

    ブリッジ
        もともとは異なるセグメントを１つのセグメントに結合するもの。
        OpenStackでは仮想HUBを物理ネットワークとつなげるのに使っている。
        * ブリッジ接続 - Wikipedia http://ja.wikipedia.org/wiki/%E3%83%96%E3%83%AA%E3%83%83%E3%82%B8%E6%8E%A5%E7%B6%9A

    L2スイッチ
        L2スイッチとは、ネットワークを中継する機器のひとつで、
        パケットに宛先情報として含まれるMAC（Media Access Control）アドレスで中継先を判断し、中継動作を行うスイッチのことである。

        宛先MACアドレスでパケットの届け先を判断するという動作はLAN（Ethenet）の動作原理にならったものであり、
        LANはOSI参照モデルにおけるレイヤー2（データリンク層）に属するので、L（layer）2スイッチと呼ばれる。
        
        なお、L2スイッチの語は、おおむねTCP/IPなどのIPプロトコルなどが属するL3スイッチに対応する用語として用いられる。
        TCPやIP、HTTPなどのプロトコルは、レイヤー3（ネットワーク層）以上に位置しているため、L2スイッチがこうしたプロトコルの違いに左右されることはない。
        
        また、スイッチングハブは、動作原理から見ればL2スイッチと同じであり、
        これは小型で安価なL2スイッチとみなされるべきであるかもしれないが、
        しかしL2スイッチの語はおおむねスイッチングハブを除き、比較的大型の機種を指して用いられる場合が多い。
        * スイッチングハブ - Wikipedia http://ja.wikipedia.org/wiki/L2%E3%82%B9%E3%82%A4%E3%83%83%E3%83%81

    L3スイッチ
        L3スイッチとは、ネットワーク内でパケット交換を行うスイッチと呼ばれる装置の一種で、
        OSI参照モデルにおける第3層（ネットワーク層）においてパケットの送信先アドレスを
        振り分ける仕組みを持ったスイッチのことである。

        L3スイッチでは、ほとんどの場合、転送プロトコルにIPを用いる。
        ハードウェア的にスイッチングが行われるため、ソフトウェア的に処理を行うルータに比べても格段に高速であると言われている。
        ただし最近では機器の高性能化や多様化によってL3スイッチとルータの違いは薄れてきているとも言われている。

        L3スイッチに対して、OSI参照モデルにおける第2層（データリンク層）でスイッチングを行う装置はL2スイッチと呼ばれる。
        L2スイッチでは転送プロトコルとしてイーサネットなどを使用している。また、第4層（トランスポート層）で
        スイッチングを行う装置はL4スイッチと呼ばれている。L4ではTCPなどをプロトコルとして扱うことができる。
        * レイヤ3スイッチ - Wikipedia http://ja.wikipedia.org/wiki/L3%E3%82%B9%E3%82%A4%E3%83%83%E3%83%81

    VLAN
        VLAN(Virtual Local Area Network)は、スイッチなどのネットワーク機器の機能により、物理的な接続形態とは別に仮想的なネットワークを構成することである。スイッチの接続ポートやMACアドレス、プロトコルなどに応じて、端末のグループ化を実現する。
        * Virtual Local Area Network - Wikipedia http://ja.wikipedia.org/wiki/Virtual_Local_Area_Network

        LinuxではvconfigをVLANを設定することができる。

    TUN
        仮想ネットワークドライバ。ネットワーク層をシミュレートし、IPパケットなどを扱う。

    TAP
        仮想ネットワークドライバ。イーサネットデバイスをシミュレートし、データリンク層を扱う。
        

        

