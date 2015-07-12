import mistune


def test_escape():
    ret = mistune.markdown('<div>**foo**</div>', escape=True)
    assert '&gt;' in ret

    ret = mistune.markdown('this **foo** is <b>bold</b>', escape=True)
    assert '&gt;' in ret


def test_linebreak():
    ret = mistune.markdown('this **foo** \nis me')
    assert '<br>' not in ret

    ret = mistune.markdown('this **foo** \nis me', hard_wrap=True)
    assert '<br>' in ret


def test_safe_links():
    ret = mistune.markdown('javascript ![foo](<javascript:alert>) alert')
    assert 'src=""' in ret
    ret = mistune.markdown('javascript [foo](<javascript:alert>) alert')
    assert 'href=""' in ret


def test_skip_style():
    ret = mistune.markdown(
        'foo\n<style>body{color:red}</style>', skip_style=True
    )
    assert ret == '<p>foo</p>\n'


def test_use_xhtml():
    ret = mistune.markdown('foo\n\n----\n\nbar')
    assert '<hr>' in ret
    ret = mistune.markdown('foo\n\n----\n\nbar', use_xhtml=True)
    assert '<hr />' in ret

    ret = mistune.markdown('foo  \nbar', use_xhtml=True)
    assert '<br />' in ret

    ret = mistune.markdown('![foo](bar "title")', use_xhtml=True)
    assert '<img src="bar" alt="foo" title="title" />' in ret


def test_parse_html():
    ret = mistune.markdown('<div>**foo**</div>', escape=False)
    assert '<strong>' not in ret
    ret = mistune.markdown(
        '<div>**foo**</div>', parse_html=True, escape=False
    )
    assert '<strong>' in ret

    ret = mistune.markdown('<span>**foo**</span>', escape=False)
    assert '<strong>' not in ret
    ret = mistune.markdown(
        '<span>**foo**</span>', parse_html=True, escape=False
    )
    assert '<strong>' in ret

    ret = mistune.markdown(
        '<span>http://example.com</span>', parse_html=True, escape=False
    )
    assert 'href' in ret
    ret = mistune.markdown(
        '<a>http://example.com</a>', parse_html=True, escape=False
    )
    assert 'href' not in ret


def test_parse_inline_html():
    ret = mistune.markdown(
        '<div>**foo**</div>', parse_inline_html=True, escape=False
    )
    assert '<strong>' not in ret
    ret = mistune.markdown(
        '<span>**foo**</span>', parse_inline_html=True, escape=False
    )
    assert '<strong>' in ret


def test_parse_block_html():
    ret = mistune.markdown(
        '<div>**foo**</div>', parse_block_html=True, escape=False
    )
    assert '<strong>' in ret
    ret = mistune.markdown(
        '<span>**foo**</span>', parse_block_html=True, escape=False
    )
    assert '<strong>' not in ret


def test_trigger_more_cases():
    markdown = mistune.Markdown(
        inline=mistune.InlineLexer,
        block=mistune.BlockLexer,
        skip_html=True
    )
    ret = markdown.render('foo[^foo]\n\n[^foo]: foo\n\n[^foo]: bar\n')
    assert 'bar' not in ret


def test_not_escape_block_tags():
    text = '<h1>heading</h1> text'
    assert text in mistune.markdown(text, escape=False)
