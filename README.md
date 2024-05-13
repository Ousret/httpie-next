HTTPie Extra!
-------------

This plugin brings support for HTTP/2 and HTTP/3 to HTTPie.
Use this plugin with caution as it uses urllib3.future (and actually shadows urllib3 in your environment).

```shell
pip install httpie-next -U

# run twice! first is http/2 and second should be http/3
https GET www.cloudflare.com/img/nav/globe-lang-select-dark.svg
```

When a server yield its QUIC support, it is saved in the default HTTPie configuration directory.

⚠️ This project is deprecated and is unmaintained. See https://github.com/httpie/cli/pull/1531 for a viable alternative.
