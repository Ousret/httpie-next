HTTPie Extra!
-------------

This plugin brings experimental support for urllib3\[h2n3\] (not released, not planned for merge, not planned to, not eligible for support!)
Use this plugin with caution.

```shell
pip install git+https://github.com/Ousret/httpie-next -U

# run twice! first is http/2 and second should be http/3
https GET www.cloudflare.com/img/nav/globe-lang-select-dark.svg
```

When a server yield its QUIC support, it is saved in default httpie configuration directory.
Installing this in your environment will alter basically everything that relies on urllib3.

Your feedbacks are appreciated so that we can prepare a safe (and actually reviewable / merge-able feature) in urllib3.
