Welcome to Cookipedia.Shinjuku
==============================

.. toctree::
   :maxdepth: 1

   articles/hoge.rst

Index
-----

* :ref:`genindex`

このドキュメントの作り方
------------------------

| ディレクトリ名を決めて ``sphinx-quickstart DIRNAME`` します。  
| 質問されるので適宜回答します。  
| ディレクトリができたらそこに移動します。

.. code-block:: console

   sphinx-quickstart cookipedia-shinjuku
   > Separate source and build directories (y/n) [n]: n
   > Project name: Cookipedia.Shinjuku
   > Author name(s): Chihiro Mihara
   > Project release []:
   > Project language [en]: ja

   cd cookipedia-shinjuku/


| 生成された ``conf.py`` を編集します。  
| 生成された ``_static/`` 以下に ``custom.css`` を作成して css をカスタマイズします。

.. code-block:: python
   :caption: conf.py

   html_theme = 'classic'
   html_css_files = ['custom.css']

.. code-block:: css
   :caption: _static/custom.css

   body { background: #5c1939; letter-spacing: 0.05em; }
   div.body { background-color: #f0f0f0; color: #444444; font-size: 94%; }
   div.footer { font-weight: bold; }
   div.sphinxsidebar h3, div.sphinxsidebar h4 { font-weight: bold; }
   div.body h1, div.body h2, div.body h3,
   div.body h4, div.body h5, div.body h6 {
       border-top: 1px solid #c0c0c0; border-bottom: 1px solid #c0c0c0;
       color: #7f2750; background-color: #e6e6e6; font-weight: bold; }
   div.body h1 { padding: 8px 0 8px 10px; border-top: 0; }
   div.related { background-color: #701c41; font-weight: bold; }
   div.document { background-color: #7f2750; }
   pre { border-top: 1px solid #bbd8a5; border-bottom: 1px solid #bbd8a5; }
   div.code-block-caption {
       border-top: 1px solid #bbd8a5; font-weight: bold;
       background-color: #ddf2bf; color: #7f2750; }
   div.sphinxsidebar a { color: #e7b2cb; }
   div.sphinxsidebar input { border: 1px solid #e0afde; }
   a { color: #7f2750; }
   a:visited { color: #7f2750; }
   a.headerlink  { color: #7f2750; }
   a.headerlink:hover { background-color: #7f2750; }
   input { color: #7f2750; }
   code { padding: 0.2em; background-color: #e6e6e6; }

| このようにして ``./make.bat html`` すると ``_build/html/index.html`` が生成されます。
| 同コマンドでリビルドできますが、カスタム css を変更した場合は先に ``./make.bat clean`` する必要があります。
| 以下のように ``index.rst`` を編集し ``articles/hoge.rst`` を追加して再実行するとページが増えます。
| 索引にも反映されます。

.. code-block:: rst
   :caption: index.rst

   Welcome to Cookipedia.Shinjuku
   ==============================

   .. toctree::
      :maxdepth: 1

      articles/hoge.rst

   Index
   -----

   * :ref:`genindex`

.. code-block:: rst
   :caption: articles/hoge.rst

   .. index::
      single: や; 山手線

   山手線
   ======

   .. index::
      single: し; 新宿駅

   新宿駅
   ------

   乗降客数が世界一多い。


   .. index::
      single: た; 高田馬場駅

   高田馬場駅
   ----------

   早稲田大学に近い。

   .. index::
      single: た; 高輪ゲートウェイ駅

   高輪ゲートウェイ駅
   ------------------

   新しい。

| サイドバーからドキュメント内を検索することもできます。
| しかし、「早稲田」では検索できますが「早稲田大学」では検索できません。
| なので `Sphinx の検索インデックス作成でMecabが使われるようにする <https://r-square.net/sphinx/03_sphinx_mecab.html>`_ を参考に MeCab を使います。
| そうすると「早稲田大学」で検索できるようになります。が、「早稲田」では検索できなくなります。
| また、GitHub Actions にビルドさせたいならこれをやると面倒になると思います (のでやめました)。

.. code-block:: python
   :caption: conf.py

   html_search_language = 'ja'
   html_search_options = {
       'type': 'sphinx.search.ja.MecabSplitter',
       'dic_enc': 'utf-8',
       'dict': '"C:\\Program Files\\MeCab\\dic\\ipadic"',
   }
