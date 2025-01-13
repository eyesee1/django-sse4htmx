# Django SSE4HTMX

A simple wrapper around [Django EventStream](https://github.com/fanout/django-eventstream)'s `send_event` to make it
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

from django_sse4htmx import SSEFragmentSender


class MyEventSender(SSEFragmentSender):
    channel_name = 'my_channel'
    template_name = 'my_template.html#my_partial'

    def get_context_data(self):
        # here you can add custom context data to be passed to the template or partial
        return {
            'my_context': 'my_context_value',
            'request': self.kwargs.get('request'),
        }


# in your code anywhere such as a view, a signal responder,
# a queued task in a task queue, etc.:

MyEventSender()(value="some value")  # value is passed to the template or partial as a context variable

# if that syntax bothers you, can also use the `send` method:

MyEventSender().send(value="some value")

# Alternatively if you will use the same sender more than once:

my_sender = MyEventSender()
my_sender(value="some value")
my_sender(value="another value")
my_sender.send(value="yet another value")
```

Any keyword arguments passed to the `__call__` or `send` method will be passed to the template or partial as context
variables.

## Gotchas

- The current request and other values which are normally in the template context will not be there unless you pass them
  explicitly as keyword arguments to the `__call__` or `send` method (as shown in the example above). The current
  request is only available from a view or a middleware, so you may need to adjust your templates (or partials)
  accordingly if your existing template code assumes their presence.

## Code of Conduct

- If contributing or participating in this project in any way, including posting issues or feature requests, you are
  expected to abide by
  the [Python Software Foundation's Code of Conduct](https://policies.python.org/python.org/code-of-conduct/).

## Roadmap

- [x] Initial release, works in quick manual testing with the sample project.
- [ ] Add Unit Tests
- [ ] tox
- [ ] improve documentation
- [ ] Support for i18n/l10n given a language code?
- [ ] Consider adding a way to send multiple events at once (if users even want it, which could happen since HTMX
      supports it)
- [ ] Clean up the demo page layout a bit. It's admittedly rushed, just to get something working quickly.

## Running the Example Project

- [Install `uv`](https://docs.astral.sh/uv/getting-started/installation/) if you haven't already.
- Clone the repository
- `cd` into the cloned repository, then into example
- `uv sync --all-groups` to install the dependencies
- `source .venv/bin/activate`
- `python manage.py runserver`
- Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser

You can watch the JavaScript console to see debugging logs as SSE messages are received.

## Contributing

- The project is using pre-commit hooks to set code style and standards.
- Please fork the repository, install pre-commit `uv tool install pre-commit`, make your changes on a new branch, then
  submit a Pull Request against `main`.

## Changes

- 0.1.1: added repo urls to project config

- 0.1.0: Initial release 2025-01-13

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

---

[There is still time.](https://www.tillystranstuesdays.com/2024/09/03/the-intentional-trans-allegory-of-i-saw-the-tv-glow-part-1/)
