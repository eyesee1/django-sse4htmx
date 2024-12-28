# Django SSE4HTMX

A simple wrapper around [Django EventStream's](https://github.com/fanout/django-eventstream) `send_event` to make it
simpler to send a properly formatted HTML fragment rendered from a template or a partial (if you
have [django-template-partials](https://github.com/carltongibson/django-template-partials/tree/main) installed). It
gives you a similar feel to Django's class-based views (CBVs).

## Installation

Install the package using `uv`:

```bash
uv add django-sse4htmx
```

Install the package using `pip`:

```bash
pip install django-sse4htmx
```

Install the package using `poetry`:

```bash
poetry add django-sse4htmx
```

## Usage

```python

from django_sse4htmx import ServerSentEventHTMLFragmentSender


class MyEventSender(ServerSentEventHTMLFragmentSender):
    channel_name = 'my_channel'
    template_name = 'my_template.html#my_partial'

    def get_context_data(self):
        return {
            'my_context': 'my_context_value',
            'request': self.kwargs.get('request'),
        }


# in your code anywhere such as a view, a signal responder,
# a queued task in a task queue, etc.:

MyEventSender()(value="some value")
```

Any keyword arguments passed to the `__call__` method will be passed to the template or partial as context variables.

## Gotchas

- The current request and other values that are normally in the template context will not be there unless you pass them
  explicitly as keyword arguments to the `__call__` method (as shown in the example above). The current
  request is only available from a view or a middleware, so you may need to adjust your templates (or partials)
  accordingly if your template code assumes their presence.

## Code of Conduct

- If contributing or participating in this project in any way, including posting issues or feature requests, you are
  expected to abide by
  the [Python Software Foundation's Code of Conduct](https://policies.python.org/python.org/code-of-conduct/).

## Roadmap

1. ✅ Initial release, works in quick manual testing with the sample project.
2. Add Unit Tests
3. Support for i18n/l10n given a language code.
4. Consider adding a way to send multiple events at once (if users even want it, which could happen since HTMX supports
   it)

## Contributing

- Your changes should pass the linter: `ruff check`
- Your changes should be formatted with `ruff format`
- Please fork the repository, make your changes on a new branch, then submit a Pull Request against `main`.

## Changes

- 0.1.0: Initial release 2024-12-27

## License

MIT License

Copyright (c) 2024 Duna Mae Cat

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
