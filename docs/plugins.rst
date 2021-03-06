.. _plugins:

Mistune Markdown Plugins
========================


strikethrough
-------------

.. code-block:: text

    ~~here is the content~~

``mistune.html()`` has enabled strikethrough plugin by default. To create
a markdown instance your own::

    markdown = mistune.create_markdown(plugins=['strikethrough'])

Another way to create your own Markdown instance::

    from mistune.plugins import plugin_strikethrough

    renderer = mistune.HTMLRenderer()
    markdown = mistune.Markdown(renderer, plugins=[plugin_strikethrough])


footnotes
---------

.. code-block:: text

    content in paragraph with footnote[^1] markup.

    [^1]: footnote explain


``mistune.html()`` has enabled footnote plugin by default. To create
a markdown instance your own::

    markdown = mistune.create_markdown(plugins=['footnotes'])

Another way to create your own Markdown instance::

    from mistune.plugins import plugin_footnotes

    renderer = mistune.HTMLRenderer()
    markdown = mistune.Markdown(renderer, plugins=[plugin_footnotes])


table
-----

Simple formatted table:

.. code-block:: text

    First Header  | Second Header
    ------------- | -------------
    Content Cell  | Content Cell
    Content Cell  | Content Cell
    
Complex formatted table:

.. code-block:: text

    | First Header  | Second Header |
    | ------------- | ------------- |
    | Content Cell  | Content Cell  |
    | Content Cell  | Content Cell  |

Align formatted table:

.. code-block:: text

     Left Header |  Center Header  | Right Header
    :----------- | :-------------: | ------------:
     Conent Cell |  Content Cell   | Content Cell


    | Left Header |  Center Header  | Right Header  |
    | :---------- | :-------------: | ------------: |
    | Conent Cell |  Content Cell   | Content Cell  |

``mistune.html()`` has enabled table plugin by default. To create
a markdown instance your own::

    markdown = mistune.create_markdown(plugins=['table'])

Another way to create your own Markdown instance::

    from mistune.plugins import plugin_table

    renderer = mistune.HTMLRenderer()
    markdown = mistune.Markdown(renderer, plugins=[plugin_table])


url
---

URL plugin enables creating link with raw URL by default:

.. code-block:: text

    For instance, https://typlog.com/

Will be converted into:

.. code-block:: html

    <p>For instance, <a href="https://typlog.com/>https://typlog.com/</a></p>

This plugin is **NOT ENABLED** by default in ``mistune.html()``. Mistune
values explicit, and we suggest writers to write links in:

.. code-block:: text

    <https://typlog.com/>

To enable **url** plugin with your own markdown instance::

    markdown = mistune.create_markdown(plugins=['url'])

Another way to create your own Markdown instance::

    from mistune.plugins import plugin_url

    renderer = mistune.HTMLRenderer()
    markdown = mistune.Markdown(renderer, plugins=[plugin_url])

task_lists
----------

Task lists plugin enables creating GitHub todo items:

.. code-block:: text

    - [x] item 1
    - [ ] item 2

Will be converted into:

.. code-block:: html

    <ul>
    <li class="task-list-item"><input class="task-list-item-checkbox" type="checkbox" disabled checked/>item 1</li>
    <li class="task-list-item"><input class="task-list-item-checkbox" type="checkbox" disabled/>item 2</li>
    </ul>


This plugin is **NOT ENABLED** by default in ``mistune.html()``. To enable
**task_lists** plugin with your own markdown instance::

    markdown = mistune.create_markdown(plugins=['task_lists'])

Another way to create your own Markdown instance::

    from mistune.plugins import plugin_task_lists

    renderer = mistune.HTMLRenderer()
    markdown = mistune.Markdown(renderer, plugins=[plugin_task_lists])
